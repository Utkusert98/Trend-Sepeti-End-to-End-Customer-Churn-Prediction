import pandas as pd
import sqlite3
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# --- SETTINGS ---
print("🤖 AI Engine Starting...")
conn = sqlite3.connect('trend_sepeti.db')
df = pd.read_sql("SELECT * FROM transactions", conn)
conn.close()

# Data Preparation (Recalculating RFM for AI Input)
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
analysis_date = dt.datetime(2024, 1, 1)

rfm = df.groupby('Customer_ID').agg({
    'Order_Date': lambda x: (analysis_date - x.max()).days,
    'Order_ID': 'count',
    'Unit_Price': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# --- ARTIFICIAL INTELLIGENCE SECTION ---

# 1. TARGET DEFINITION (Labeling)
# Teaching the machine: Who is 'Churn'?
# Rule: If Recency > 120 days, Churn = 1 (Lost), else 0 (Retained)
rfm['Churn'] = rfm['Recency'].apply(lambda x: 1 if x > 120 else 0)

# 2. DATA SPLITTING (Training & Testing)
# X: Features (The clues: Recency, Frequency, Monetary)
# y: Target (The answer: Churn or Not?)
X = rfm[['Recency', 'Frequency', 'Monetary']]
y = rfm['Churn']

# Split data: 80% for studying (Train), 20% for exams (Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. MODEL TRAINING (Random Forest)
# A powerful model that uses multiple decision trees (The "Forest")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. MAKE PREDICTIONS
y_pred = model.predict(X_test)

print("\n✅ Model Training Completed.")
print(f"Model Accuracy: %{model.score(X_test, y_test) * 100:.2f}")

# --- VISUALIZATION (FOR CV PORTFOLIO) ---

# PLOT 1: Customer Segments (Churn Analysis)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Churn', palette='coolwarm', alpha=0.7)
plt.title('Customer Churn Analysis (Red = Churn)')
plt.xlabel('Days Since Last Visit (Recency)')
plt.ylabel('Total Spend (Monetary)')
plt.legend(title='Churn Status')
plt.savefig('1_Customer_Churn_Analysis.png')
print("🖼️  Image 1 Saved: 1_Customer_Churn_Analysis.png")

# PLOT 2: AI Performance (Confusion Matrix)
plt.figure(figsize=(6, 5))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title('AI Prediction Success (Confusion Matrix)')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.savefig('2_AI_Performance.png')
print("🖼️  Image 2 Saved: 2_AI_Performance.png")

# PLOT 3: Feature Importance (What matters most?)
plt.figure(figsize=(8, 4))
feature_imp = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
sns.barplot(x=feature_imp, y=feature_imp.index, palette='viridis')
plt.title('Top Factors Affecting Churn')
plt.xlabel('Importance Score')
plt.savefig('3_Feature_Importance.png')
print("🖼️  Image 3 Saved: 3_Feature_Importance.png")

print("\n🚀 ALL PROCESSES FINISHED! Check your folder for images.")
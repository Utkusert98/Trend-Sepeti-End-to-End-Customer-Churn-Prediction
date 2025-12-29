import pandas as pd
import sqlite3
import datetime as dt

# 1. SETUP CONNECTION (Reading from the database)
conn = sqlite3.connect('trend_sepeti.db')
df = pd.read_sql("SELECT * FROM transactions", conn)
conn.close()

# 2. DATE CONFIGURATION
# Converting string dates to datetime objects
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# 3. SET ANALYSIS DATE (Assuming today is Jan 1, 2024)
analysis_date = dt.datetime(2024, 1, 1)

print("📊 Data Loaded. Calculating RFM Metrics...")

# 4. RFM CALCULATION
rfm = df.groupby('Customer_ID').agg({
    'Order_Date': lambda x: (analysis_date - x.max()).days, # Recency
    'Order_ID': 'count',                                    # Frequency
    'Unit_Price': 'sum'                                     # Monetary
})

# Rename columns to standard RFM terminology
rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\n--- TOP 10 CUSTOMER SCORECARDS ---")
print(rfm.head(10))

# Customer Segmentation Logic
# Rule: If a customer hasn't visited in > 100 days, mark as 'At Risk'
def define_segment(days):
    if days > 100:
        return "At Risk (Churn)"
    else:
        return "Loyal (Active)"

# Apply the segmentation rule
rfm['Segment'] = rfm['Recency'].apply(define_segment)

print("\n--- CUSTOMER SEGMENTATION REPORT ---")
print(rfm['Segment'].value_counts())
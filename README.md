🛒 Trend Sepeti: End-to-End Customer Churn Prediction
📋 Project Overview
Trend Sepeti is an end-to-end Data Science project designed to solve a critical business problem: Customer Churn.

This project simulates a real-world e-commerce environment to analyze customer behavior. It processes raw transaction data, segments customers using RFM Analysis, and deploys a Machine Learning model (Random Forest) to predict which customers are likely to stop purchasing.

🏗️ Architecture & Workflow
The project follows a structured Data Pipeline:

Data Generation (Simulation): Created a synthetic dataset (data_generator.py) representing 2,000+ realistic e-commerce transactions, including customer demographics, categories, and order statuses.

ETL & Database Design: Built an ETL process (setup_db.py) to extract raw CSV data, transform formats, and load it into a structured SQLite database for scalability.

RFM Analysis (Feature Engineering): Calculated Recency, Frequency, and Monetary metrics (rfm_analysis.py) to segment customers into "Loyal" and "At Risk" groups.

Predictive Modeling (AI): Developed a Random Forest Classifier (trend_sepeti_ai.py) to predict customer churn with high accuracy (>90%).

🛠️ Tech Stack
Language: Python 3

Database: SQLite (Relational DB)

Data Manipulation: Pandas, NumPy

Machine Learning: Scikit-Learn (Random Forest)

Visualization: Matplotlib, Seaborn

📊 Key Insights & Results
The Artificial Intelligence model revealed critical business insights:

Prediction Accuracy: The model achieved over 90% accuracy in distinguishing between retained and churned customers.

Primary Churn Factor: The Feature Importance analysis demonstrated that Recency (Days since last visit) is the strongest predictor of churn, outweighing Total Spend (Monetary).

Visualizations
(Please upload your generated PNG images here)

Fig 1: Customer Churn Analysis (Scatter Plot)

Fig 2: AI Confusion Matrix (Model Performance)

Fig 3: Feature Importance (Top Factors)

🚀 How to Run
Clone the repository:

Bash

git clone https://github.com/utkusert/trend-sepeti-project.git
Install dependencies:

Bash

pip install pandas scikit-learn matplotlib seaborn
Run the pipeline:

Bash

python3 data_generator.py   # Generate Data
python3 setup_db.py         # Build Database
python3 trend_sepeti_ai.py  # Train AI & Visualize
👨‍💻 Author
Utku Sert

Full Stack & AI Developer

[[LinkedIn Profile Link](https://www.linkedin.com/in/utku-sert-/)]

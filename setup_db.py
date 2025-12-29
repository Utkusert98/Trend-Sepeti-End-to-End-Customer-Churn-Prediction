import pandas as pd
import sqlite3
import os 

csv_file = 'ecommerce_data.csv'
db_file = 'trend_sepeti.db'

print("🚀 Starting Data Ingestion Process...")

if not os.path.exists(csv_file):
    print(f"❌ CSV file '{csv_file}' not found. Please run the data generator first.")
    exit()

try:
    print(f"📥 Reading data from '{csv_file}'...")
    df = pd.read_csv(csv_file)
    
    print(f"Connecting to database: {db_file}...")
    conn = sqlite3.connect(db_file)
    
    print("Writing data to SQL table 'transactions'...")
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    
    print("✅ SUCCESS: Database setup complete.")
    
    print("\n--- SQL TEST: First 3 Orders ---")
    test_query = "SELECT * FROM transactions LIMIT 3;"
    test_result = pd.read_sql(test_query, conn)
    print(test_result)
    
    conn.close()
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    
    
    
"""
connect_rds_mysql.py

This script connects to an Amazon RDS MySQL instance using Python and the PyMySQL library.
It demonstrates how to connect, create a table, and insert a sample record.

Prerequisites:
- An RDS MySQL instance with public access and correct security group settings.
- Python 3.x with PyMySQL installed.
"""

import pymysql

# Replace the following with your RDS details
RDS_HOST = 'your-db-endpoint.rds.amazonaws.com'
RDS_PORT = 3306
RDS_USER = 'admin'
RDS_PASSWORD = 'yourpassword'
RDS_DB = 'yourdatabase'

try:
    # Establish connection to RDS
    conn = pymysql.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )
    print("✅ Connected to RDS successfully!")

    with conn.cursor() as cursor:
        # Create a table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            score FLOAT
        );
        """)
        print("🧱 Table checked/created.")

        # Insert a sample record
        cursor.execute("INSERT INTO predictions (name, score) VALUES (%s, %s)", ("Sample", 0.95))
        conn.commit()
        print("📥 Inserted sample data into table.")

    conn.close()
    print("🔌 Connection closed.")

except Exception as e:
    print("❌ Error connecting to RDS:", e)


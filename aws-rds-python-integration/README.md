# AWS RDS MySQL Integration with Python

This repository demonstrates how to connect a Python application to an Amazon RDS MySQL instance. It includes an example of creating a table and inserting data into it.

## Services Used
- **Amazon RDS** (MySQL)
- **Python 3**
- **PyMySQL**

---

## Prerequisites

1. **AWS Account**
2. **Amazon RDS MySQL instance**
   - Public accessibility: **enabled**
   - Inbound rule in **Security Group** allowing port **3306** from your IP
3. **AWS CLI configured**
4. **Python Environment**

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/aws-rds-python-integration.git
cd aws-rds-python-integration
pip install pymysql
```

## Usage
Edit the connect_rds_mysql.py file and update these placeholders:
```
RDS_HOST = 'your-db-endpoint.rds.amazonaws.com'
RDS_USER = 'admin'
RDS_PASSWORD = 'yourpassword'
RDS_DB = 'yourdatabase'

```

Then run the script:

```
python connect_rds_mysql.py

```
## Output
- Connects to the RDS instance

- Creates a table predictions if it doesn't exist

- Inserts a sample record (Sample, 0.95)

- Closes the connection


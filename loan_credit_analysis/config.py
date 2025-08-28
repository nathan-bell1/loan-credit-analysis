import os

# Project root directory
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# Data folder and database path
DB_DIR = os.path.join(ROOT_DIR, "data")
DB_PATH = os.path.join(DB_DIR, "loan_portfolio.db")

# Ensure data directory exists
os.makedirs(DB_DIR, exist_ok=True)

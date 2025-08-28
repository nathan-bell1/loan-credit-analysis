import sqlite3
from loan_credit_analysis.config import DB_PATH

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop tables if re-running
    cursor.execute("DROP TABLE IF EXISTS borrowers")
    cursor.execute("DROP TABLE IF EXISTS loans")
    cursor.execute("DROP TABLE IF EXISTS payments")

    # Create borrowers table
    cursor.execute("""
    CREATE TABLE borrowers (
        borrower_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        income REAL,
        credit_score INTEGER
    )
    """)

    # Create loans table
    cursor.execute("""
    CREATE TABLE loans (
        loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
        borrower_id INTEGER,
        amount REAL,
        interest_rate REAL,
        term_months INTEGER,
        status TEXT,
        FOREIGN KEY(borrower_id) REFERENCES borrowers(borrower_id)
    )
    """)

    # Create payments table
    cursor.execute("""
    CREATE TABLE payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        loan_id INTEGER,
        payment_month INTEGER,
        amount REAL,
        on_time BOOLEAN,
        FOREIGN KEY(loan_id) REFERENCES loans(loan_id)
    )
    """)

    conn.commit()
    conn.close()
    print(f"Database created at {DB_PATH}")

if __name__ == "__main__":
    create_database()

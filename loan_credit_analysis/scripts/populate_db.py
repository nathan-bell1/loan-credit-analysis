import sqlite3
import random
from faker import Faker
from loan_credit_analysis.config import DB_PATH

fake = Faker()

def populate_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insert fake borrowers
    for _ in range(1000):
        name = fake.name()
        age = random.randint(21, 70)
        income = round(random.uniform(30000, 150000), 2)
        credit_score = random.randint(300, 850)
        cursor.execute(
            "INSERT INTO borrowers (name, age, income, credit_score) VALUES (?, ?, ?, ?)",
            (name, age, income, credit_score)
        )


    # Insert fake loans
    for borrower_id in range(1, 1001):
        # Fetch this borrower's credit score
        credit_score = cursor.execute(
            "SELECT credit_score FROM borrowers WHERE borrower_id = ?",
            (borrower_id,)
        ).fetchone()[0]

        for _ in range(random.randint(1, 5)):  # 1–5 loans per borrower
            amount = round(random.uniform(1000, 50000), 2)
            term = random.choice([12, 24, 36, 60])  # months
            status = random.choice(["active", "defaulted", "paid_off"])

            # Interest rate depends on credit score
            if credit_score < 580:
                base_rate = 15.0
            elif credit_score < 670:
                base_rate = 12.0
            elif credit_score < 740:
                base_rate = 9.0
            elif credit_score < 800:
                base_rate = 6.0
            else:  # 800–850
                base_rate = 4.0

            # Add slight randomness so it’s not fixed
            interest_rate = round(random.uniform(base_rate - 1, base_rate + 1.5), 2)

            cursor.execute("""
                INSERT INTO loans (borrower_id, amount, interest_rate, term_months, status)
                VALUES (?, ?, ?, ?, ?)
            """, (borrower_id, amount, interest_rate, term, status))


    # Insert fake payments
    loan_ids = [row[0] for row in cursor.execute("SELECT loan_id FROM loans").fetchall()]
    for loan_id in loan_ids:
        num_payments = random.randint(6, 60)
        for month in range(1, num_payments + 1):
            amount = round(random.uniform(50, 2000), 2)
            on_time = random.choice([True, False, True])
            cursor.execute(
                "INSERT INTO payments (loan_id, payment_month, amount, on_time) VALUES (?, ?, ?, ?)",
                (loan_id, month, amount, on_time)
            )

    conn.commit()
    conn.close()
    print("Database populated with fake data")

if __name__ == "__main__":
    populate_database()

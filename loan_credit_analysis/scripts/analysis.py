import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from loan_credit_analysis.config import DB_PATH

def run_analysis():
    conn = sqlite3.connect(DB_PATH)

    # Query 1: Count credit scores and sort into rating buckets
    query1 = """
    SELECT
        CASE
            WHEN credit_score < 580 THEN 'Poor'
            WHEN credit_score BETWEEN 580 AND 669 THEN 'Fair'
            WHEN credit_score BETWEEN 670 AND 739 THEN 'Good'
            WHEN credit_score BETWEEN 740 AND 799 THEN 'Very Good'
            ELSE 'Excellent'
        END AS credit_category,
        COUNT(*) AS borrower_count
    FROM borrowers
    GROUP BY credit_category
    ORDER BY borrower_count DESC
    """
    credit_df = pd.read_sql_query(query1, conn)
    print(credit_df)

    # Plot borrower distrubution by credit category
    plt.figure(figsize=(8,5))
    sns.barplot(x='credit_category', y='borrower_count', data=credit_df)
    plt.title("Borrowers by Credit Score Category")
    plt.ylabel("Number of Borrowers")
    plt.xlabel("Credit Category")
    plt.tight_layout()
    plt.show()

    # Query 2: Collect interest rate and credit score for each buyer's payment
    query2 = """
    SELECT
        b.credit_score,
        l.interest_rate
    FROM borrowers b
    JOIN loans l ON b.borrower_id = l.borrower_id
    """
    loan_df = pd.read_sql_query(query2, conn)

    # Add credit categories to pandas dataframe
    bins = [0, 579, 669, 739, 799, 850]
    labels = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
    loan_df['credit_category'] = pd.cut(loan_df['credit_score'], bins=bins, labels=labels)

    # Group and average dataframe categories
    avg_interest = loan_df.groupby('credit_category', observed=False)['interest_rate'].mean().reset_index()
    print(avg_interest)

    # Plot the average interest rate for each category
    plt.figure(figsize=(8,5))
    sns.barplot(x='credit_category', y='interest_rate', data=avg_interest)
    plt.title("Average Loan Interest Rate by Credit Category")
    plt.ylabel("Average Interest Rate (%)")
    plt.xlabel("Credit Category")
    plt.tight_layout()
    plt.show()

    conn.close()

if __name__ == "__main__":
    run_analysis()

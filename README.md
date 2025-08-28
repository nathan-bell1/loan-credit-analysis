# Loan Credit Analysis

This python repository generates a simulated loan database in SQLite, then analyzes and visualizes average interest rates by credit category using SQL queries, grouping, and plotting with pandas and seaborn.

---

## Overview
This project generates a simulated loan database using SQLite and Python, then performs analysis on loan interest rates across different credit score categories. It demonstrates database creation, SQL querying, data manipulation with `pandas`, and visualization using `seaborn` and `matplotlib`.

---

## Features
- Generate a realistic dataset of borrowers, loans, and payments using Python `Faker`.
- Store data in a **SQLite** database.
- Perform SQL queries to group, aggregate, and filter loan data.
- Analyze average interest rates by credit score category.
- Visualize trends with bar plots.

---

## Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/loan-credit-analysis.git
cd loan-credit-analysis
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```
3. **Install dependencies**
```bash
pip install -e .
```
---

## Usage

Run the main script:
```bash
python main.py
```

This will:
- Create and Query the SQLite database.
- Compute average interest rates by credit score category.
- Display bar plots of interest trends.

---

## Dependencies
Python 3.10 (recommended)
- pandas
- matplotlib
- seaborn
- Faker
- sqlite3 (built-in)

---

## License

This project is licensed under the MIT License.

---
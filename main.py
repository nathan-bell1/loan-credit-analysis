import subprocess
import sys

def run_module(module_name):
    result = subprocess.run([sys.executable, module_name], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("[ERRORS/WARNINGS]", result.stderr)

if __name__ == "__main__":
    print("=== Loan Credit Analysis ===")

    # Setup database
    run_module("loan_credit_analysis/scripts/setup_db.py")

    # Populate database with synthetic data
    run_module("loan_credit_analysis/scripts/populate_db.py")

    # Run analysis and plots
    run_module("loan_credit_analysis/scripts/analysis.py")

    print("\n=== Complete! ===")

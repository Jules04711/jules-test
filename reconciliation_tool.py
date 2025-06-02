# This script needs refactoring and improvements:
# 1. Poor code organization
# 2. Missing dependencies handling
# 3. No unit tests
# 4. Hardcoded configurations
# 5. Poor documentation

import pandas as pd
import numpy as np

# Issue: Global variables instead of configuration
TOLERANCE = 0.01
BANK_ACCOUNT = "123456789"

def reconcile_accounts(bank_file, ledger_file):
    # Issue: No error handling for file operations
    bank_df = pd.read_csv(bank_file)
    ledger_df = pd.read_csv(ledger_file)
    
    # Issue: Assumes specific column names without validation
    bank_df['date'] = pd.to_datetime(bank_df['transaction_date'])
    ledger_df['date'] = pd.to_datetime(ledger_df['entry_date'])
    
    # Issue: Inefficient matching algorithm
    matched_transactions = []
    unmatched_bank = bank_df.copy()
    unmatched_ledger = ledger_df.copy()
    
    for bank_idx, bank_row in bank_df.iterrows():
        for ledger_idx, ledger_row in ledger_df.iterrows():
            # Issue: Simple matching logic that could miss valid matches
            if (abs(bank_row['amount'] - ledger_row['amount']) <= TOLERANCE and
                bank_row['date'] == ledger_row['date']):
                matched_transactions.append({
                    'bank_id': bank_row['id'],
                    'ledger_id': ledger_row['id'],
                    'amount': bank_row['amount'],
                    'date': bank_row['date']
                })
                # Issue: Inefficient removal from dataframes
                unmatched_bank = unmatched_bank[unmatched_bank['id'] != bank_row['id']]
                unmatched_ledger = unmatched_ledger[unmatched_ledger['id'] != ledger_row['id']]
                break
    
    return matched_transactions, unmatched_bank, unmatched_ledger

def calculate_reconciliation_summary(matched, unmatched_bank, unmatched_ledger):
    # Issue: No input validation
    summary = {}
    summary['matched_count'] = len(matched)
    summary['matched_amount'] = sum([t['amount'] for t in matched])
    summary['unmatched_bank_count'] = len(unmatched_bank)
    summary['unmatched_ledger_count'] = len(unmatched_ledger)
    
    # Issue: Potential division by zero
    total_transactions = len(matched) + len(unmatched_bank) + len(unmatched_ledger)
    summary['match_rate'] = len(matched) / total_transactions * 100
    
    return summary

def export_reconciliation_results(matched, unmatched_bank, unmatched_ledger, output_dir):
    # Issue: No directory creation or existence check
    matched_df = pd.DataFrame(matched)
    matched_df.to_csv(f"{output_dir}/matched_transactions.csv", index=False)
    unmatched_bank.to_csv(f"{output_dir}/unmatched_bank.csv", index=False)
    unmatched_ledger.to_csv(f"{output_dir}/unmatched_ledger.csv", index=False)

# Issue: No proper CLI interface or configuration management
if __name__ == "__main__":
    matched, unmatched_b, unmatched_l = reconcile_accounts("bank.csv", "ledger.csv")
    summary = calculate_reconciliation_summary(matched, unmatched_b, unmatched_l)
    print(f"Reconciliation complete. Match rate: {summary['match_rate']:.2f}%")
    export_reconciliation_results(matched, unmatched_b, unmatched_l, "output")

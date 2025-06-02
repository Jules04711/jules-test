# This script has several issues that Jules can fix:
# 1. Deprecated pandas syntax
# 2. Poor error handling
# 3. No logging
# 4. No type hints
# 5. Hard-coded values

import pandas as pd
import re
from datetime import datetime

def process_invoices(file_path):
    # Issue: Using deprecated pandas syntax
    df = pd.read_csv(file_path, encoding='utf-8')
    
    # Issue: No error handling for missing columns
    df['invoice_date'] = pd.to_datetime(df['date'])
    df['amount'] = df['amount'].str.replace('$', '').str.replace(',', '')
    df['amount'] = pd.to_numeric(df['amount'])
    
    # Issue: Hard-coded tax rate
    df['tax_amount'] = df['amount'] * 0.08
    df['total_amount'] = df['amount'] + df['tax_amount']
    
    # Issue: Poor validation logic
    valid_invoices = df[df['amount'] > 0]
    
    # Issue: No logging of processing results
    return valid_invoices

def validate_invoice_number(invoice_num):
    # Issue: Basic regex that could be improved
    pattern = r'^INV-\d{4}'
    return re.match(pattern, invoice_num) is not None

def generate_report(invoices_df):
    # Issue: No error handling for empty dataframe
    total_revenue = invoices_df['total_amount'].sum()
    invoice_count = len(invoices_df)
    
    # Issue: Hard-coded file path
    report_path = '/tmp/invoice_report.txt'
    
    with open(report_path, 'w') as f:
        f.write(f"Invoice Report - {datetime.now()}\n")
        f.write(f"Total Invoices: {invoice_count}\n")
        f.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    
    return report_path

# Issue: No main function or proper entry point
if __name__ == "__main__":
    # Issue: Hard-coded file path
    invoices = process_invoices("invoices.csv")
    report = generate_report(invoices)
    print(f"Report generated: {report}")

# This script lacks proper testing and documentation:
# 1. No unit tests
# 2. Missing docstrings
# 3. No input validation
# 4. Poor exception handling
# 5. No audit trail logging

import json
from datetime import datetime, timedelta
from decimal import Decimal

class GAAPreporter:
    def __init__(self, company_name):
        self.company_name = company_name
        self.reporting_period = None
        self.financial_data = {}
    
    def set_reporting_period(self, start_date, end_date):
        # Issue: No date validation
        self.reporting_period = {
            'start': start_date,
            'end': end_date
        }
    
    def add_revenue_data(self, revenue_items):
        # Issue: No validation of revenue data structure
        self.financial_data['revenue'] = revenue_items
    
    def add_expense_data(self, expense_items):
        # Issue: No validation of expense data structure  
        self.financial_data['expenses'] = expense_items
    
    def calculate_revenue_recognition(self):
        # Issue: Simplified revenue recognition logic
        if 'revenue' not in self.financial_data:
            return 0
        
        total_revenue = 0
        for item in self.financial_data['revenue']:
            # Issue: No proper date checking for revenue recognition
            if item['type'] == 'subscription':
                # Simple monthly recognition
                total_revenue += item['amount'] / 12
            else:
                total_revenue += item['amount']
        
        return total_revenue
    
    def validate_expense_matching(self):
        # Issue: Basic expense matching without proper GAAP principles
        if 'expenses' not in self.financial_data:
            return True
        
        valid_expenses = []
        for expense in self.financial_data['expenses']:
            # Issue: Oversimplified validation
            if expense['amount'] > 0 and 'date' in expense:
                valid_expenses.append(expense)
        
        return len(valid_expenses) == len(self.financial_data['expenses'])
    
    def generate_compliance_report(self):
        # Issue: No comprehensive compliance checking
        report = {
            'company': self.company_name,
            'period': self.reporting_period,
            'timestamp': datetime.now().isoformat(),
            'revenue_recognition': self.calculate_revenue_recognition(),
            'expense_validation': self.validate_expense_matching(),
            'compliance_score': 85  # Issue: Hard-coded score
        }
        
        # Issue: No audit trail or logging
        return report
    
    def export_to_json(self, filename):
        # Issue: No error handling for file operations
        report = self.generate_compliance_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)

def create_sample_data():
    # Issue: Sample data without proper structure validation
    revenue_data = [
        {'type': 'sale', 'amount': 50000, 'date': '2024-01-15'},
        {'type': 'subscription', 'amount': 12000, 'date': '2024-01-01'},
        {'type': 'sale', 'amount': 75000, 'date': '2024-02-10'}
    ]
    
    expense_data = [
        {'category': 'operating', 'amount': 25000, 'date': '2024-01-10'},
        {'category': 'marketing', 'amount': 15000, 'date': '2024-01-20'},
        {'category': 'salaries', 'amount': 80000, 'date': '2024-01-31'}
    ]
    
    return revenue_data, expense_data

# Issue: No proper main function structure
if __name__ == "__main__":
    reporter = GAAPreporter("Example Corp")
    reporter.set_reporting_period("2024-01-01", "2024-03-31")
    
    revenue, expenses = create_sample_data()
    reporter.add_revenue_data(revenue)
    reporter.add_expense_data(expenses)
    
    reporter.export_to_json("compliance_report.json")
    print("Compliance report generated successfully")

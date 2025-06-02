# Jules Testing Scripts for YouTube Demo

This repository contains Python scripts designed to test Google Jules' autonomous coding capabilities for a YouTube demonstration. Each script has intentional issues and areas for improvement that showcase Jules' abilities.

## Scripts Overview

### 1. invoice_processor.py
**Issues to fix:**
- Deprecated pandas syntax
- Missing error handling
- No logging implementation
- Missing type hints
- Hard-coded configuration values

**Jules tasks to assign:**
- "Fix deprecated pandas syntax in invoice_processor.py"
- "Add proper error handling and logging to invoice processing functions"
- "Add type hints and improve code documentation"

### 2. reconciliation_tool.py
**Issues to fix:**
- Poor code organization and structure
- Inefficient matching algorithms
- Missing input validation
- No configuration management

**Jules tasks to assign:**
- "Refactor reconciliation_tool.py for better performance and readability"
- "Add input validation and error handling to reconciliation functions"
- "Implement proper configuration management"

### 3. compliance_reporter.py
**Issues to fix:**
- No unit tests
- Missing docstrings and documentation
- Poor exception handling
- No audit trail logging

**Jules tasks to assign:**
- "Add comprehensive unit tests for compliance_reporter.py"
- "Add detailed docstrings and improve documentation"
- "Implement audit trail logging for compliance operations"

### 4. financial_dashboard.py
**Issues to fix:**
- Outdated Streamlit syntax
- Missing security validation
- Poor state management
- No proper error handling

**Jules tasks to assign:**
- "Update financial_dashboard.py to use latest Streamlit best practices"
- "Add file upload security validation and error handling"
- "Improve dashboard layout and user experience"

## How to Use with Jules

1. **Create a GitHub repository** with these files
2. **Create GitHub issues** for each task you want Jules to handle
3. **Add the label** `assign-to-jules` to the issues
4. **Review Jules' plans** before approving execution
5. **Test the improvements** Jules makes

## Sample GitHub Issues to Create

### Issue 1: Fix Deprecated Code
```
Title: Fix deprecated pandas syntax in invoice processor
Label: assign-to-jules
Description: The invoice_processor.py file uses deprecated pandas syntax that may cause warnings or errors in newer versions. Please update to modern pandas best practices.
```

### Issue 2: Add Tests
```
Title: Add unit tests for compliance reporter
Label: assign-to-jules  
Description: The compliance_reporter.py needs comprehensive unit tests to ensure financial calculations are accurate and GAAP compliant.
```

### Issue 3: Security Improvements
```
Title: Add security validation to dashboard file uploads
Label: assign-to-jules
Description: The financial_dashboard.py needs proper file validation and security checks for uploaded CSV files.
```

## Expected Improvements After Jules

- Modern, maintainable code following Python best practices
- Comprehensive error handling and logging
- Security improvements for file operations
- Unit tests with good coverage
- Updated dependencies and syntax
- Better documentation and type hints
- Improved performance and code organization

## Video Demonstration Tips

1. **Start with the problematic code** - show the issues
2. **Create clear GitHub issues** - demonstrate the assignment process
3. **Show Jules' planning phase** - review the proposed changes
4. **Test before and after** - demonstrate the improvements
5. **Highlight key features** like async execution and pull request workflow

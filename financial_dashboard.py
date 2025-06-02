# This Streamlit app needs dependency updates and improvements:
# 1. Outdated Streamlit syntax
# 2. Missing requirements.txt
# 3. No proper state management
# 4. Poor data validation
# 5. Security issues with file uploads

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# Issue: Using deprecated Streamlit syntax
st.set_page_config(page_title="Financial Dashboard", layout="wide")

# Issue: No proper session state management
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False

def load_financial_data(uploaded_file):
    # Issue: No file validation or security checks
    if uploaded_file is not None:
        try:
            # Issue: Assumes CSV format without checking
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            # Issue: Poor error handling
            st.error(f"Error loading file: {e}")
            return None
    return None

def create_revenue_chart(df):
    # Issue: No data validation
    if 'date' in df.columns and 'revenue' in df.columns:
        # Issue: Using older plotly syntax
        fig = px.line(df, x='date', y='revenue', title='Revenue Trend')
        return fig
    else:
        # Issue: Poor error messaging
        st.error("Invalid data format")
        return None

def calculate_kpis(df):
    # Issue: No error handling for missing columns
    kpis = {}
    kpis['total_revenue'] = df['revenue'].sum()
    kpis['avg_monthly_revenue'] = df['revenue'].mean()
    kpis['max_revenue'] = df['revenue'].max()
    
    # Issue: No validation for division by zero
    kpis['growth_rate'] = (df['revenue'].iloc[-1] - df['revenue'].iloc[0]) / df['revenue'].iloc[0] * 100
    
    return kpis

def main():
    st.title("Financial Performance Dashboard")
    
    # Issue: Poor layout organization
    st.sidebar.header("Data Upload")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file:
        df = load_financial_data(uploaded_file)
        
        if df is not None:
            st.session_state.data_loaded = True
            
            # Issue: No data preview or validation step
            st.subheader("Financial Overview")
            
            # Issue: Poor column layout
            col1, col2, col3, col4 = st.columns(4)
            
            kpis = calculate_kpis(df)
            
            # Issue: No formatting for currency display
            col1.metric("Total Revenue", f"${kpis['total_revenue']:,.2f}")
            col2.metric("Avg Monthly", f"${kpis['avg_monthly_revenue']:,.2f}")
            col3.metric("Peak Revenue", f"${kpis['max_revenue']:,.2f}")
            col4.metric("Growth Rate", f"{kpis['growth_rate']:.1f}%")
            
            # Issue: No proper chart container
            st.subheader("Revenue Trend")
            chart = create_revenue_chart(df)
            if chart:
                st.plotly_chart(chart, use_container_width=True)
            
            # Issue: Raw data display without pagination
            st.subheader("Raw Data")
            st.dataframe(df)
            
            # Issue: No data export functionality
            if st.button("Generate Report"):
                # Issue: No actual report generation
                st.success("Report generated successfully!")
    
    else:
        # Issue: Poor user guidance
        st.info("Please upload a CSV file to get started.")

# Issue: No proper error handling or logging
if __name__ == "__main__":
    main()

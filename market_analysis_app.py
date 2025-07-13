
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Market Analysis Tool", layout="wide")

st.title("📊 Market Analysis Automation Tool")

st.sidebar.header("🔍 Analysis Setup")
industry = st.sidebar.text_input("Enter Industry", "Storage Battery")
company = st.sidebar.text_input("Enter Company Name", "VoltEdge Energy Solutions")

st.header("1. SWOT Analysis")
cols = st.columns(4)
swot_labels = ["Strengths", "Weaknesses", "Opportunities", "Threats"]
swot_data = {}

for col, label in zip(cols, swot_labels):
    swot_data[label] = col.text_area(label, height=150)

st.header("2. PESTEL Analysis")
pestel_factors = ["Political", "Economic", "Social", "Technological", "Environmental", "Legal"]
pestel_data = {}

for factor in pestel_factors:
    pestel_data[factor] = st.text_area(f"**{factor} Factors**", height=100)

st.header("3. Financial Ratios Calculator")
col1, col2 = st.columns(2)
with col1:
    revenue = st.number_input("Revenue (₦)", value=0.0)
    cogs = st.number_input("Cost of Goods Sold (₦)", value=0.0)
    net_profit = st.number_input("Net Profit (₦)", value=0.0)
    current_assets = st.number_input("Current Assets (₦)", value=0.0)
    current_liabilities = st.number_input("Current Liabilities (₦)", value=0.0)
with col2:
    total_debt = st.number_input("Total Debt (₦)", value=0.0)
    equity = st.number_input("Shareholders' Equity (₦)", value=0.0)
    net_income = st.number_input("Net Income (₦)", value=0.0)

st.subheader("📈 Calculated Financial Ratios")
try:
    st.write(f"**Gross Margin:** {((revenue - cogs) / revenue) * 100:.2f}%" if revenue else "Gross Margin: -")
    st.write(f"**Net Profit Margin:** {(net_profit / revenue) * 100:.2f}%" if revenue else "Net Profit Margin: -")
    st.write(f"**Current Ratio:** {(current_assets / current_liabilities):.2f}" if current_liabilities else "Current Ratio: -")
    st.write(f"**Debt-to-Equity Ratio:** {(total_debt / equity):.2f}" if equity else "Debt-to-Equity Ratio: -")
    st.write(f"**Return on Equity (ROE):** {(net_income / equity) * 100:.2f}%" if equity else "ROE: -")
except Exception as e:
    st.error(f"Error in calculation: {e}")

st.header("4. Competitor Benchmarking")
st.markdown("Add details of competitors below:")
competitor_df = pd.DataFrame({
    "Competitor": ["Competitor A", "Competitor B"],
    "Market Share (%)": ["", ""],
    "Strengths": ["", ""],
    "Weaknesses": ["", ""],
    "Price Range (₦)": ["", ""],
    "Product Quality": ["", ""],
    "Distribution Channels": ["", ""]
})
edited_df = st.data_editor(competitor_df, num_rows="dynamic")

if st.button("📤 Export Report (Coming Soon)"):
    st.info("Export feature will be available in full release.")

st.success("✅ Market analysis inputs saved. You can now generate insights or use this template for business planning.")

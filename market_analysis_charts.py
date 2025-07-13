# Generate full Streamlit code to embed financial and competitor charts

chart_integration_code = """
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Market Analysis Charts")

# User financial inputs
st.header("1️⃣ Financial Overview")
revenue = st.number_input("Revenue (₦)", value=120_000_000)
cogs = st.number_input("Cost of Goods Sold (₦)", value=70_000_000)
net_profit = st.number_input("Net Profit (₦)", value=15_000_000)

# Plot bar chart
fig1, ax1 = plt.subplots()
labels = ['Revenue', 'COGS', 'Net Profit']
values = [revenue, cogs, net_profit]
bars = ax1.bar(labels, values, color=['green', 'red', 'blue'])
ax1.set_title("Financial Overview")
ax1.set_ylabel("Amount (₦)")
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 1e6, f"₦{int(yval/1e6)}M", ha='center', va='bottom')
st.pyplot(fig1)

# Competitor market share
st.header("2️⃣ Competitor Market Share")
competitor_df = pd.DataFrame({
    'Competitor': ['VoltEdge', 'Competitor A', 'Competitor B'],
    'Market Share (%)': [50, 30, 20]
})
edited_df = st.data_editor(competitor_df, num_rows="dynamic")

# Plot pie chart
fig2, ax2 = plt.subplots()
ax2.pie(edited_df['Market Share (%)'],
        labels=edited_df['Competitor'],
        autopct='%1.1f%%',
        startangle=90)
ax2.axis('equal')
ax2.set_title("Competitor Market Share")
st.pyplot(fig2)
"""

# Save to new Streamlit file for chart visualization
chart_app_path = "/mnt/data/market_analysis_charts.py"
with open(chart_app_path, "w") as f:
    f.write(chart_integration_code)

chart_app_path

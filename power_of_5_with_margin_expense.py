
import streamlit as st

st.set_page_config(page_title="Power of 5 Profit Growth Planner", layout="centered")
st.title("📈 Power of 5 Profit Growth Planner")

st.markdown("Use the inputs below to compare your current business metrics to projected improvements using the ActionCOACH Power of 5 formula.")

# Input columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔹 Current Business Metrics")
    leads_current = st.number_input("Leads", min_value=0, value=1000, step=50, key="leads_current")
    conversion_current = st.slider("Conversion Rate (%)", 0.0, 100.0, 25.0, key="conv_current")
    transactions_current = st.number_input("Transactions per Customer", 0.0, value=2.0, step=0.1, key="trans_current")
    avg_sale_current = st.number_input("Average Sale ($)", 0.0, value=100.0, step=10.0, key="sale_current")
    gross_margin_current = st.slider("Gross Margin (%)", 0.0, 100.0, 60.0, key="gm_current")
    op_expense_current = st.number_input("Monthly Operational Expense ($)", 0.0, value=20000.0, step=500.0, key="opex_current")

with col2:
    st.subheader("🔸 Planned % Improvements")
    leads_increase = st.slider("Leads Increase (%)", 0.0, 100.0, 10.0, key="leads_inc")
    conversion_increase = st.slider("Conversion Rate Increase (%)", 0.0, 100.0, 10.0, key="conv_inc")
    transactions_increase = st.slider("Transactions Increase (%)", 0.0, 100.0, 10.0, key="trans_inc")
    avg_sale_increase = st.slider("Average Sale Increase (%)", 0.0, 100.0, 10.0, key="sale_inc")
    gross_margin_increase = st.slider("Gross Margin Increase (%)", 0.0, 100.0, 5.0, key="gm_inc")
    op_expense_reduction = st.slider("Operational Expense Reduction (%)", 0.0, 100.0, 10.0, key="opex_dec")

# Current values
customers_current = leads_current * (conversion_current / 100)
revenue_current = customers_current * transactions_current * avg_sale_current
gross_profit_current = revenue_current * (gross_margin_current / 100)
net_profit_current = gross_profit_current - op_expense_current

# Improved values
leads_new = leads_current * (1 + leads_increase / 100)
conversion_new = conversion_current * (1 + conversion_increase / 100)
transactions_new = transactions_current * (1 + transactions_increase / 100)
avg_sale_new = avg_sale_current * (1 + avg_sale_increase / 100)
gross_margin_new = gross_margin_current * (1 + gross_margin_increase / 100)
op_expense_new = op_expense_current * (1 - op_expense_reduction / 100)

customers_new = leads_new * (conversion_new / 100)
revenue_new = customers_new * transactions_new * avg_sale_new
gross_profit_new = revenue_new * (gross_margin_new / 100)
net_profit_new = gross_profit_new - op_expense_new

# % Improvements
def pct_change(new, old):
    if old == 0:
        return "N/A"
    return f"{((new - old) / old) * 100:.1f}%"

# Display results
st.markdown("## 📊 Results Comparison")
col3, col4, col5 = st.columns([1, 1, 1.2])  # Adjusted column width for alignment

with col3:
    st.markdown("### Metric")
    metrics = ["Customers", "Revenue", "Gross Profit", "Operational Expense", "Net Profit"]
    for m in metrics:
        st.markdown(f"**{m}**")

with col4:
    st.markdown("### Current")
    st.markdown(f"{customers_current:,.0f}")
    st.markdown(f"${revenue_current:,.2f}")
    st.markdown(f"${gross_profit_current:,.2f}")
    st.markdown(f"${op_expense_current:,.2f}")
    st.markdown(f"${net_profit_current:,.2f}")

with col5:
    st.markdown("### Projected (% Change)")
    st.markdown(f"{customers_new:,.0f} ({pct_change(customers_new, customers_current)})")
    st.markdown(f"${revenue_new:,.2f} ({pct_change(revenue_new, revenue_current)})")
    st.markdown(f"${gross_profit_new:,.2f} ({pct_change(gross_profit_new, gross_profit_current)})")
    st.markdown(f"${op_expense_new:,.2f} ({pct_change(op_expense_current, op_expense_new)}) ↓")
    st.markdown(f"${net_profit_new:,.2f} ({pct_change(net_profit_new, net_profit_current)})")


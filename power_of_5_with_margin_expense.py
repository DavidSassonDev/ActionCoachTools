import streamlit as st
import pandas as pd


st.title("5 Ways Tool – Leads Driver Module")

st.header("Enter Current Business Metrics")
ad_budget_current = st.number_input("Ad Budget ($/month)", value=1000)
referral_leads_current = st.number_input("Referral Leads per Month", value=200)
outreach_current = st.number_input("Outreach Campaigns (Contacts per Week)", value=100)
seo_current_enabled = st.checkbox("SEO Currently Enabled?", value=False)

st.header("Enter Planned Improvements")
ad_budget_improvement_pct = st.slider("Increase in Ad Budget (%)", 0.0, 1.0, 0.3)
referral_leads_improvement_pct = st.slider("Increase in Referral Leads (%)", 0.0, 1.0, 0.0)
outreach_improvement_pct = st.slider("Increase in Outreach Contacts (%)", 0.0, 1.0, 0.2)
seo_enabled = st.checkbox("Enable SEO?", value=True)

# Calculate improved values
ad_budget_improved = ad_budget_current * (1 + ad_budget_improvement_pct)
referral_leads_improved = referral_leads_current * (1 + referral_leads_improvement_pct)
outreach_improved = outreach_current * (1 + outreach_improvement_pct)

def calculate_leads(ad_budget, referrals, outreach, seo, lead_multiplier=1.3):
    monthly_outreach_contacts = outreach * 4
    leads_from_ads = ad_budget * lead_multiplier
    leads_from_outreach = monthly_outreach_contacts * 0.20
    total_leads = leads_from_ads + leads_from_outreach + referrals
    if seo:
        total_leads *= 1.10
    return round(total_leads, 2)

leads_current = calculate_leads(ad_budget_current, referral_leads_current, outreach_current, seo_current_enabled)
leads_improved = calculate_leads(ad_budget_improved, referral_leads_improved, outreach_improved, seo_enabled)

st.subheader("Results")
st.write(f"**Current Monthly Leads:** {leads_current}")
st.write(f"**Improved Monthly Leads:** {leads_improved}")
st.write(f"**% Increase:** {round((leads_improved - leads_current) / leads_current * 100, 2)}%" if leads_current > 0 else "N/A")

st.title("5 Ways Tool – Conversion Rate Driver Module")

st.header("Current Conversion Metrics")
sales_perf_current = st.slider("Sales Team Performance (1-10)", 1, 10, 5)
sales_script_current = st.checkbox("Sales Script in Place?", value=False)
objection_handling_current = st.slider("Objection Handling Skill (1-10)", 1, 10, 5)
follow_up_current = st.checkbox("Follow-up Automation in Place?", value=False)
trust_signals_current = st.checkbox("Trust Signals Available?", value=False)

st.header("Planned Improvements")
sales_perf_improved = st.slider("Sales Team Performance (Improved)", 1, 10, 7)
sales_script_improved = st.checkbox("Sales Script in Place? (Improved)", value=True)
objection_handling_improved = st.slider("Objection Handling (Improved)", 1, 10, 7)
follow_up_improved = st.checkbox("Follow-up Automation (Improved)", value=True)
trust_signals_improved = st.checkbox("Trust Signals Available? (Improved)", value=True)

def calc_conversion_rate(base, perf, script, objections, followup, trust):
    cr = base + perf * 1 + objections * 0.5
    if script:
        cr *= 1.10
    if followup:
        cr *= 1.05
    if trust:
        cr *= 1.05
    return round(cr, 2)

base_cr = 10.0  # 10% base
cr_current = calc_conversion_rate(base_cr, sales_perf_current, sales_script_current, objection_handling_current, follow_up_current, trust_signals_current)
cr_improved = calc_conversion_rate(base_cr, sales_perf_improved, sales_script_improved, objection_handling_improved, follow_up_improved, trust_signals_improved)

st.subheader("Results")
st.write(f"**Current Conversion Rate:** {cr_current}%")
st.write(f"**Improved Conversion Rate:** {cr_improved}%")
st.write(f"**% Improvement:** {round((cr_improved - cr_current) / cr_current * 100, 2)}%" if cr_current > 0 else "N/A")

st.title("5 Ways Tool – Transactions per Customer Module")

st.header("Current State")
email_campaigns_current = st.number_input("Email/SMS Campaigns per Month", value=2)
loyalty_program_current = st.checkbox("Loyalty Program Active?", value=False)
return_rate_current = st.slider("Returning Customer %", 0, 100, 30)
subscription_current = st.checkbox("Subscription Model Active?", value=False)

st.header("Planned Improvements")
email_campaigns_improved = st.number_input("Email/SMS Campaigns (Improved)", value=4)
loyalty_program_improved = st.checkbox("Loyalty Program Active? (Improved)", value=True)
return_rate_improved = st.slider("Returning Customer % (Improved)", 0, 100, 50)
subscription_improved = st.checkbox("Subscription Model Active? (Improved)", value=True)

def calc_transactions(base, campaigns, loyalty, return_pct, subscription):
    tx = base + (campaigns * 0.02)
    if loyalty:
        tx *= 1.10
    if subscription:
        tx *= 1.20
    tx *= (1 + return_pct / 100)
    return round(tx, 2)

base_tx = 1.0  # 1 transaction baseline
tx_current = calc_transactions(base_tx, email_campaigns_current, loyalty_program_current, return_rate_current, subscription_current)
tx_improved = calc_transactions(base_tx, email_campaigns_improved, loyalty_program_improved, return_rate_improved, subscription_improved)

st.subheader("Results")
st.write(f"**Current Transactions per Customer:** {tx_current}")
st.write(f"**Improved Transactions per Customer:** {tx_improved}")
st.write(f"**% Improvement:** {round((tx_improved - tx_current) / tx_current * 100, 2)}%" if tx_current > 0 else "N/A")

st.title("5 Ways Tool – Average Order Value (AOV) Module")

st.header("Current State")
cart_size_current = st.number_input("Average Cart Size (Items)", value=2)
premium_options_current = st.checkbox("Premium Options Offered?", value=False)
upselling_rate_current = st.slider("Upselling Rate (%)", 0, 100, 5)
bundling_current = st.checkbox("Bundling Strategy In Place?", value=False)

st.header("Planned Improvements")
cart_size_improved = st.number_input("Improved Cart Size (Items)", value=3)
premium_options_improved = st.checkbox("Premium Options Offered? (Improved)", value=True)
upselling_rate_improved = st.slider("Upselling Rate (%) (Improved)", 0, 100, 15)
bundling_improved = st.checkbox("Bundling Strategy In Place? (Improved)", value=True)

def calc_aov(base, cart_size, premium, upsell_pct, bundling):
    aov = base + (cart_size - 1) * 30  # $30 per additional item beyond base
    aov *= (1 + upsell_pct / 100)
    if premium:
        aov *= 1.15
    if bundling:
        aov *= 1.10
    return round(aov, 2)

base_aov = 100.0  # base AOV with 1 item
aov_current = calc_aov(base_aov, cart_size_current, premium_options_current, upselling_rate_current, bundling_current)
aov_improved = calc_aov(base_aov, cart_size_improved, premium_options_improved, upselling_rate_improved, bundling_improved)

st.subheader("Results")
st.write(f"**Current AOV:** ${aov_current}")
st.write(f"**Improved AOV:** ${aov_improved}")
st.write(f"**% Improvement:** {round((aov_improved - aov_current) / aov_current * 100, 2)}%" if aov_current > 0 else "N/A")

st.title("5 Ways Tool – Profit Margin Module")

st.header("Current State")
cogs_current = st.slider("COGS (% of Sales)", 0, 100, 60)
efficiency_current = st.slider("Operational Efficiency (1–10)", 1, 10, 5)
automation_current = st.checkbox("Using Automation/Software?", value=False)
overhead_current = st.number_input("Overhead Costs per Month ($)", value=5000)
pricing_review_current = st.checkbox("Pricing Strategy Reviewed?", value=False)

st.header("Planned Improvements")
cogs_improved = st.slider("COGS (% of Sales) (Improved)", 0, 100, 50)
efficiency_improved = st.slider("Operational Efficiency (Improved)", 1, 10, 8)
automation_improved = st.checkbox("Using Automation/Software? (Improved)", value=True)
overhead_improved = st.number_input("Overhead Costs ($) (Improved)", value=4000)
pricing_review_improved = st.checkbox("Pricing Strategy Reviewed? (Improved)", value=True)

def calc_margin(cogs, efficiency, automation, overhead, pricing):
    margin = 100 - cogs  # start with gross margin
    margin += efficiency * 0.5  # operational efficiency boost
    if automation:
        margin += 5
    if pricing:
        margin += 10
    margin -= overhead / 1000  # scale penalty: $1000 overhead = -1%
    return round(min(margin, 100), 2)  # cap at 100%

margin_current = calc_margin(cogs_current, efficiency_current, automation_current, overhead_current, pricing_review_current)
margin_improved = calc_margin(cogs_improved, efficiency_improved, automation_improved, overhead_improved, pricing_review_improved)

st.subheader("Results")
st.write(f"**Current Profit Margin:** {margin_current}%")
st.write(f"**Improved Profit Margin:** {margin_improved}%")
st.write(f"**% Improvement:** {round((margin_improved - margin_current) / margin_current * 100, 2)}%" if margin_current > 0 else "N/A")

st.title("💰 Final Profit Summary")

# Final Profit Calculation
def calc_total_profit(leads, cr_pct, tx, aov, margin_pct):
    return round(leads * (cr_pct / 100) * tx * aov * (margin_pct / 100), 2)

profit_current = calc_total_profit(leads_current, cr_current, tx_current, aov_current, margin_current)
profit_improved = calc_total_profit(leads_improved, cr_improved, tx_improved, aov_improved, margin_improved)

# Show Results
st.subheader("🧾 Current vs. Improved Profit")
st.write(f"**Current Monthly Profit:** ${profit_current:,.2f}")
st.write(f"**Improved Monthly Profit:** ${profit_improved:,.2f}")
st.write(f"**Total % Increase in Profit:** {round((profit_improved - profit_current) / profit_current * 100, 2)}%" if profit_current > 0 else "N/A")

# Format helper
def format_metric(metric, value):
    if "Rate" in metric or "Margin" in metric:
        return f"{value:.2f}%"
    elif "AOV" in metric or "Profit" in metric:
        return f"${value:,.2f}"
    else:
        return f"{value:,.2f}"

# Build formatted summary table
summary_data = {
    "Metric": ["Leads", "Conversion Rate (%)", "Transactions", "AOV ($)", "Profit Margin (%)", "Profit ($)"],
    "Current": [
        format_metric("Leads", leads_current),
        format_metric("Conversion Rate", cr_current),
        format_metric("Transactions", tx_current),
        format_metric("AOV", aov_current),
        format_metric("Profit Margin", margin_current),
        format_metric("Profit", profit_current),
    ],
    "Improved": [
        format_metric("Leads", leads_improved),
        format_metric("Conversion Rate", cr_improved),
        format_metric("Transactions", tx_improved),
        format_metric("AOV", aov_improved),
        format_metric("Profit Margin", margin_improved),
        format_metric("Profit", profit_improved),
    ]
}

summary_df = pd.DataFrame(summary_data)
st.dataframe(summary_df)

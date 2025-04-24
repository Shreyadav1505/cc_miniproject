#run this in terminal
#"C:\Users\shrey\AppData\Roaming\Python\Python313\Scripts\streamlit.exe" run app.py 


import streamlit as st
from eda_utils import load_data, clean_data, explore_data
from insights import show_distribution, show_correlation_heatmap, show_grouped_bar_chart

st.title("📊 Insights Explorer App")

# Upload CSV
file = st.file_uploader("E:\3rd_year_prac\CC\minipro3\data\credit_card_transactions.csv", type=["csv"])
if file:
    df = load_data(file)
    df = clean_data(df)

    st.sidebar.header("Exploration")
    if st.sidebar.checkbox("Show Raw Data"):
        st.write(df.head())

    if st.sidebar.checkbox("Basic Summary"):
        summary = explore_data(df)
        st.write(summary)

    st.header("🔍 Key Insights")

    # Insight 1
    column = st.selectbox("Select column for distribution", df.columns)
    show_distribution(df, column)

    # Insight 2
    show_correlation_heatmap(df)

    # Insight 3
    group_col = st.selectbox("Select group-by column", df.columns)
    value_col = st.selectbox("Select value column", df.columns)
    show_grouped_bar_chart(df, group_col, value_col)

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def show_distribution(df, column):
    st.subheader(f"Distribution of {column}")
    fig, ax = plt.subplots()
    df[column].hist(ax=ax, bins=30)
    st.pyplot(fig)

def show_correlation_heatmap(df):
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

def show_grouped_bar_chart(df, group_col, value_col):
    st.subheader(f"{value_col} by {group_col}")
    fig, ax = plt.subplots()
    df.groupby(group_col)[value_col].mean().plot(kind='bar', ax=ax)
    st.pyplot(fig)

import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="معاشات خالدة", layout="wide")

# Load the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv("معاشات_خالدة_final.csv")
    return df

df = load_data()

# Sidebar search by name
st.sidebar.title("🔍 البحث بالاسم")
search_term_name = st.sidebar.text_input("أدخل الاسم:")

# Filter results by name
if search_term_name:
    results = df[df["الاسم"].astype(str).str.contains(search_term_name)]
    if not results.empty:
        st.write(f"**🔍 النتائج لـ الاسم** `{search_term_name}`:")
        st.dataframe(results)
    else:
        st.warning("❌ لم يتم العثور على نتائج.")
else:
    st.write("📋 **كل السجلات:**")
    st.dataframe(df)

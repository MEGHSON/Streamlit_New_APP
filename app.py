import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
st.title("Main Title")
st.header("Section Header")
st.subheader("Subsection")
st.text("Plain text")
st.write("Flexible write function")
 
 
st.markdown("**ABCD** and *italic*")
st.markdown("- Item 1 \n - Item 2")
 
 
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Sales' : [100, 200, 300, 400],
    'Region' : ['North', 'South', 'East', 'East']  
})
 
st.dataframe(df)
st.table(df)
 
total_sales = df['Sales'].sum()
total_regions = df['Region'].nunique()
st.metric(label="Total Sales", value=total_sales, delta=-20)
 
if st.button("Show Region Details"):
    st.metric(label="Total Regions", value=total_regions)
 
age = st.slider("Select Age", 0, 100, 25)
 
st.write(f"Selected Age: {age}")
 
 
region = st.selectbox("Select Region", df['Region'].unique())
st.write(f"Selected Region: {region}")
 
 
region_ms = st.multiselect("Select Regions", df['Region'].unique(), default=df['Region'].unique()[0])
st.write(f"Selected Regions: {region_ms}")
 
if st.checkbox("Show DataFrame"):
    st.dataframe(df)
 
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")
 
 
st.write( {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Sales' : [100, 200, 300, 400],
    'Region' : ['North', 'South', 'East', 'East']  
})
 
 
fig,ax = plt.subplots()
sns.barplot(x='Name', y='Sales', data=df, ax=ax)
st.pyplot(fig)
 
st.write(fig)
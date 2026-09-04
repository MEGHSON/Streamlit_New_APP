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
st.markdown("- Item 1 \n - Item 2 \n - trree")

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Sales' : [100, 200, 300, 400],
    'Region' : ['North', 'South', 'East', 'East']  
})

# dataframe is interactive
st.dataframe(df)

# table is not interactive ; static 
st.table(df)

total_regions = df["Region"].nunique()
# total_regions = df["Region"].unique()
total_sales = df["Sales"].sum()
# st.metric(label="Sales",value=200, delta=250)
st.metric(label="Sales", value=total_sales, delta=20)

# if st.button("Click Me"):
#     st.write("Button Clicked")

if st.button("Click to see Metric:"):
    st.metric(label="Total Regions", value=total_regions)

age = st.slider("Select Age", 0 , 100, 25)

st.write(f"Selected age is: {age}")

st.write("Now the new line is going to look like the following:")

# city = st.selectbox("Select City:",["New York", "California","L.A."])
# st.write(f"The selected city is: {city}")

region = st.selectbox("Select Region:",df["Region"].unique())
st.write(f"The selected region is: {region}")

names = st.selectbox("Select the Names: ", df["Name"].unique())
st.write(f"The new name is {names}")

names_multiselect = st.multiselect("Select the Names: ", df["Name"].unique(), default= df["Name"].unique()[0])
st.write(f"The new names are as follows {names_multiselect}")

if st.checkbox("Show DataFrame"):
    st.dataframe(df)

name1 = st.text_input("Write your name: ")
st.write(f"Hello {name1}")

fig,ax = plt.subplots()
sns.barplot(x='Name', y='Sales', data=df, ax=ax)
st.pyplot(fig)
st.write(fig)
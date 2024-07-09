import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

title = st.title("In Search for Happiness")

x = st.selectbox("Select the data for the X-axis",
                 ("GDP","Life Expectancy",
                              "Happiness","Generosity"))
y = st.selectbox("Select the data for the Y-axis",
                ("GDP","Life Expectancy",
                              "Happiness","Corruption"))
Name = st.subheader(f"{x} against {y} graph" )

match x:
        case  "GDP":
            value = df["gdp"]
        case "Life Expectancy":
            value = df["life_expectancy"]
        case  "Happiness":
            value == df["happiness"]
        case "Generosity":
            value == df["generosity"]

match y:
        case  "GDP":
            value1 = df["gdp"]
        case "Life Expectancy":
            value1= df["life_expectancy"]
        case  "Happiness":
            value1 = df["happiness"]
        case "Corruption":
            value1 = df["corruption"]


figure = px.scatter(x=value,y=value1,labels={"x":f"{x}","y":f"{y}"})

st.plotly_chart(figure)
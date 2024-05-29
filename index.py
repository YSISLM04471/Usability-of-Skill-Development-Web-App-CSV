import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    st.title("Usability Skill Development Web Application")
    
    # Load CSV file directly
    @st.cache_data
    def load_data():
        return pd.read_csv("hcI.csv")  # Change "your_file.csv" to your actual file name
    
    df = load_data()
    
    # Display the dataframe
    st.write("### Data from CSV file:")
    st.dataframe(df, width=2000)  # Adjust the width as needed
    
    # Generate bar plot for a selected column
    selected_column_bar = st.selectbox("Select a column for bar plot:", df.columns[1:])
    bar_fig = px.bar(df, x=df[selected_column_bar].value_counts().index, y=df[selected_column_bar].value_counts().values)
    st.write("### Bar Plot:")
    st.plotly_chart(bar_fig)
    
    # Generate curve plot for a selected column
    selected_curve_column = st.selectbox("Select a column for curve plot:", df.columns[1:])
    curve_fig = px.line(df, x=df.index, y=selected_curve_column)
    st.write("### Curve Plot:")
    st.plotly_chart(curve_fig)
    
    # Generate pie chart for a selected column
    selected_column_pie = st.selectbox("Select a column for pie chart:", df.columns[1:])
    pie_fig = px.pie(df, values=df[selected_column_pie].value_counts().values, names=df[selected_column_pie].value_counts().index)
    st.write("### Pie Chart:")
    st.plotly_chart(pie_fig)
        
if __name__ == "__main__":
    main()

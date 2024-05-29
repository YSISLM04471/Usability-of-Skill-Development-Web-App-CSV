import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    
    # Generate scatter plot for two selected columns with interactive features
    st.write("### Scatter Plot (with interactivity):")
    selected_x_column = st.selectbox("Select X-axis column:", df.columns[1:])
    selected_y_column = st.selectbox("Select Y-axis column:", df.columns[1:])
    scatter_fig = px.scatter(df, x=selected_x_column, y=selected_y_column, color=df.columns[0], hover_name=df.columns[0])
    scatter_fig.update_layout(title=f"Scatter Plot: {selected_x_column} vs {selected_y_column}",
                              xaxis_title=selected_x_column,
                              yaxis_title=selected_y_column)
    st.plotly_chart(scatter_fig)
   

if __name__ == "__main__":
    main()

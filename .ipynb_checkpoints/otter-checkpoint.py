import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('train.csv')

# Set the page title and icon
st.set_page_config(
    page_title="Churn Analysis Dashboard",
    page_icon="📈",
)

# Define the sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Data Exploration", "Model Analysis", "Code Editor", "About Me"])

# Define code editor placeholder
code = st.sidebar.text_area("Code Editor", value="", height=300)

# Main content based on the selected page
if page == "Overview":
    st.title("Churn Analysis Dashboard")

    st.write("Welcome to the Churn Analysis Dashboard. Use the sidebar to navigate between sections.")

elif page == "Data Exploration":
    st.title("Data Exploration")

    # Display the dataset
    st.write("### Raw Data")
    st.write(data)

    # Summary statistics
    st.write("### Summary Statistics")
    st.write(data.describe())

    # Data visualization
    st.write("### Data Visualization")

    # Example: Histogram of total_day_minutes using Plotly
    st.subheader("Histogram of Total Day Minutes")
    fig_histogram = px.histogram(data, x='total_day_minutes', nbins=30, title='Total Day Minutes Distribution')
    st.plotly_chart(fig_histogram)

    # Example: Count plot of churn using Plotly
    st.subheader("Count of Churn")
    churn_counts = data['churn'].value_counts().reset_index()
    churn_counts.columns = ['Churn', 'Count']
    fig_countplot = px.bar(churn_counts, x='Churn', y='Count', title='Churn Count')
    st.plotly_chart(fig_countplot)

    # Advanced Graph: Scatter Plot Matrix using Plotly Express
    st.subheader("Scatter Plot Matrix")
    fig_scatter_matrix = px.scatter_matrix(
        data,
        dimensions=['total_day_minutes', 'total_eve_minutes', 'total_night_minutes', 'total_intl_minutes'],
        title='Scatter Plot Matrix',
    )
    st.plotly_chart(fig_scatter_matrix)

    # Advanced Graph: Correlation Heatmap using Plotly
    st.subheader("Correlation Heatmap")
    correlation_matrix = data[['total_day_minutes', 'total_eve_minutes', 'total_night_minutes', 'total_intl_minutes']].corr()
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.index,
        colorscale='Viridis',
        zmin=-1, zmax=1,
        hoverongaps=False,
    ))
    st.plotly_chart(fig_heatmap)

    # Insights in Markdown
    st.write("### Insights")
    st.markdown("""
    - The scatter plot matrix shows relationships between different call minutes features. 
    - In the correlation heatmap, we observe that 'total_day_minutes' has a positive correlation with 'total_eve_minutes' and 'total_intl_minutes'.
    - Conversely, 'total_day_minutes' has a negative correlation with 'total_night_minutes'.
    """)

elif page == "Model Analysis":
    st.title("Model Analysis")

    # Build and evaluate machine learning models (you can add your model code here)

    # Display model performance metrics and visualizations using Plotly

elif page == "Code Editor":
    st.title("Code Editor")

    # Run code using the "Run Code" button
    if st.button("Run Code"):
        with st.spinner("Running code..."):
            try:
                # Execute the code and display results
                exec(code)
            except Exception as e:
                st.error(f"An error occurred: {e}")

elif page == "About Me":
    st.title("About Me")

    # Include links to GitHub and LinkedIn
    st.write("### Connect with Me")
    st.write("[GitHub](https://github.com/)")
    st.write("[LinkedIn](https://www.linkedin.com/in/amitha-s983)")

    st.markdown("[Download Resume PDF](https://drive.google.com/file/d/1yS3Igfnp1U9cQOvU60Pi5vWhGcsKMsh_/view?usp=sharing)")
    # Showcase your resume (assuming the resume.pdf file is in the same directory)

# Add additional sections and functionalities as needed

# Footer
st.sidebar.markdown("---")
st.sidebar.text("© 2023 Otter")


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import os

import sys
from io import StringIO



# Set the page title and icon
st.set_page_config(
    page_title="Amitha Portfolio",
    page_icon="📈",
)

# Define the sidebar
st.sidebar.header("Menu")
page = st.sidebar.radio("Go to", ["Overview","Code Editor", "Projects", "Apply for Jobs"])

# Define code editor placeholder


# Main content based on the selected page
if page == "Overview":
    st.title("Overview")

    st.markdown("""
    # AMITHA S
    +91 9538692183 | amithasuri98@gmail.com | Bangalore, KA | [LinkedIn Profile](www.linkedin.com/in/amitha-s983)
    
    ## Summary
    A Business Analyst with 3 years of experience across the BFSI and Retail industry, gaining insights into driving successful
    business solutions through data-driven decisions and committed to delivering results that align with business objectives.
    
    ## Professional Experience
    
    ### Business Analyst | Impact Analytics
    Jan 2023 – Present
    - **Dashboard Development and Reporting**: Spearheaded the development of dynamic and interactive dashboards leveraging Datastudio. These dashboards not only elevated reporting capabilities but also contributed to a remarkable 60% surge in user engagement. By enabling real-time data-driven decision-making, they became instrumental in steering strategic initiatives.
    - **Stakeholder Engagement and Requirement Elicitation**: Functioned as the primary interface between multifaceted teams, including product, analytics, and marketing. Proficiently translated client requisites for new feature integration and market expansion strategies. The adept alignment of business objectives with data insights propelled project success.
    - **Agile and SDLC Integration**: Pioneered the integration of Agile methodologies with Software Development Life Cycle (SDLC) practices. This fusion delivered a marked boost in project flexibility, fostering seamless collaboration among stakeholders, and ensuring on-time, on-budget project deliveries.
    - **Advanced Data Analysis**: Applied advanced data analysis techniques to extract actionable insights from intricate datasets. This data-driven approach led to the creation of visually compelling presentation decks, effectively conveying complex insights to discerning clients.
    - **Business Requirement Documentation**: Collaborated closely with stakeholders to meticulously document business requirements. Created comprehensive Business Requirement Documents (BRDs) and precise use cases, aligning project objectives with stakeholder expectations seamlessly.
    
    ### Data Analyst | American Banking and Financial Services Company (Tata Consultancy Services)
    - **Leveraged Data-Driven Business Insights**: Proficiently harnessed a suite of data analysis tools and techniques to extract valuable insights from extensive datasets. Transformed these insights into actionable recommendations, driving significant enhancements in business performance. This data-centric approach paved the way for informed decision-making.
    - **User Acceptance Testing (UAT)**: Spearheaded user acceptance testing (UAT) initiatives to meticulously evaluate product quality and functionality. Ensured that the product aligned with business requirements, fostering reliability and customer satisfaction.
    - **Operational Efficiency Improvement**: Strategically analyzed data to identify process inefficiencies. Collaborated closely with cross-functional teams to implement targeted improvements, resulting in substantial enhancements in operational efficiency and a notable reduction in operational costs. Employed root cause analysis to tackle recurring issues systematically.
    - **Master Data Analysis**: Leveraged advanced SQL and Excel expertise to conduct in-depth master data analysis. Effectively translated complex data insights into meaningful narratives for key stakeholders. This data-driven communication facilitated well-informed strategic decisions.
    
    ### Developer (Tata Consultancy Services)
    Nov 2020 – Jan 2023
    
    ### Middleware developer | American Banking and Financial Services Company
    - **Strategic Process Automation**: Pioneered an in-depth analysis and successful implementation of an internal project aimed at automating a mission-critical repository process. This transformative initiative resulted in a remarkable 70% reduction in labor hours, translating into substantial cost savings and heightened operational efficiency.
    - **Cross-functional collaboration**: Chaired and actively contributed to over 15 internal and third-party service review meetings, encompassing in-depth assessments of performance metrics, process improvements, and workflow refinements. By fostering cross-functional collaboration, fostered synergies across teams, resulting in streamlined processes and enhanced service quality.
    - **Data-Driven Decision Support**: Collaborated closely with business units, aligning technology solutions with strategic objectives. Leveraged cutting-edge middleware technologies, including Service-Oriented Architecture (SOA), APIs, Microservices, and IBM DataPower tools, to enable robust data integration and analysis capabilities. This empowered stakeholders to make informed, data-driven decisions, enhancing competitiveness and agility in a dynamic industry landscape.
    
    ## Education
    Global Academy of Technology, Bangalore, India
    - Engineering| Computer Science | CGPA: 7.53
    - 2016-2020
    
    ## Skills
    - Programming Languages: Basics in Python, XML, JSON, Web Services, Basics of R
    - Data Visualization: Excel, Power BI, PowerPoint, Matplotlib
    - Databases: MySQL, Google Big Query, PostgreSQL
    - Basics of AWS and Data Structures
    - Tools: Jira, Rally, Confluence, PowerPoint, Eclipse, Google Data Studio, Tableau and Jupyter
    
    ## Accomplishments
    - Certified Business Analyst by IIBA-endorsed course on LinkedIn Learning.
    - Completed courses related to Business Intelligence, Agile methodologies, and SDLC.
    - Conducted a 3-day workshop about Business Analysis at Dayanand Sagar College of Engineering.
    - Collaborated with C-level suite and key stakeholders to improve methodologies and operations for employee budgeting and resource management within the organization.
    - Completed courses on Blockchain and worked on a technical paper regarding Blockchain implementation over cloud technology.
    - Been an active part of the college Cultural team.
    """)
    

    st.write("### Connect with Me")
    st.write("[GitHub](https://github.com/)")
    st.write("[LinkedIn](https://www.linkedin.com/in/amitha-s983)")

    st.markdown("[Download Resume PDF](https://drive.google.com/file/d/1yS3Igfnp1U9cQOvU60Pi5vWhGcsKMsh_/view?usp=sharing)")
    







                
                



elif page == "Projects":
    st.title("Projects")

    # Define the main projects directory path
    projects_dir = "./projects/"

    # List all subdirectories (projects) within the projects directory
    project_names = [project for project in os.listdir(projects_dir) if os.path.isdir(os.path.join(projects_dir, project))]

    # Create a project selection dropdown
    selected_project = st.selectbox("Select a Project", project_names)

    # Define the folder path for the selected project
    project_folder_path = os.path.join(projects_dir, selected_project)

    # Define the names of the Markdown files
    markdown_files = ["requirements.md", "step1.md", "step2.md"]

    # Display the selected project's Markdown content
    for markdown_file in markdown_files:
        file_path = os.path.join(project_folder_path, markdown_file)

        # Display each Markdown file under a corresponding header
        st.markdown(f"### {markdown_file[:-3].capitalize()}")

        # Read and display Markdown content from the file
        with open(file_path, 'r', encoding='utf-8') as markdown_file_content:
            markdown_text = markdown_file_content.read()
            st.markdown(markdown_text)
            


elif page == "Code Editor":
    st.title("Code Editor")

    # Code editor input
    code = st.text_area("Enter Python code", value="", height=300)

    # Run code using the "Run Code" button
    if st.button("Run Code"):
        with st.spinner("Running code..."):
            try:
                # Capture the standard output (stdout)
                original_stdout = sys.stdout
                sys.stdout = StringIO()

                # Execute the code
                exec(code, globals(), locals())

                # Get the captured stdout content
                code_output = sys.stdout.getvalue()

                # Restore the original stdout
                sys.stdout = original_stdout

                # Display the code output
                st.write("### Code Output")
                st.code(code_output, language="python")  # Display code output using st.code()
                st.success("Code executed successfully.")
            except Exception as e:
                # Display any error messages
                st.error(f"An error occurred: {e}")
                
                
elif page == "Apply for Jobs":
    st.title("Apply for Jobs")

    
    job_links= {"Trinity Life Sciences": "https://www.linkedin.com/jobs/view/3756323371", "Citibank": "https://www.linkedin.com/jobs/view/3725424645"}
    

  
    
    # Display added job links
    if job_links:
        st.write("### LinkedIn Job Links:")
        for company,link in job_links.items():
            st.write(company)
            st.markdown(f"- [{link}]({link})")

	




# Add additional sections and functionalities as needed

# Footer
st.sidebar.markdown("---")
st.sidebar.text("© 2023 Amitha S")


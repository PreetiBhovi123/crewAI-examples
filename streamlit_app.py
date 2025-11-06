import streamlit as st
from crewai import Agent, Task, Crew

st.title("💼 AI Job Posting Generator")

# Create a simple agent
agent = Agent(
    name="JobPostingAgent",
    role="Job Description Writer",
    goal="Create professional job postings based on user input",
)

job_title = st.text_input("Enter Job Title:")
skills = st.text_area("Required Skills:")
company = st.text_input("Company Name:")

if st.button("Generate Job Description"):
    if job_title and skills and company:
        task = Task(
            description=f"Write a professional job posting for {job_title} at {company}. "
                        f"Required skills: {skills}",
            expected_output="A detailed and attractive job posting."
        )

        crew = Crew(agents=[agent], tasks=[task])
        result = crew.run()
        st.subheader("📝 Generated Job Description:")
        st.write(result)
    else:
        st.warning("Please fill all fields before generating.")

import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define tools
search_tool = SerperDevTool()

# Define agents
blog_writer = Agent(
    role='Tech Blog Writer',
    goal='Write engaging tech blog posts on given topics',
    backstory='You are an expert tech writer with years of experience in creating content for tech audiences.',
    tools=[search_tool],
    verbose=True
)

linkedin_poster = Agent(
    role='LinkedIn Poster',
    goal='Post the generated blog content to LinkedIn newsletter',
    backstory='You handle social media posting, ensuring content is formatted correctly for LinkedIn.',
    verbose=True
)

# Define tasks
write_blog_task = Task(
    description='Write a blog post on the topic: {topic}',
    expected_output='A full blog post in markdown format',
    agent=blog_writer
)

post_to_linkedin_task = Task(
    description='Post the blog post to LinkedIn newsletter',
    expected_output='Confirmation of successful posting',
    agent=linkedin_poster,
    context=[write_blog_task]
)

# Create crew
crew = Crew(
    agents=[blog_writer, linkedin_poster],
    tasks=[write_blog_task, post_to_linkedin_task],
    verbose=True
)

if __name__ == "__main__":
    # Example run
    result = crew.kickoff(inputs={'topic': 'Latest Trends in AI'})
    print(result)

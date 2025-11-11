import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from linkedin_tool import LinkedInPostTool

# Load environment variables
load_dotenv()

# Define tools
search_tool = SerperDevTool()
linkedin_tool = LinkedInPostTool()

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
    tools=[linkedin_tool],
    verbose=True
)

# Define tasks
write_blog_task = Task(
    description='Research and write a comprehensive blog post on the topic: {topic}. Use the search tool to gather the latest information and insights. The blog post should be well-structured with an introduction, main content sections, and a conclusion.',
    expected_output='A full blog post in markdown format with proper headings, paragraphs, and formatting',
    agent=blog_writer
)

post_to_linkedin_task = Task(
    description='Post the blog post to LinkedIn. Extract the title from the blog post (use the first heading or create a compelling title based on the content). Use the LinkedIn Newsletter Poster tool to publish the content.',
    expected_output='Confirmation message with the LinkedIn post ID indicating successful posting',
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

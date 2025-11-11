# Usage Guide for ALOG Agentic Blog Writer

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**
   
   Copy the example environment file and add your API keys:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add:
   - `OPENAI_API_KEY`: Your OpenAI API key for the AI agents
   - `SERPER_API_KEY`: Your Serper API key for web searches (get one at https://serper.dev)
   - `LINKEDIN_ACCESS_TOKEN`: Your LinkedIn access token for posting

   ### Getting LinkedIn Access Token
   
   To post to LinkedIn, you need to:
   1. Create a LinkedIn App at https://www.linkedin.com/developers/apps
   2. Request the following permissions:
      - `w_member_social` (to post on behalf of a user)
      - `r_liteprofile` or `r_basicprofile` (to get user info)
   3. Use OAuth 2.0 flow to get an access token
   4. Add the token to your `.env` file

## Running the Blog Writer

### Basic Usage

Run the script with the default topic (Latest Trends in AI):
```bash
python main.py
```

### Custom Topic

To write about a different topic, modify the `main.py` file:

```python
if __name__ == "__main__":
    result = crew.kickoff(inputs={'topic': 'Your Custom Topic Here'})
    print(result)
```

Or create a new script that imports the crew:

```python
from main import crew

# Write about quantum computing
result = crew.kickoff(inputs={'topic': 'Quantum Computing Breakthroughs'})
print(result)
```

## How It Works

The system uses CrewAI framework with two AI agents:

1. **Blog Writer Agent**
   - Researches the topic using the Serper search tool
   - Generates a comprehensive blog post
   - Outputs markdown-formatted content

2. **LinkedIn Poster Agent**
   - Takes the blog post from the writer
   - Extracts or creates a title
   - Posts to LinkedIn via the API

## Example Output

When you run the script, you'll see:
1. The Blog Writer agent researching the topic
2. Generation of the blog post content
3. The LinkedIn Poster agent preparing to post
4. Confirmation of successful posting with a post ID

## Troubleshooting

### "OPENAI_API_KEY is required"
- Make sure you've created a `.env` file
- Verify your OpenAI API key is correctly set

### "LINKEDIN_ACCESS_TOKEN not found"
- Check that your `.env` file includes the LinkedIn access token
- Ensure the token hasn't expired (LinkedIn tokens typically expire after 60 days)

### "Failed to post to LinkedIn"
- Verify your LinkedIn app has the correct permissions
- Check that your access token is still valid
- Review the error message for specific API issues

## Customization

### Change the AI Model

By default, CrewAI uses OpenAI's GPT-4. To use a different model, modify the agent definitions in `main.py`:

```python
from crewai import LLM

custom_llm = LLM(model="gpt-3.5-turbo")

blog_writer = Agent(
    role='Tech Blog Writer',
    goal='Write engaging tech blog posts on given topics',
    backstory='...',
    tools=[search_tool],
    llm=custom_llm,
    verbose=True
)
```

### Add More Platforms

To add support for other platforms (Twitter, Medium, etc.):

1. Create a new tool file (e.g., `twitter_tool.py`)
2. Implement the posting logic similar to `linkedin_tool.py`
3. Create a new agent and task for that platform
4. Add them to the crew

## Best Practices

- **API Rate Limits**: Be mindful of API rate limits for LinkedIn and OpenAI
- **Content Review**: Always review generated content before posting
- **Testing**: Test with a sandbox LinkedIn account first
- **Token Management**: Refresh LinkedIn tokens before they expire
- **Error Handling**: Check return messages for any errors

## Advanced Features

### Scheduling Posts

To schedule posts, you can use cron jobs or task schedulers:

```bash
# Run daily at 9 AM
0 9 * * * cd /path/to/ALOG-agentic-blog-writer && python main.py
```

### Multiple Topics

Create a script to process multiple topics:

```python
from main import crew

topics = [
    'AI in Healthcare',
    'Cloud Computing Trends',
    'Cybersecurity Best Practices'
]

for topic in topics:
    print(f"Processing: {topic}")
    result = crew.kickoff(inputs={'topic': topic})
    print(f"Result: {result}\n")
```

### Content Customization

Modify the task descriptions in `main.py` to change how content is generated:

```python
write_blog_task = Task(
    description='''Write a blog post on: {topic}
    
    Requirements:
    - Include real-world examples
    - Add statistics and data
    - Keep it under 1000 words
    - Use a professional but approachable tone
    ''',
    expected_output='A blog post meeting the above requirements',
    agent=blog_writer
)
```

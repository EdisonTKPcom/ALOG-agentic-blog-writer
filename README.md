# ALOG Agentic Blog Writer

## Overview

ALOG is an Agentic AI-powered system designed to automate the creation and posting of tech blog content. It leverages advanced AI to generate high-quality blog posts and currently focuses on publishing to LinkedIn newsletters. The project is built with scalability in mind, allowing for future expansion to other social media platforms and content distribution channels.

Built using the CrewAI framework, which enables the creation of collaborative AI agents to handle content generation and posting tasks.

## Features

- **Automated Blog Writing**: Utilizes agentic AI to create engaging tech blog content
- **LinkedIn Integration**: Seamlessly posts generated content to LinkedIn newsletters
- **Scalable Architecture**: Designed to easily add support for additional platforms
- **AI-Powered Content Generation**: Leverages cutting-edge AI models for content creation

## Current Status

- ✅ LinkedIn newsletter posting
- 🚧 Expansion to other platforms (planned)

## Getting Started

### Prerequisites

- Python 3.8+
- CrewAI framework
- LinkedIn API access (for posting)
- AI model API keys (e.g., OpenAI, Anthropic)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EdisonTKPcom/ALOG-agentic-blog-writer.git
   cd ALOG-agentic-blog-writer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and settings
   # Required: OPENAI_API_KEY, LINKEDIN_ACCESS_TOKEN, etc.
   ```

### Usage

1. Configure your content topics and posting schedule in the code (e.g., modify the `inputs` in `main.py`).
2. Run the agent:
   ```bash
   python main.py
   ```
   This will execute the CrewAI crew, generating a blog post on the specified topic and attempting to post it to LinkedIn.

## Architecture

The system is built using the CrewAI framework and consists of:

- **AI Agents**:
  - **Blog Writer Agent**: Generates engaging tech blog content using AI models and research tools.
  - **LinkedIn Poster Agent**: Handles posting the generated content to LinkedIn newsletters.
- **Tasks**:
  - Content generation task
  - Posting task
- **Tools**: Integrated tools like search engines for research and API integrations for posting.
- **Scheduling and Automation Engine**: Manages the workflow and timing of posts.
- **Content Quality Assurance Pipeline**: Ensures the generated content meets quality standards.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Roadmap

- [ ] Add support for Twitter/X
- [ ] Add support for Medium
- [ ] Add support for Dev.to
- [ ] Implement content scheduling dashboard
- [ ] Add analytics and performance tracking
"""
LinkedIn Posting Tool for CrewAI
This tool handles posting blog content to LinkedIn as a newsletter article.
"""
import os
import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class LinkedInPostInput(BaseModel):
    """Input schema for LinkedIn posting."""
    content: str = Field(..., description="The blog post content to be posted to LinkedIn")
    title: str = Field(default="Tech Blog Post", description="The title of the blog post")


class LinkedInPostTool(BaseTool):
    name: str = "LinkedIn Newsletter Poster"
    description: str = "Posts blog content to LinkedIn as a newsletter article or post. Provide the blog content and optional title."
    args_schema: Type[BaseModel] = LinkedInPostInput
    
    def _run(self, content: str, title: str = "Tech Blog Post") -> str:
        """
        Post content to LinkedIn.
        
        Args:
            content: The blog post content
            title: The title of the post (optional)
            
        Returns:
            str: Success or error message
        """
        access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        
        if not access_token:
            return "Error: LINKEDIN_ACCESS_TOKEN not found in environment variables. Please configure your .env file."
        
        # Get user profile ID first
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0'
        }
        
        try:
            # Get user profile
            profile_response = requests.get(
                'https://api.linkedin.com/v2/userinfo',
                headers=headers
            )
            
            if profile_response.status_code != 200:
                return f"Error: Failed to get LinkedIn profile. Status code: {profile_response.status_code}. Response: {profile_response.text}"
            
            profile_data = profile_response.json()
            user_id = profile_data.get('sub')
            
            if not user_id:
                return "Error: Could not retrieve user ID from LinkedIn profile"
            
            # Format the post content
            post_text = f"{title}\n\n{content}"
            
            # Prepare the post data
            post_data = {
                "author": f"urn:li:person:{user_id}",
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": post_text
                        },
                        "shareMediaCategory": "ARTICLE"
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }
            
            # Post to LinkedIn
            post_response = requests.post(
                'https://api.linkedin.com/v2/ugcPosts',
                headers=headers,
                json=post_data
            )
            
            if post_response.status_code in [200, 201]:
                post_id = post_response.json().get('id', 'unknown')
                return f"Success! Blog post has been published to LinkedIn. Post ID: {post_id}"
            else:
                return f"Error: Failed to post to LinkedIn. Status code: {post_response.status_code}. Response: {post_response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"Error: Network error occurred while posting to LinkedIn: {str(e)}"
        except Exception as e:
            return f"Error: Unexpected error occurred: {str(e)}"

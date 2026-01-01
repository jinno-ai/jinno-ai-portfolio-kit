#!/usr/bin/env python3
"""
Create GitHub repository for portfolio kit and push code
"""
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

# Get token from environment
token = os.getenv("GITHUB_TOKEN")
if not token:
    print("❌ Error: GITHUB_TOKEN not found")
    exit(1)

# Initialize GitHub client
g = Github(token)
user = g.get_user()

print(f"✅ Authenticated as: {user.login}")

# Repository details
repo_name = "jinno-ai-portfolio-kit"
description = "Complete automated setup kit for creating an impressive AI Engineer GitHub portfolio in 10 minutes"

try:
    # Check if repository exists
    try:
        repo = user.get_repo(repo_name)
        print(f"✅ Repository '{repo_name}' already exists")
        print(f"📍 URL: {repo.html_url}")
    except:
        # Create repository
        repo = user.create_repo(
            name=repo_name,
            description=description,
            private=False,
            auto_init=False,
            has_issues=True,
            has_projects=False,
            has_wiki=False
        )
        print(f"✅ Repository created: {repo.html_url}")
    
    # Add topics
    topics = [
        "portfolio", "github", "automation", "ai-engineer", 
        "python", "setup-kit", "career", "github-profile",
        "readme", "template"
    ]
    repo.replace_topics(topics)
    print(f"✅ Topics added: {', '.join(topics)}")
    
    print(f"\n🎉 Success!")
    print(f"📍 Repository URL: {repo.html_url}")
    print(f"🔗 Clone URL: {repo.clone_url}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)


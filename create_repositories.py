#!/usr/bin/env python3
"""
GitHub Repository Auto-Creation Script for jinno-ai Portfolio

This script automatically creates all necessary repositories for your GitHub portfolio.

Requirements:
    pip install PyGithub python-dotenv

Setup:
    1. Create a Personal Access Token: https://github.com/settings/tokens
       - Click "Generate new token (classic)"
       - Select scopes: repo, workflow, write:packages
    2. Create a .env file with: GITHUB_TOKEN=your_token_here
    3. Run: python create_repositories.py

Author: AI Assistant for jinno-ai
"""

import os
import sys
from github import Github, GithubException
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Repository configurations
REPOSITORIES = [
    {
        "name": "jinno-ai",  # Special profile README repository
        "description": "My GitHub Profile",
        "readme_file": "jinno-ai-profile-README.md",
        "is_profile": True,
        "topics": ["profile", "readme", "portfolio"]
    },
    {
        "name": "enterprise-rag-system",
        "description": "Production-grade RAG pipeline for enterprise knowledge bases",
        "readme_file": "enterprise-rag-system-README.md",
        "additional_files": {
            "requirements.txt": "requirements.txt",
            "docker-compose.yml": "docker-compose.yml",
            ".env.example": ".env.example",
            ".gitignore": ".gitignore"
        },
        "topics": ["rag", "llm", "langchain", "vector-database", "ai", "machine-learning", "enterprise"]
    },
    {
        "name": "llm-agent-framework",
        "description": "Multi-agent orchestration system for complex task automation",
        "readme_file": "llm-agent-framework-README.md",
        "topics": ["llm", "agents", "langgraph", "automation", "ai", "multi-agent", "orchestration"]
    },
    {
        "name": "realtime-edge-detection",
        "description": "Low-latency object detection optimized for edge devices",
        "topics": ["computer-vision", "yolo", "edge-ai", "object-detection", "tensorrt", "real-time"]
    },
    {
        "name": "multilingual-sentiment-analyzer",
        "description": "Cross-lingual sentiment analysis with fine-tuned transformers",
        "topics": ["nlp", "sentiment-analysis", "transformers", "multilingual", "huggingface"]
    },
    {
        "name": "micro-instruction-engineering",
        "description": "Systematic methodology for prompt optimization & AI reasoning",
        "topics": ["prompt-engineering", "llm", "ai", "optimization", "research"]
    }
]


def create_repository(g, username, repo_config):
    """Create a single repository with configuration."""
    repo_name = repo_config["name"]
    
    print(f"\n{'='*60}")
    print(f"Creating repository: {repo_name}")
    print(f"{'='*60}")
    
    try:
        # Check if repository already exists
        try:
            user = g.get_user()
            existing_repo = user.get_repo(repo_name)
            print(f"⚠️  Repository '{repo_name}' already exists!")
            response = input(f"   Do you want to update it? (y/n): ").lower()
            if response != 'y':
                print(f"   Skipping {repo_name}")
                return existing_repo
            repo = existing_repo
        except GithubException as e:
            if e.status == 404:
                # Repository doesn't exist, create it
                user = g.get_user()
                
                # Create repository
                repo = user.create_repo(
                    name=repo_name,
                    description=repo_config["description"],
                    private=False,
                    auto_init=True,  # Initialize with README
                    has_issues=True,
                    has_projects=True,
                    has_wiki=False
                )
                print(f"✅ Repository created: https://github.com/{username}/{repo_name}")
                time.sleep(2)  # Wait for GitHub to initialize
            else:
                raise
        
        # Add topics
        if "topics" in repo_config:
            repo.replace_topics(repo_config["topics"])
            print(f"✅ Topics added: {', '.join(repo_config['topics'])}")
        
        # Update README if specified
        if "readme_file" in repo_config:
            readme_path = repo_config["readme_file"]
            if os.path.exists(readme_path):
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                try:
                    # Get existing README to update it
                    readme = repo.get_contents("README.md")
                    repo.update_file(
                        path="README.md",
                        message="Update README with portfolio content",
                        content=content,
                        sha=readme.sha
                    )
                    print(f"✅ README.md updated from {readme_path}")
                except GithubException as e:
                    if e.status == 404:
                        # Create new README
                        repo.create_file(
                            path="README.md",
                            message="Add README with portfolio content",
                            content=content
                        )
                        print(f"✅ README.md created from {readme_path}")
            else:
                print(f"⚠️  README file not found: {readme_path}")
        
        # Add additional files
        if "additional_files" in repo_config:
            for target_path, source_file in repo_config["additional_files"].items():
                if os.path.exists(source_file):
                    with open(source_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    try:
                        # Check if file exists
                        existing_file = repo.get_contents(target_path)
                        repo.update_file(
                            path=target_path,
                            message=f"Update {target_path}",
                            content=content,
                            sha=existing_file.sha
                        )
                        print(f"✅ {target_path} updated")
                    except GithubException as e:
                        if e.status == 404:
                            # Create new file
                            repo.create_file(
                                path=target_path,
                                message=f"Add {target_path}",
                                content=content
                            )
                            print(f"✅ {target_path} created")
                    
                    time.sleep(1)  # Rate limiting
                else:
                    print(f"⚠️  File not found: {source_file}")
        
        # Add LICENSE
        try:
            repo.get_contents("LICENSE")
        except GithubException as e:
            if e.status == 404:
                mit_license = """MIT License

Copyright (c) 2026 Jinno AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
                
                repo.create_file(
                    path="LICENSE",
                    message="Add MIT License",
                    content=mit_license
                )
                print(f"✅ LICENSE added")
        
        print(f"\n🎉 Repository '{repo_name}' setup complete!")
        print(f"   URL: https://github.com/{username}/{repo_name}")
        
        return repo
        
    except GithubException as e:
        print(f"❌ Error creating repository '{repo_name}': {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def main():
    """Main function to create all repositories."""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║  GitHub Portfolio Repository Creator for jinno-ai            ║
    ║  Automated setup for AI Engineer Portfolio                   ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Check for GitHub token
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("❌ Error: GITHUB_TOKEN not found in environment variables")
        print("\nPlease follow these steps:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select scopes: repo, workflow, write:packages")
        print("4. Create a .env file with: GITHUB_TOKEN=your_token_here")
        sys.exit(1)
    
    # Initialize GitHub client
    try:
        g = Github(github_token)
        user = g.get_user()
        username = user.login
        print(f"✅ Authenticated as: {username}")
        print(f"📧 Email: {user.email or 'Not public'}")
        print(f"👥 Followers: {user.followers}")
        print(f"📦 Public repos: {user.public_repos}")
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        sys.exit(1)
    
    # Confirm before proceeding
    print(f"\n📋 Ready to create {len(REPOSITORIES)} repositories:")
    for repo in REPOSITORIES:
        print(f"   - {repo['name']}")
    
    response = input("\n🤔 Do you want to proceed? (y/n): ").lower()
    if response != 'y':
        print("❌ Cancelled by user")
        sys.exit(0)
    
    # Create repositories
    created_repos = []
    for repo_config in REPOSITORIES:
        repo = create_repository(g, username, repo_config)
        if repo:
            created_repos.append(repo)
        time.sleep(2)  # Rate limiting between repositories
    
    # Summary
    print(f"\n{'='*60}")
    print("🎉 Setup Complete!")
    print(f"{'='*60}")
    print(f"✅ Successfully created/updated {len(created_repos)} repositories")
    print(f"\n📍 Your GitHub Profile: https://github.com/{username}")
    print("\n📌 Next steps:")
    print("   1. Visit your profile to see the new README")
    print("   2. Pin your favorite repositories")
    print("   3. Start adding code to your projects")
    print("   4. Share on social media!")
    print("\n🚀 Your AI Engineer portfolio is ready!")


if __name__ == "__main__":
    main()

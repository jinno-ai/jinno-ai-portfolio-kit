#!/usr/bin/env python3
"""
GitHub Token Setup Helper

This script helps you securely configure your GitHub Personal Access Token.

Usage:
    python setup_token.py

Author: AI Assistant for jinno-ai
"""

import os
import sys
from pathlib import Path


def print_banner():
    """Print welcome banner."""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║          GitHub Token Setup Helper for jinno-ai              ║
    ║          Secure configuration of Personal Access Token       ║
    ╚══════════════════════════════════════════════════════════════╝
    """)


def print_instructions():
    """Print detailed instructions for getting a GitHub token."""
    print("""
📋 How to get your GitHub Personal Access Token:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Open this URL in your browser:
   👉 https://github.com/settings/tokens

2. Click "Generate new token (classic)"

3. Configure the token:
   • Note: Portfolio Automation
   • Expiration: 90 days (recommended)
   • Select scopes:
     ✅ repo (all sub-items)
     ✅ workflow
     ✅ write:packages

4. Click "Generate token" at the bottom

5. ⚠️  IMPORTANT: Copy the token immediately!
   It looks like: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   (You can only see it once!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)


def validate_token(token):
    """Validate token format."""
    if not token:
        return False, "Token is empty"
    
    if not token.startswith(('ghp_', 'github_pat_')):
        return False, "Token should start with 'ghp_' or 'github_pat_'"
    
    if len(token) < 40:
        return False, "Token seems too short (should be 40+ characters)"
    
    if ' ' in token:
        return False, "Token contains spaces (please remove them)"
    
    return True, "Token format looks valid"


def create_env_file(token):
    """Create .env file with the token."""
    env_path = Path(".env")
    
    # Backup existing .env if it exists
    if env_path.exists():
        backup_path = Path(".env.backup")
        try:
            with open(env_path, 'r') as f:
                content = f.read()
            with open(backup_path, 'w') as f:
                f.write(content)
            print(f"✅ Existing .env backed up to .env.backup")
        except Exception as e:
            print(f"⚠️  Warning: Could not backup existing .env: {e}")
    
    # Write new .env file
    try:
        with open(env_path, 'w') as f:
            f.write(f"GITHUB_TOKEN={token}\n")
        
        # Set file permissions (Unix-like systems only)
        try:
            os.chmod(env_path, 0o600)  # Read/write for owner only
        except:
            pass  # Windows doesn't support chmod
        
        print(f"✅ .env file created successfully!")
        print(f"   Location: {env_path.absolute()}")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False


def create_gitignore():
    """Ensure .env is in .gitignore."""
    gitignore_path = Path(".gitignore")
    
    # Read existing .gitignore if it exists
    if gitignore_path.exists():
        with open(gitignore_path, 'r') as f:
            content = f.read()
        
        if '.env' in content:
            print("✅ .env already in .gitignore")
            return
    
    # Add .env to .gitignore
    try:
        with open(gitignore_path, 'a') as f:
            f.write("\n# Environment variables\n")
            f.write(".env\n")
            f.write(".env.local\n")
            f.write(".env.*.local\n")
        print("✅ Added .env to .gitignore")
    except Exception as e:
        print(f"⚠️  Warning: Could not update .gitignore: {e}")


def test_token(token):
    """Test if the token works."""
    print("\n🔍 Testing token...")
    
    try:
        from github import Github
        
        g = Github(token)
        user = g.get_user()
        
        print(f"\n✅ Token is valid!")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"👤 Username: {user.login}")
        print(f"📧 Email: {user.email or 'Not public'}")
        print(f"👥 Followers: {user.followers}")
        print(f"📦 Public repos: {user.public_repos}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        return True
        
    except ImportError:
        print("\n⚠️  PyGithub not installed. Skipping token test.")
        print("   Install with: pip install PyGithub")
        return None
    except Exception as e:
        print(f"\n❌ Token test failed: {e}")
        print("   Please check your token and try again.")
        return False


def main():
    """Main function."""
    print_banner()
    
    # Check if .env already exists
    if Path(".env").exists():
        print("⚠️  .env file already exists!")
        response = input("   Do you want to replace it? (y/n): ").lower()
        if response != 'y':
            print("❌ Setup cancelled")
            sys.exit(0)
        print()
    
    print_instructions()
    
    # Get token from user
    while True:
        token = input("📝 Paste your GitHub token here: ").strip()
        
        if not token:
            print("❌ No token provided. Exiting.")
            sys.exit(1)
        
        # Validate token
        is_valid, message = validate_token(token)
        if is_valid:
            print(f"✅ {message}")
            break
        else:
            print(f"❌ {message}")
            retry = input("   Try again? (y/n): ").lower()
            if retry != 'y':
                sys.exit(1)
    
    # Create .env file
    print("\n📁 Creating .env file...")
    if not create_env_file(token):
        sys.exit(1)
    
    # Update .gitignore
    create_gitignore()
    
    # Test token
    test_result = test_token(token)
    
    # Final message
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                   🎉 Setup Complete!                         ║
    ╚══════════════════════════════════════════════════════════════╝
    
    ✅ Your GitHub token has been configured securely.
    
    Next steps:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    1. Run the repository creation script:
       python create_repositories.py
    
    2. Your .env file is protected (in .gitignore)
    
    3. Keep your token safe - never share it!
    
    🚀 Ready to create your GitHub portfolio!
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)
    
    if test_result is False:
        print("\n⚠️  Note: Token validation failed, but setup is complete.")
        print("   You may need to check your token permissions.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

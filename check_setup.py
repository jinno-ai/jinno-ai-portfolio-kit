#!/usr/bin/env python3
"""
Quick Setup Status Checker for jinno-ai Portfolio

This script checks the current setup status and suggests next steps.
"""

import os
import sys
from pathlib import Path

def print_header():
    print("""
╔══════════════════════════════════════════════════════════════╗
║     jinno-ai Portfolio - Setup Status Checker                ║
╚══════════════════════════════════════════════════════════════╝
""")

def check_env_file():
    """Check if .env file exists and has GITHUB_TOKEN"""
    env_path = Path(".env")
    if not env_path.exists():
        return False, "❌ .env file not found"
    
    try:
        with open(env_path, 'r') as f:
            content = f.read()
        
        if "GITHUB_TOKEN" not in content:
            return False, "❌ GITHUB_TOKEN not found in .env"
        
        # Check if token looks valid (not placeholder)
        for line in content.split('\n'):
            if line.startswith('GITHUB_TOKEN='):
                token = line.split('=', 1)[1].strip()
                if token and not token.startswith('your_'):
                    return True, "✅ .env file configured"
                else:
                    return False, "❌ GITHUB_TOKEN is placeholder value"
        
        return False, "❌ GITHUB_TOKEN not properly set"
    except Exception as e:
        return False, f"❌ Error reading .env: {e}"

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import github
        import dotenv
        return True, "✅ Dependencies installed (PyGithub, python-dotenv)"
    except ImportError as e:
        return False, f"❌ Missing dependency: {e.name}"

def check_github_connection():
    """Test GitHub API connection"""
    try:
        from github import Github
        from dotenv import load_dotenv
        
        load_dotenv()
        token = os.getenv("GITHUB_TOKEN")
        
        if not token:
            return False, "❌ GITHUB_TOKEN not loaded"
        
        g = Github(token)
        user = g.get_user()
        username = user.login
        
        return True, f"✅ Connected as: {username} ({user.public_repos} repos)"
    except Exception as e:
        return False, f"❌ GitHub connection failed: {str(e)[:50]}"

def check_repositories():
    """Check if repositories exist"""
    try:
        from github import Github
        from dotenv import load_dotenv
        
        load_dotenv()
        token = os.getenv("GITHUB_TOKEN")
        
        if not token:
            return False, "❌ Cannot check repositories (no token)"
        
        g = Github(token)
        user = g.get_user()
        repos = [repo.name for repo in user.get_repos()]
        
        expected_repos = [
            "jinno-ai",
            "enterprise-rag-system",
            "llm-agent-framework",
        ]
        
        found = [r for r in expected_repos if r in repos]
        missing = [r for r in expected_repos if r not in repos]
        
        if len(found) == len(expected_repos):
            return True, f"✅ All key repositories exist ({len(found)}/{len(expected_repos)})"
        elif len(found) > 0:
            return "partial", f"⚠️  Some repositories exist ({len(found)}/{len(expected_repos)})"
        else:
            return False, f"❌ Key repositories not found"
    except Exception as e:
        return False, f"❌ Cannot check repositories: {str(e)[:50]}"

def get_next_steps(status):
    """Suggest next steps based on current status"""
    env_ok, env_msg = status['env']
    deps_ok, deps_msg = status['deps']
    github_ok, github_msg = status['github']
    repos_ok, repos_msg = status['repos']
    
    print("\n" + "="*60)
    print("📋 CURRENT STATUS")
    print("="*60)
    print(f"1. Environment:   {env_msg}")
    print(f"2. Dependencies:  {deps_msg}")
    print(f"3. GitHub API:    {github_msg}")
    print(f"4. Repositories:  {repos_msg}")
    print("="*60)
    
    print("\n" + "="*60)
    print("🎯 RECOMMENDED NEXT STEPS")
    print("="*60)
    
    if not deps_ok:
        print("\n1️⃣  Install dependencies:")
        print("   pip install PyGithub python-dotenv")
        return
    
    if not env_ok:
        print("\n1️⃣  Setup GitHub token:")
        print("   python setup_token.py")
        print("   OR manually create .env with GITHUB_TOKEN=your_token")
        return
    
    if not github_ok:
        print("\n1️⃣  Fix GitHub connection:")
        print("   - Verify token in .env is correct")
        print("   - Check token permissions (repo, workflow)")
        print("   - Generate new token if needed")
        return
    
    if repos_ok == True:
        print("\n✅ Setup is complete! Ready for development.")
        print("\n📌 Development workflow:")
        print("   1. Clone a repository locally")
        print("   2. Create development branch")
        print("   3. Add code and commit regularly")
        print("   4. Push changes and create PRs")
        print("\n💡 Quick start with enterprise-rag-system:")
        print("   git clone https://github.com/jinno-ai/enterprise-rag-system.git")
        print("   cd enterprise-rag-system")
        print("   # Start developing!")
    elif repos_ok == "partial":
        print("\n1️⃣  Complete repository setup:")
        print("   python create_repositories.py")
        print("   (This will create missing repositories)")
    else:
        print("\n1️⃣  Create GitHub repositories:")
        print("   python create_repositories.py")
    
    print("\n" + "="*60)

def main():
    print_header()
    
    # Run all checks
    status = {
        'env': check_env_file(),
        'deps': check_dependencies(),
        'github': check_github_connection(),
        'repos': check_repositories()
    }
    
    # Display results and next steps
    get_next_steps(status)
    
    print("\n💡 For detailed guides, see:")
    print("   - IMPLEMENTATION_GUIDE.md (full workflow)")
    print("   - 実行手順.md (Japanese quick guide)")
    print("   - TOKEN_SETUP_GUIDE.md (token setup)")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nℹ️  Cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

#!/usr/bin/env python3
"""
Development Workflow Manager for jinno-ai Portfolio

Efficient development workflow for existing repositories.
"""

import os
import sys
import subprocess
from pathlib import Path

REPOS = {
    "enterprise-rag-system": {
        "url": "https://github.com/jinno-ai/enterprise-rag-system.git",
        "description": "Production-grade RAG pipeline",
        "priority": 1,
        "next_steps": [
            "Implement core RAG pipeline",
            "Add document ingestion scripts",
            "Create FastAPI endpoints",
            "Build Streamlit UI"
        ]
    },
    "llm-agent-framework": {
        "url": "https://github.com/jinno-ai/llm-agent-framework.git",
        "description": "Multi-agent orchestration system",
        "priority": 2,
        "next_steps": [
            "Implement base agent class",
            "Create ReAct agent implementation",
            "Add tool integration system",
            "Build agent orchestration"
        ]
    },
    "realtime-edge-detection": {
        "url": "https://github.com/jinno-ai/realtime-edge-detection.git",
        "description": "Low-latency object detection",
        "priority": 3,
        "next_steps": [
            "Setup YOLO v8 model",
            "Implement inference pipeline",
            "Add TensorRT optimization",
            "Create deployment scripts"
        ]
    },
    "multilingual-sentiment-analyzer": {
        "url": "https://github.com/jinno-ai/multilingual-sentiment-analyzer.git",
        "description": "Cross-lingual sentiment analysis",
        "priority": 4,
        "next_steps": [
            "Load XLM-RoBERTa model",
            "Implement preprocessing",
            "Create FastAPI endpoint",
            "Add model fine-tuning scripts"
        ]
    },
    "micro-instruction-engineering": {
        "url": "https://github.com/jinno-ai/micro-instruction-engineering.git",
        "description": "Prompt optimization methodology",
        "priority": 5,
        "next_steps": [
            "Create prompt templates",
            "Implement evaluation framework",
            "Add benchmark datasets",
            "Build comparison tools"
        ]
    }
}

def print_header():
    print("""
╔══════════════════════════════════════════════════════════════╗
║         jinno-ai Portfolio - Development Workflow            ║
║         Efficient project management for active repos        ║
╚══════════════════════════════════════════════════════════════╝
""")

def check_local_repos():
    """Check which repositories are cloned locally"""
    local_repos = {}
    for repo_name in REPOS.keys():
        repo_path = Path(repo_name)
        if repo_path.exists() and (repo_path / ".git").exists():
            local_repos[repo_name] = repo_path
    return local_repos

def clone_repository(repo_name, repo_info):
    """Clone a repository"""
    print(f"\n📦 Cloning {repo_name}...")
    try:
        result = subprocess.run(
            ["git", "clone", repo_info["url"]],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ Successfully cloned {repo_name}")
            return True
        else:
            print(f"❌ Failed to clone: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def get_repo_status(repo_path):
    """Get git status of a repository"""
    try:
        # Get current branch
        branch_result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        branch = branch_result.stdout.strip()
        
        # Get number of commits
        commit_result = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        commits = commit_result.stdout.strip()
        
        # Check if there are uncommitted changes
        status_result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        has_changes = len(status_result.stdout.strip()) > 0
        
        return {
            "branch": branch,
            "commits": commits,
            "has_changes": has_changes
        }
    except Exception as e:
        return None

def display_menu(local_repos):
    """Display interactive menu"""
    print("\n" + "="*60)
    print("📚 REPOSITORY STATUS")
    print("="*60)
    
    if not local_repos:
        print("\n⚠️  No repositories found locally.")
        print("\nYou need to clone repositories first.")
    
    for i, (repo_name, repo_info) in enumerate(REPOS.items(), 1):
        if repo_name in local_repos:
            status = get_repo_status(local_repos[repo_name])
            if status:
                change_mark = "📝" if status["has_changes"] else "✓"
                print(f"\n{i}. {change_mark} {repo_name}")
                print(f"   Branch: {status['branch']} | Commits: {status['commits']}")
                print(f"   📂 {local_repos[repo_name].absolute()}")
            else:
                print(f"\n{i}. ⚠️  {repo_name} (git status unavailable)")
        else:
            print(f"\n{i}. ⭕ {repo_name} (not cloned)")
        
        print(f"   {repo_info['description']}")
    
    print("\n" + "="*60)
    print("⚙️  ACTIONS")
    print("="*60)
    print("[c] Clone missing repositories")
    print("[s] Show development priorities")
    print("[1-5] Open repository in new terminal")
    print("[q] Quit")
    print("="*60)

def show_priorities():
    """Show development priorities and next steps"""
    print("\n" + "="*60)
    print("🎯 DEVELOPMENT PRIORITIES")
    print("="*60)
    
    sorted_repos = sorted(REPOS.items(), key=lambda x: x[1]["priority"])
    
    for repo_name, repo_info in sorted_repos:
        print(f"\n{repo_info['priority']}. {repo_name}")
        print(f"   {repo_info['description']}")
        print(f"   Next steps:")
        for step in repo_info['next_steps']:
            print(f"   - {step}")
    
    print("\n" + "="*60)

def clone_all_missing(local_repos):
    """Clone all repositories that aren't local"""
    missing = [name for name in REPOS.keys() if name not in local_repos]
    
    if not missing:
        print("\n✅ All repositories are already cloned!")
        return
    
    print(f"\n📦 Found {len(missing)} repositories to clone:")
    for repo in missing:
        print(f"   - {repo}")
    
    response = input("\n🤔 Clone all missing repositories? (y/n): ").lower()
    if response != 'y':
        print("❌ Cancelled")
        return
    
    for repo_name in missing:
        clone_repository(repo_name, REPOS[repo_name])
    
    print("\n✅ Clone process complete!")

def main():
    print_header()
    
    # Check current directory
    cwd = Path.cwd()
    print(f"📂 Working directory: {cwd}")
    
    while True:
        local_repos = check_local_repos()
        display_menu(local_repos)
        
        choice = input("\n👉 Choose an action: ").strip().lower()
        
        if choice == 'q':
            print("\n👋 Goodbye!")
            break
        elif choice == 'c':
            clone_all_missing(local_repos)
        elif choice == 's':
            show_priorities()
        elif choice in ['1', '2', '3', '4', '5']:
            idx = int(choice) - 1
            repo_name = list(REPOS.keys())[idx]
            
            if repo_name in local_repos:
                repo_path = local_repos[repo_name]
                print(f"\n📂 Opening {repo_name}...")
                print(f"   Path: {repo_path.absolute()}")
                print(f"\n💡 To start working:")
                print(f"   cd {repo_name}")
                print(f"   git checkout -b feature/your-feature")
                print(f"   # Start coding!")
                input("\nPress Enter to continue...")
            else:
                print(f"\n⚠️  {repo_name} is not cloned yet.")
                response = input("   Clone now? (y/n): ").lower()
                if response == 'y':
                    clone_repository(repo_name, REPOS[repo_name])
        else:
            print("❌ Invalid choice")
        
        print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

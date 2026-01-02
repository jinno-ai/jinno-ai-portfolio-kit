#!/bin/bash
# Push all repositories to GitHub
# Usage: bash push_all_repos.sh [github_token]

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   Push All Repositories to GitHub                           ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if token provided
if [ -z "$1" ]; then
    if [ -f ".env" ]; then
        echo -e "${GREEN}✅ Using token from .env file${NC}"
        source .env
        TOKEN="$GITHUB_TOKEN"
    else
        echo -e "${RED}❌ GitHub token required${NC}"
        echo "Usage: bash push_all_repos.sh <github_token>"
        echo "   OR: Create .env with GITHUB_TOKEN=your_token"
        exit 1
    fi
else
    TOKEN="$1"
fi

# Repositories to push
REPOS=(
    "enterprise-rag-system"
    "llm-agent-framework"
    "realtime-edge-detection"
    "multilingual-sentiment-analyzer"
    "micro-instruction-engineering"
)

# Function to push repository
push_repo() {
    local repo=$1
    echo ""
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}📦 Pushing: $repo${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    if [ ! -d "$repo" ]; then
        echo -e "${RED}❌ Directory not found: $repo${NC}"
        return 1
    fi
    
    cd "$repo"
    
    # Check if there are commits
    if ! git rev-parse HEAD >/dev/null 2>&1; then
        echo -e "${YELLOW}⚠️  No commits in $repo${NC}"
        cd ..
        return 0
    fi
    
    # Configure remote with token
    REMOTE_URL="https://${TOKEN}@github.com/jinno-ai/${repo}.git"
    git remote set-url origin "$REMOTE_URL" 2>/dev/null || git remote add origin "$REMOTE_URL"
    
    # Get current branch
    BRANCH=$(git rev-parse --abbrev-ref HEAD)
    
    # Push
    if git push origin "$BRANCH" 2>&1; then
        echo -e "${GREEN}✅ Successfully pushed $repo (branch: $BRANCH)${NC}"
        
        # Show PR creation URL
        echo -e "${GREEN}📝 Create PR:${NC}"
        echo "   https://github.com/jinno-ai/${repo}/pull/new/${BRANCH}"
    else
        echo -e "${RED}❌ Failed to push $repo${NC}"
        cd ..
        return 1
    fi
    
    cd ..
}

# Push all repositories
SUCCESS_COUNT=0
FAIL_COUNT=0

for repo in "${REPOS[@]}"; do
    if push_repo "$repo"; then
        ((SUCCESS_COUNT++))
    else
        ((FAIL_COUNT++))
    fi
done

# Summary
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}📊 Summary${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Successfully pushed: $SUCCESS_COUNT${NC}"
if [ $FAIL_COUNT -gt 0 ]; then
    echo -e "${RED}❌ Failed: $FAIL_COUNT${NC}"
fi
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
    echo -e "${GREEN}🎉 All repositories pushed successfully!${NC}"
    echo ""
    echo -e "${GREEN}📝 Next steps:${NC}"
    echo "1. Create Pull Requests for each repository"
    echo "2. Review and merge PRs"
    echo "3. Update repository descriptions and topics"
    echo "4. Pin repositories on your profile"
else
    echo -e "${YELLOW}⚠️  Some repositories failed to push${NC}"
    echo "Please check the errors above and retry"
fi

echo ""

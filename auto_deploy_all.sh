#!/bin/bash
# Automatic Deploy All Repositories
# Push, Create PR, and Merge automatically
# Usage: bash auto_deploy_all.sh [github_token]

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║   Automatic Deploy All Repositories to GitHub               ║${NC}"
echo -e "${CYAN}║   Push → Create PR → Merge                                   ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Get token
if [ -z "$1" ]; then
    if [ -f ".env" ]; then
        source .env
        TOKEN="$GITHUB_TOKEN"
    else
        echo -e "${RED}❌ GitHub token required${NC}"
        echo "Usage: bash auto_deploy_all.sh <github_token>"
        exit 1
    fi
else
    TOKEN="$1"
fi

# Check if gh CLI is available
USE_GH_CLI=false
if command -v gh &> /dev/null; then
    if gh auth status &> /dev/null; then
        USE_GH_CLI=true
        echo -e "${GREEN}✅ GitHub CLI detected and authenticated${NC}"
    else
        echo -e "${YELLOW}⚠️  GitHub CLI not authenticated, using API${NC}"
    fi
fi

# Repositories
REPOS=(
    "enterprise-rag-system"
    "llm-agent-framework"
    "realtime-edge-detection"
    "multilingual-sentiment-analyzer"
    "micro-instruction-engineering"
)

SUCCESS_COUNT=0
FAIL_COUNT=0

# Function to deploy repository
deploy_repo() {
    local repo=$1
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}🚀 Deploying: $repo${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
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
    
    # Step 1: Push
    echo -e "${YELLOW}📤 Step 1/3: Pushing to GitHub...${NC}"
    if git push origin "$BRANCH" -f 2>&1; then
        echo -e "${GREEN}✅ Pushed successfully${NC}"
    else
        echo -e "${RED}❌ Failed to push${NC}"
        cd ..
        return 1
    fi
    
    # Step 2: Create PR
    echo -e "${YELLOW}📝 Step 2/3: Creating Pull Request...${NC}"
    
    if [ "$USE_GH_CLI" = true ]; then
        # Use GitHub CLI
        PR_URL=$(gh pr create \
            --base main \
            --head "$BRANCH" \
            --title "feat: Initial implementation - $repo" \
            --body "Automated deployment of $repo implementation" \
            --repo "jinno-ai/$repo" 2>&1 | grep "https://github.com" || echo "")
        
        if [ -n "$PR_URL" ]; then
            echo -e "${GREEN}✅ PR created: $PR_URL${NC}"
            PR_NUMBER=$(echo "$PR_URL" | grep -oP '/pull/\K\d+')
        else
            echo -e "${YELLOW}⚠️  PR might already exist or failed to create${NC}"
            cd ..
            return 0
        fi
    else
        # Use GitHub API
        PR_RESPONSE=$(curl -s -X POST \
            -H "Authorization: token $TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/jinno-ai/$repo/pulls" \
            -d "{\"title\":\"feat: Initial implementation - $repo\",\"body\":\"Automated deployment of $repo implementation\",\"head\":\"$BRANCH\",\"base\":\"main\"}")
        
        PR_NUMBER=$(echo "$PR_RESPONSE" | grep -oP '"number":\s*\K\d+' | head -1)
        
        if [ -n "$PR_NUMBER" ]; then
            echo -e "${GREEN}✅ PR #$PR_NUMBER created${NC}"
        else
            ERROR_MSG=$(echo "$PR_RESPONSE" | grep -oP '"message":\s*"\K[^"]+')
            if [[ "$ERROR_MSG" == *"already exists"* ]]; then
                echo -e "${YELLOW}⚠️  PR already exists, fetching existing PR...${NC}"
                EXISTING_PR=$(curl -s -H "Authorization: token $TOKEN" \
                    "https://api.github.com/repos/jinno-ai/$repo/pulls?head=jinno-ai:$BRANCH&base=main")
                PR_NUMBER=$(echo "$EXISTING_PR" | grep -oP '"number":\s*\K\d+' | head -1)
            else
                echo -e "${RED}❌ Failed to create PR: $ERROR_MSG${NC}"
                cd ..
                return 1
            fi
        fi
    fi
    
    # Step 3: Merge PR
    echo -e "${YELLOW}🔀 Step 3/3: Merging Pull Request...${NC}"
    sleep 2  # Wait a moment for PR to be ready
    
    if [ "$USE_GH_CLI" = true ]; then
        if gh pr merge "$PR_NUMBER" --merge --delete-branch --repo "jinno-ai/$repo" 2>&1; then
            echo -e "${GREEN}✅ PR merged successfully${NC}"
        else
            echo -e "${YELLOW}⚠️  Manual merge might be required${NC}"
        fi
    else
        MERGE_RESPONSE=$(curl -s -X PUT \
            -H "Authorization: token $TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/jinno-ai/$repo/pulls/$PR_NUMBER/merge" \
            -d "{\"merge_method\":\"merge\"}")
        
        if echo "$MERGE_RESPONSE" | grep -q '"merged": true'; then
            echo -e "${GREEN}✅ PR merged successfully${NC}"
            
            # Delete branch
            curl -s -X DELETE \
                -H "Authorization: token $TOKEN" \
                "https://api.github.com/repos/jinno-ai/$repo/git/refs/heads/$BRANCH" > /dev/null
            echo -e "${GREEN}✅ Branch deleted${NC}"
        else
            ERROR_MSG=$(echo "$MERGE_RESPONSE" | grep -oP '"message":\s*"\K[^"]+')
            echo -e "${YELLOW}⚠️  Merge status: $ERROR_MSG${NC}"
        fi
    fi
    
    echo -e "${GREEN}🎉 Deployment complete for $repo${NC}"
    cd ..
    return 0
}

# Deploy all repositories
for repo in "${REPOS[@]}"; do
    if deploy_repo "$repo"; then
        ((SUCCESS_COUNT++))
    else
        ((FAIL_COUNT++))
    fi
done

# Summary
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}📊 Deployment Summary${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Successfully deployed: $SUCCESS_COUNT${NC}"
if [ $FAIL_COUNT -gt 0 ]; then
    echo -e "${RED}❌ Failed: $FAIL_COUNT${NC}"
fi
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
    echo -e "${GREEN}🎉 All repositories deployed successfully!${NC}"
    echo ""
    echo -e "${GREEN}✅ Check your repositories:${NC}"
    echo "   https://github.com/jinno-ai"
else
    echo -e "${YELLOW}⚠️  Some repositories had issues${NC}"
fi

echo ""

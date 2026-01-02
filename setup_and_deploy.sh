#!/bin/bash
# Complete Setup and Deploy
# Interactive setup + automatic deployment
# Usage: bash setup_and_deploy.sh

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║   Complete Setup and Deploy - jinno-ai Portfolio            ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if .env exists
if [ -f ".env" ] && grep -q "GITHUB_TOKEN" .env; then
    echo -e "${GREEN}✅ .env file found with GITHUB_TOKEN${NC}"
    source .env
    if [ -n "$GITHUB_TOKEN" ]; then
        echo -e "${GREEN}✅ Token loaded from .env${NC}"
        TOKEN="$GITHUB_TOKEN"
    else
        echo -e "${RED}❌ GITHUB_TOKEN is empty in .env${NC}"
        TOKEN=""
    fi
else
    echo -e "${YELLOW}⚠️  .env file not found or incomplete${NC}"
    TOKEN=""
fi

# If no token, ask for it
if [ -z "$TOKEN" ]; then
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}📋 GitHub Token Setup${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "To get your GitHub token:"
    echo "1. Visit: https://github.com/settings/tokens"
    echo "2. Click 'Generate new token (classic)'"
    echo "3. Select scopes: repo, workflow"
    echo "4. Copy the token (starts with ghp_)"
    echo ""
    read -p "Enter your GitHub token: " TOKEN
    
    if [ -z "$TOKEN" ]; then
        echo -e "${RED}❌ No token provided. Exiting.${NC}"
        exit 1
    fi
    
    # Save to .env
    echo "GITHUB_TOKEN=$TOKEN" > .env
    chmod 600 .env
    echo -e "${GREEN}✅ Token saved to .env${NC}"
fi

# Validate token format
if [[ ! "$TOKEN" =~ ^(ghp_|github_pat_) ]]; then
    echo -e "${RED}❌ Invalid token format${NC}"
    echo "Token should start with 'ghp_' or 'github_pat_'"
    exit 1
fi

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}🚀 Starting Automatic Deployment${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Run auto deploy
bash auto_deploy_all.sh "$TOKEN"

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   🎉 All Done! Check your repositories:                     ║${NC}"
echo -e "${GREEN}║   https://github.com/jinno-ai                                ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

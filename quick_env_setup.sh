#!/bin/bash
# Quick .env file setup for development
# Usage: bash quick_env_setup.sh [token]

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}╔══════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   Quick .env Setup for jinno-ai Development     ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════╝${NC}"
echo ""

# Check if token provided as argument
if [ -n "$1" ]; then
    TOKEN="$1"
    echo -e "${GREEN}✅ Token provided as argument${NC}"
else
    # Check if .env already exists
    if [ -f ".env" ]; then
        echo -e "${YELLOW}⚠️  .env file already exists!${NC}"
        cat .env
        echo ""
        read -p "Replace it? (y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${GREEN}✅ Using existing .env${NC}"
            exit 0
        fi
    fi
    
    # Ask for token
    echo -e "${YELLOW}Please enter your GitHub token:${NC}"
    echo "(Get it from: https://github.com/settings/tokens)"
    read -p "Token: " TOKEN
fi

# Validate token format
if [[ ! $TOKEN =~ ^(ghp_|github_pat_) ]]; then
    echo -e "${RED}❌ Invalid token format${NC}"
    echo "Token should start with 'ghp_' or 'github_pat_'"
    exit 1
fi

# Create .env file
echo "GITHUB_TOKEN=$TOKEN" > .env
chmod 600 .env

echo -e "${GREEN}✅ .env file created successfully!${NC}"
echo ""
echo -e "${GREEN}📋 Next steps:${NC}"
echo "  1. Run: python check_setup.py"
echo "  2. Run: python dev_workflow.py"
echo "  3. Start developing!"
echo ""

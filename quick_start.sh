#!/bin/bash
# Quick Start Script for jinno-ai Portfolio Kit
# Usage: bash quick_start.sh

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║   jinno-ai GitHub Portfolio Quick Start                     ║"
echo "║   魅力的なAIエンジニアポートフォリオを10分で完成!              ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Step 1: Check Python version
echo -e "\n${BLUE}[Step 1/4]${NC} Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo -e "${RED}❌ Error: Python not found${NC}"
    echo "Please install Python 3.8+ first"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✅ Python $PYTHON_VERSION found${NC}"

# Step 2: Install dependencies
echo -e "\n${BLUE}[Step 2/4]${NC} Installing dependencies..."
echo -e "${YELLOW}Running: pip install PyGithub python-dotenv${NC}"

if $PYTHON_CMD -m pip install PyGithub python-dotenv --quiet; then
    echo -e "${GREEN}✅ Dependencies installed successfully${NC}"
else
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    echo "Please run manually: pip install PyGithub python-dotenv"
    exit 1
fi

# Step 3: Setup GitHub token
echo -e "\n${BLUE}[Step 3/4]${NC} Setting up GitHub token..."
echo -e "${YELLOW}Running: python setup_token.py${NC}"
echo ""

if [ -f ".env" ]; then
    echo -e "${YELLOW}⚠️  .env file already exists${NC}"
    read -p "Do you want to recreate it? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${GREEN}✅ Using existing .env file${NC}"
    else
        rm .env
        $PYTHON_CMD setup_token.py
    fi
else
    $PYTHON_CMD setup_token.py
fi

# Verify .env file exists
if [ ! -f ".env" ]; then
    echo -e "${RED}❌ .env file not created${NC}"
    echo "Please run setup_token.py manually"
    exit 1
fi

echo -e "${GREEN}✅ GitHub token configured${NC}"

# Step 4: Create repositories
echo -e "\n${BLUE}[Step 4/4]${NC} Creating GitHub repositories..."
echo -e "${YELLOW}Running: python create_repositories.py${NC}"
echo ""

$PYTHON_CMD create_repositories.py

# Success message
echo -e "\n${GREEN}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║   🎉 Setup Complete! 🎉                                     ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "\n${CYAN}📍 Your GitHub Profile:${NC} https://github.com/jinno-ai"
echo ""
echo -e "${YELLOW}📌 Next Steps:${NC}"
echo "   1. Visit your profile to see the new README"
echo "   2. Go to your profile and click 'Customize your pins'"
echo "   3. Select 6 repositories to pin"
echo "   4. Update Profile README links (LinkedIn, Twitter, etc.)"
echo "   5. Share on social media!"
echo ""
echo -e "${GREEN}🚀 Your AI Engineer portfolio is ready!${NC}"
echo ""

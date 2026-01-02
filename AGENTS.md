# AI Agent Operational Guide (AGENTS.md)

This document outlines the environment setup and operational procedures for AI agents working within this repository. This repository is a **Portfolio Setup Kit** for managing AI-focused submodules.

## 1. Repository Overview

The root repository contains automation scripts to manage a collection of submodules (portfolio projects).

### Key Components:
- **Root**: Automation scripts (`.py`, `.sh`), documentation.
- **Submodules**: Individual projects (e.g., `enterprise-rag-system`, `llm-agent-framework`) located in their respective directories.

## 2. Environment Setup

### Prerequisites
- **Python**: Version 3.8+
- **Docker**: Required for running submodules like `enterprise-rag-system`
- **Git**: Configured for the user `jinno-ai`
- **SSH**: GitHub SSH key configured (for git operations)

### Initial Configuration
1. **Install Dependencies**:
   ```bash
   pip install PyGithub python-dotenv
   ```

2. **Update Submodules**:
   ```bash
   git submodule update --init --recursive
   ```

## 3. Operational Procedures

### A. Submodule Development
Each submodule is a standalone project. When working on a submodule:

1. **Navigate**: `cd enterprise-rag-system`
2. **Context**: Read the specific `README.md` and `docker-compose.yml` in that directory.
3. **Testing**:
   - **Unit Tests**: `pytest` (if available in `tests/`)
   - **Integration**: `docker-compose up -d` to spin up services
4. **Verification**:
   - Before declaring a task complete, verify the application starts (e.g., check `docker ps` or curl the API endpoint)

**Example: `enterprise-rag-system`**
- **Type**: FastAPI + Streamlit + Pinecone
- **Run**: `docker-compose up -d`
- **Verify**: Check `localhost:8000/docs` (API) and `localhost:8501` (UI)

### B. Git Operations
- **Manual workflow**: Use standard git commands with SSH
  ```bash
  git add .
  git commit -m "message"
  git push origin main
  ```
- **Feature branches**: Create branches for development
  ```bash
  git checkout -b feature/my-feature
  ```

## 4. Agent Guidelines & Rules

1. **Verification is Mandatory**:
   - Always verify file creations/edits
   - Always verify script execution results
2. **Security**:
   - **NEVER** commit `.env` or secrets
   - **NEVER** output full API keys in logs
3. **File System**:
   - Focus development work inside the submodule directories
4. **Git Operations**:
   - Use SSH for git operations
   - Ensure you're on the correct branch before committing

## 5. Submodules Overview

| Submodule | Description | Tech Stack |
|-----------|-------------|------------|
| enterprise-rag-system | Production RAG pipeline | FastAPI, Streamlit, Pinecone |
| llm-agent-framework | Multi-agent orchestration | LangGraph, LangChain |
| micro-instruction-engineering | Prompt optimization | Python, LLM APIs |
| multilingual-sentiment-analyzer | Cross-lingual sentiment | Transformers, PyTorch |
| realtime-edge-detection | Low-latency object detection | OpenCV, TensorFlow |

## 6. Common Commands

```bash
# Update all submodules
git submodule update --remote --merge

# Check submodule status
git submodule status

# Work in specific submodule
cd enterprise-rag-system
docker-compose up -d

# Test Python packages
cd llm-agent-framework
pip install -r requirements.txt
pytest tests/
```

## 7. Troubleshooting

- **Submodule issues**: Run `git submodule update --init --recursive`
- **Docker failures**: Check `docker logs <container_name>`
- **Permission denied**: Run `chmod +x *.sh`
- **Missing dependencies**: Run `pip install -r requirements.txt`

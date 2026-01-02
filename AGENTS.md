# AI Agent Operational Guide (AGENTS.md)

This document outlines the environment setup and operational procedures for AI agents (like Jules) working within this repository. This repository is a **Portfolio Setup Kit** designed to automate the creation and deployment of multiple AI-focused repositories.

## 1. Repository Overview

The root repository contains automation scripts to manage a collection of submodules (portfolio projects).
The goal is to support **autonomous development and operation** of these submodules.

### Key Components:
- **Root**: Automation scripts (`.py`, `.sh`), documentation.
- **Submodules**: Individual projects (e.g., `enterprise-rag-system`, `llm-agent-framework`) located in their respective directories.

## 2. Environment Setup

### Prerequisites
- **Python**: Version 3.8+ is required.
- **Docker**: Required for running submodules like `enterprise-rag-system`.
- **Git**: Configured for the user `jinno-ai`.

### Initial Configuration
1.  **Install Dependencies**:
    ```bash
    pip install PyGithub python-dotenv
    ```
    *Note: `quick_start.sh` handles this automatically.*

2.  **Token Setup**:
    - The repository requires a GitHub Personal Access Token (PAT).
    - Tokens are managed via `.env` file (excluded from git).
    - **Setup Script**:
        ```bash
        python3 setup_token.py
        ```
    - **Agent Instruction**: Do not create or overwrite `.env` unless explicitly instructed to reset credentials. Read environment variables from the environment or assume they are pre-loaded in the runtime if `.env` is absent but checking `.env` is standard procedure here.

## 3. Operational Procedures

### A. Initialization
To set up the entire portfolio from scratch (idempotent):
```bash
bash quick_start.sh
```
This script:
1.  Checks Python version.
2.  Installs dependencies.
3.  Runs `setup_token.py` (if `.env` missing).
4.  Runs `create_repositories.py` to ensure remote repos exist.

### B. Deployment Cycle
When changes are made to any submodule or the root:
```bash
bash auto_deploy_all.sh
```
This script:
1.  Iterates through all defined repositories.
2.  Pushes changes to GitHub.
3.  **Automatically creates a Pull Request**.
4.  **Automatically merges the PR** into `main`.
5.  Deletes the feature branch.

**Agent Rule**: When asked to "deploy" or "submit" changes to the remote, prefer using `auto_deploy_all.sh` over manual git commands to ensure the PR/Merge workflow is followed.

### C. Submodule Development
Each submodule is a standalone project. When working on a submodule (e.g., `enterprise-rag-system`):

1.  **Navigate**: `cd enterprise-rag-system`
2.  **Context**: Read the specific `README.md` and `docker-compose.yml` in that directory.
3.  **Testing**:
    - **Unit Tests**: `pytest` (if available in `tests/`).
    - **Integration**: `docker-compose up -d` to spin up services.
4.  **Verification**:
    - Before declaring a task complete, verify the application starts (e.g., check `docker ps` or curl the API endpoint).

**Example: `enterprise-rag-system`**
- **Type**: FastAPI + Streamlit + Pinecone.
- **Run**: `docker-compose up -d`
- **Verify**: Check `localhost:8000/docs` (API) and `localhost:8501` (UI).

## 4. Agent Guidelines & Rules

1.  **Verification is Mandatory**:
    - Always verify file creations/edits with `read_file`.
    - Always verify script execution results.
2.  **Security**:
    - **NEVER** commit `.env` or secrets.
    - **NEVER** output full API keys in logs or conversation history.
3.  **File System**:
    - Do not modify `auto_deploy_all.sh` or `setup_token.py` unless the task specifically requests changing the *automation logic itself*.
    - Focus development work inside the submodule directories.
4.  **Git Operations**:
    - The `auto_deploy_all.sh` script handles git commit/push/PR/merge.
    - If manual git is required, ensure you are on a feature branch, not `main`.

## 5. Troubleshooting

- **Script Permission Denied**: Run `chmod +x *.sh`.
- **Missing Dependencies**: Run `pip install -r requirements.txt`.
- **Docker Failures**: Check `docker logs <container_name>`.

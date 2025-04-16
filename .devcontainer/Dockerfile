FROM mcr.microsoft.com/devcontainers/python:3

# The base image already includes:
# - A non-root user 'vscode'
# - Python, pip, git and common tools
# - Basic VSCode configuration

# Install additional Python tools
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir setuptools wheel flake8 black pytest pytest-asyncio build



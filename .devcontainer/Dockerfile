FROM mcr.microsoft.com/devcontainers/python:3

# The base image already includes:
# - A non-root user 'vscode'
# - Python, pip, git and common tools
# - Basic VSCode configuration

# Install additional Python tools
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir setuptools wheel flake8 black pytest pytest-asyncio build

# Install Poetry
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry \
    && poetry config virtualenvs.create false

# Verify installation
RUN poetry --version

# Copy test script
COPY .devcontainer/test-poetry.sh /usr/local/bin/test-poetry.sh
RUN chmod +x /usr/local/bin/test-poetry.sh



from setuptools import setup, find_namespace_packages

setup(
    name="microsoft-agents-client",
    version="0.0.0a1",
    packages=find_namespace_packages(),
    install_requires=[
        "microsoft-agents-protocols",
    ],
    author="Microsoft Corporation",
    description="A client library for Microsoft Agents",
    url="https://github.com/yourusername/microsoft-agents-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

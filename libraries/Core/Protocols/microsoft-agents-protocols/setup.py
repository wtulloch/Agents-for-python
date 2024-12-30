from setuptools import setup, find_namespace_packages

setup(
    name="microsoft-agents-protocols",
    version="0.0.0a1",
    packages=find_namespace_packages(),
    install_requires=[
        "azure-core>=1.30.0",
        "isodate>=0.6.1",
        "pydantic>=2.10.4"
    ],
    author="Microsoft Corporation",
    description="A protocol library for Microsoft Agents",
    url="https://github.com/microsoft/microsoft-agents-protocol",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

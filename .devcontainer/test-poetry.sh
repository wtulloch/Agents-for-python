#!/bin/bash
set -e

echo "Testing Poetry installation..."
which poetry
poetry --version
echo "Poetry is installed correctly!"

echo "Checking Poetry configuration..."
poetry config --list

echo "Test complete - Poetry is working!"
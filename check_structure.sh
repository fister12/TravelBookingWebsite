#!/bin/bash

# Directory Structure Diagnostic Script
echo "🔍 Checking directory structure..."
echo ""
echo "Current directory: $(pwd)"
echo ""
echo "Contents of current directory:"
ls -la
echo ""
echo "Looking for manage.py:"
if [ -f "manage.py" ]; then
    echo "✅ manage.py found in current directory"
else
    echo "❌ manage.py not found in current directory"
fi
echo ""
echo "Looking for Django project structure..."
if [ -d "travel_project" ]; then
    echo "✅ travel_project directory found"
    echo "Contents of travel_project/:"
    ls -la travel_project/
else
    echo "❌ travel_project directory not found"
fi
echo ""
echo "Looking for booking app..."
if [ -d "booking" ]; then
    echo "✅ booking directory found"
    echo "Contents of booking/:"
    ls -la booking/ | head -10
else
    echo "❌ booking directory not found"
fi
echo ""
echo "Python version:"
python3 --version
echo ""
echo "Virtual environment status:"
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Virtual environment active: $VIRTUAL_ENV"
else
    echo "⚠️  No virtual environment active"
fi

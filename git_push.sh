#!/bin/bash
# Check if commit message is provided
if [ -z "$1" ]
then
  echo "Please provide a commit message."
  exit 1
fi

# Add changes
git add .

# Commit changes with provided message
git commit -m "$1"

# Push changes to the main branch
git push origin main

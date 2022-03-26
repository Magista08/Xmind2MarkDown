#!/bin/bash

set -eu

if [ $# -ne 1 ];then
    echo "USAGE: $0 <GitHub_url>"
fi

GITHUB_URL=$1

# Check if git installed yet
GIT_EXIST=`which git | wc -l`
if [ $GIT_EXIST -ne 1 ]; then
    apt install git
fi

# Create the local repository
git init
git add -A
git commit -m "First commit"
git branch -M main

# Connect the remote repository
git remote add origin $GITHUB_URL
git push -u origin main
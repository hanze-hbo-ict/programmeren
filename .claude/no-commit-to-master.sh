#!/usr/bin/env bash
# Blokkeer directe commits op master, maar sta cherry-picks en merges toe
# (cherry-picks zijn de normale "propageer naar master" workflow)

git_dir=$(git rev-parse --git-dir)

if [ -f "$git_dir/CHERRY_PICK_HEAD" ]; then
    exit 0
fi

if [ -f "$git_dir/MERGE_HEAD" ]; then
    exit 0
fi

branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "master" ]; then
    echo "GEBLOKKEERD: commit nooit direct op master. Maak een feature branch."
    exit 1
fi

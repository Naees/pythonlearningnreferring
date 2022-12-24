# pythonlearningnreferring
second iteration of the python ghome

This is a personal python "cheatsheet" for myself as I am still in the learning stages. I left the details in public mode to allow any and everyone to learn.
All of the code listed are from public sources and I hope that we can all have an enjoyable and easy time learning about Python.





  Some help for Git/Github if you are having problems with Git/Github
  
  Pull from Github:
  
git pull origin <name>
  
  Creating a new repository on the command line:
  
git init
git commit -m "random commit message"
git branch -M main
git remote add origin <random git url>
git push -u origin main

  Add changes from a single/all files:
  
git add .
git add <filename>
  
  Savechanges with message (aka commiting):
  
git commit -m  "add message here"
  
  Push an existing repo:
  
git remote add origin <random git url>
git branch - M main
git push -u origin main
  
  Git setup for CLI:
  
git config --global user.name "username"
git config --global user.email "email"

  Git branches to create new branches and switch to those branches:
  
git checkout -b <name of new branch>
git branch

  Merging branches by pushing new branch:
  
git branch
git push origin <name of branch that you want to push>
  
  Traveling to an old commit:
  
git checkout <hash of an older commit which can be found in the logs>
  
  Git log:
git log

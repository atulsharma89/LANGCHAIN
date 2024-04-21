### create  an r git repository on Git server and execute following commnands

…or create a new repository on the command line
===============================================

echo "# LANGCHAIN" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/atulsharma89/LANGCHAIN.git

git push -u origin main




…or push an existing repository from the command line
======================

git remote add origin https://github.com/atulsharma89/LANGCHAIN.git

git branch -M main

git push -u origin main


### Creating a virtual environment

conda create -p myenv python ==3.10

conda activate myenv/

### add the code files app.py (Langchain Chat Bot using streamlit and Open AI)

### Test the program on local by excuting

streamlit run app.py


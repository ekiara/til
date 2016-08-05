# Push your repository to multiple remote origins

<On your devmachine>
$ cd Projects
$ mkdir new_project
$ cd new_project
$ git init
$ touch .gitignore # or echo .log >> .gitignore
$ git add .
$ git commit -m "Initial commit"

<On github.com>
Create a new repository with the name new_project

<On bitbucket.org>
Create a new repository with the name new_project

<Back to your devmachine>


$ git remote add origin git@github.com:<your_github_username>/new_project.git

$ git remote set-url --add --push origin git@bitbucket.org:<your_github_username>/new_project.git

$ git remote set-url --add --push origin git@github.com:<your_github_username>/new_project.git

$ git remote -v

origin  git@github.com:<your_github_username>/new_project.git (fetch)                                  
origin  git@bitbucket.org:<your_github_username>/new_project.git (push)                                
origin  git@github.com:<your_github_username>/new_project.git (push)                                                                                                   

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
Create a new repository with the name <project_name>

<On bitbucket.org>
Create a new repository with the name <project_name>

<Back to your devmachine>


$ git remote add origin git@github.com:<github_username>/<project_name>.git

$ git remote set-url --add --push origin git@bitbucket.org:<bitbucket_username>/<project_name>.git

$ git remote set-url --add --push origin git@github.com:<github_username>/<project_name>.git

$ git remote -v

origin  git@github.com:<github_username>/<project_name>.git (fetch)
origin  git@bitbucket.org:<bitbucket_username>/<project_name>.git (push)
origin  git@github.com:<github_username>/<project_name>.git (push)

from flask import Blueprint, request, render_template


git = Blueprint('git', __name__, template_folder="templates", 
        static_folder="static", static_url_path="assets")


github_repo = 'https://github.com/makeopensource/github-workshop-2022'
repo_api = 'https://api.github.com/repos/makeopensource/Classic-RPG/pulls'

@git.route("/")
def git_workshop():
    if request.method == 'GET':
        return render_template('git-workshop.html', repo=github_repo, repo_api=repo_api)


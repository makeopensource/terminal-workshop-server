from flask import Blueprint, request, render_template, escape
import os


terminal = Blueprint('terminal', __name__, template_folder="templates", 
        static_folder="static", static_url_path="assets")

@terminal.route("/", methods=['GET', 'POST'])
def terminal_workshop():
    if request.method == 'GET':
        return render_template('website.html')

    else:
        data = request.files['data']
        data = data.stream.read().decode()
        parsed = data.strip().split('\n')
        if len(parsed) == 2:
            submission = f'<b>{escape(parsed[0])}</b><br/>{escape(parsed[1])}'
            with open('workshops/terminal/submissions.txt', 'a') as f:
                f.write(submission + '\n')
            return '200: Successful submission!'
        else:
            return 'file not formatted correctly, please make sure the spacing is correct!'


@terminal.route("/submissions")
def get_submissions():
    with open('workshops/terminal/submissions.txt', 'r') as file:
        submissions = file.readlines()
        retval = ""
        for submission in submissions:
            retval += f'<p>{submission}</p>'

        return retval


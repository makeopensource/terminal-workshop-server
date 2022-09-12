from flask import Flask, request, render_template
import os
import sys

from workshops.terminal.workshop import terminal
from workshops.git.workshop import git

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', workshops=os.listdir("workshops"))

app.register_blueprint(terminal, url_prefix="/terminal")
app.register_blueprint(git, url_prefix="/git")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 5000
    elif len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        raise ValueError("Invalid number of arguments")
    app.run(host='0.0.0.0', port=port)

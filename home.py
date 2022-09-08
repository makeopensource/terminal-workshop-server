from flask import Flask, request, render_template
import os

from workshops.terminal.workshop import terminal

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', workshops=os.listdir("workshops"))

app.register_blueprint(terminal, url_prefix="/terminal")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)

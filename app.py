from flask import Flask, request, render_template
import flask
import time


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('website.html')

    else:
        time.sleep(0.5)
        data = request.files['data']
        data = data.stream.read().decode()
        parsed = data.strip().split('\n')
        if len(parsed) == 2:
            submission = f'<b>{flask.escape(parsed[0])}</b><br/>{flask.escape(parsed[1])}'
            with open('submissions.txt', 'a') as f:
                f.write(submission + '\n')
            return '200: Successful submission!'
        else:
            return 'file not formatted correctly, please make sure the spacing is correct!'


@app.route("/submissions")
def get_submissions():
    with open('submissions.txt', 'r') as file:
        submissions = file.readlines()
        retval = ""
        for submission in submissions:
            retval += f'<p>{submission}</p>'

        return retval


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

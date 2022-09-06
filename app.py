from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        with open('submissions.txt', 'r') as file:
            retval = ""
            for item in file.readlines():
                retval += f'<p>{item}</p>'
            return retval

    else:
        data = request.files['data']
        data = data.stream.read().decode()
        parsed = data.strip().split('\n')
        if len(parsed) == 2:
            submission = f'{parsed[0]} | {parsed[1]}'
            with open('submissions.txt', 'a') as f:
                f.write(submission + '\n')
            return '200: Successful submission!'
        else:
            return 'file not formatted correctly, please make sure the spacing is correct!'


if __name__ == '__main__':
    app.run()

from flask import Flask, request, render_template
import time


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        with open('submissions.txt', 'r') as file:
            submissions = file.readlines()
            return render_template('website.html', submissions=submissions)

    else:
        time.sleep(0.5)
        data = request.files['data']
        data = data.stream.read().decode()
        parsed = data.strip().split('\n')
        if len(parsed) == 2:
            submission = f'Name: {parsed[0]} Hobby: {parsed[1]}'
            with open('submissions.txt', 'a') as f:
                f.write(submission + '\n')
            return '200: Successful submission!'
        else:
            return 'file not formatted correctly, please make sure the spacing is correct!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

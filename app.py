from flask import Flask, request, jsonify
import os

app = Flask(__name__)


def list_dir(dire):
    data = {}
    files = os.listdir(dire)
    for f in files:
        item = f.split('-')
        data[item[0]] = item[1]
    return data


@app.route('/course')
def course():
    return jsonify(os.listdir('course'))


@app.route('/course_dict')
def course_dict():
    return jsonify(list_dir('course'))


@app.route('/course/<int:num>', methods=['GET', 'POST'])
def subject(num):
    if request.method == 'GET':
        fname = list_dir('course')[str(num)]
        with open('./course/{0}-{1}'.format(num, fname), 'r') as file:
            data = file.read()
        return data


@app.route('/exercise')
def exercises():
    return jsonify(os.listdir('exercise'))


@app.route('/exercise_dict')
def exercise_dict():
    return jsonify(list_dir('exercise'))


@app.route('/exercise/<int:num>', methods=['GET', 'POST'])
def exercise(num):
    if request.method == 'GET':
        fname = list_dir('exercise')[str(num)]
        with open('./exercise/{0}-{1}'.format(num, fname), 'r') as file:
            data = file.read()
        return data


if __name__ == '__main__':
    app.run()

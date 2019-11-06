from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'content'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def list_dir(dire):
    data = {}
    files = os.listdir(dire)
    for f in files:
        item = f.split('-')
        it = item[1].split('.')
        data[item[0]] = it[0]
    return data


@app.route('/panel')
def main():
    return render_template('index.html', subjects=list_dir('content/Kurs JS'))


@app.route('/content', methods=['GET', 'POST'])
def content():
    return jsonify(os.listdir('content'))


@app.route('/content/<string:text>', methods=['GET', 'POST'])
def content_item(text):
    if request.method == 'GET':
        return jsonify(list_dir('content/{}'.format(text)))
    elif request.method == 'POST':
        file = request.files['file']
        file_name = request.form['name']
        file_name += '.md'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return render_template('index.html')


@app.route('/content/<string:text>/<string:num>')
def specified_subject(text, num):
    fname = list_dir('content/{}'.format(text))[num]
    with open('content/{}/{}-{}'.format(text, num, fname), 'r') as file:
        data = file.read()
    return data


@app.route('/course_dict')
def course_dict():
    return jsonify(list_dir('content/Kurs JS'))


if __name__ == '__main__':
    app.run()

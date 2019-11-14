from flask import Flask, request, jsonify, render_template, redirect, json
import os

app = Flask(__name__)


def list_dir(dire):
    '''Zwraca zawartość pliku list.json we wskazanym folderze.'''
    f = open('content/{}/list.json'.format(dire), 'r')
    data = json.loads(f.read())
    return data


def sort_files():
    pass


@app.route('/')
def index():
    return render_template('index.html', dirs=os.listdir('content'))


@app.route('/panel', methods=['POST'])
def panel():
    return render_template('panel.html', subjects=list_dir(request.form['index']))


@app.route('/content', methods=['GET', 'POST'])
def content():
    if request.method == 'GET':
        return jsonify(os.listdir('content'))
    elif request.method == 'POST':
        file = request.files['file']
        raw_file_name = request.form['name']
        file_name = raw_file_name + '.md'
        files = os.listdir('content')
        dir_name = files[int(request.form['index']) - 1]
        file.save(os.path.join('content/{}'.format(dir_name), file_name))
        print(request.form['index'])
        return redirect('/')


@app.route('/content/<string:text>')
def content_item(text):
    return jsonify(list_dir(text))


@app.route('/content/<string:text>/<string:num>')
def specified_subject(text, num):
    dire = list_dir(text)
    with open('content/{}/{}.md'.format(text, dire[int(num)]), 'r', encoding='utf8') as file:
        data = file.read()
    return data


if __name__ == '__main__':
    app.run()

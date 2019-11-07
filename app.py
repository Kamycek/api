from flask import Flask, request, jsonify, render_template, redirect
import os

app = Flask(__name__)


def list_dir(dire):
    data = {}
    files = os.listdir(dire)
    for f in files:
        item = f.split('-')
        it = item[1].split('.')
        data[item[0]] = it[0]
    return data


@app.route('/')
def index():
    return render_template('index.html', dirs=os.listdir('content'))


@app.route('/panel', methods=['POST'])
def panel():
    return render_template('panel.html', subjects=list_dir('content/{}'.format(request.form['index'])))


@app.route('/content', methods=['GET', 'POST'])
def content():
    if request.method == 'GET':
        return jsonify(os.listdir('content'))
    elif request.method == 'POST':
        file = request.files['file']
        raw_file_name = request.form['name']
        file_name = '999-' + raw_file_name + '.md'
        files = os.listdir('content')
        dir_name = files[int(request.form['index'])-1]
        subjects = list_dir('content/{}'.format(dir_name))
        subjects_list = list(subjects.values())
        subjects_list.insert(int(request.form['index']), raw_file_name)
        print(subjects_list)
        file.save(os.path.join('content/{}'.format(dir_name), file_name))
        return redirect('/')


@app.route('/content/<string:text>')
def content_item(text):
    return jsonify(list_dir('content/{}'.format(text)))


@app.route('/content/<string:text>/<string:num>')
def specified_subject(text, num):
    fname = list_dir('content/{}'.format(text))[num]
    with open('content/{}/{}-{}.md'.format(text, num, fname), 'r') as file:
        data = file.read()
    return data


if __name__ == '__main__':
    app.run()

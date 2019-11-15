from flask import Flask, request, jsonify, render_template, redirect, json
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024


def list_dir(dire):
    """Zwraca zawartosc pliku list.json we wskazanym folderze jako liste"""
    f = open('content/{}/list.json'.format(dire), 'r')
    data = json.loads(f.read())
    return data


@app.route('/')
def index():
    return render_template('index.html', dirs=os.listdir('content'))


@app.route('/panel', methods=['POST'])
# TODO sprawdzenie poprawnosci argumentu list_dir
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
        dir_name = files[int(request.form['index']) - 1]  # indeks od 0 bo w html jest od 1
        file.save(os.path.join('content/{}'.format(dir_name), file_name))
        print(request.form['index'])
        return render_template('status.html', status="201 Created"), 201


@app.route('/content/<string:text>')
def content_item(text):
    if text in os.listdir('content'):
        return jsonify(list_dir(text))
    else:
        return render_template('status.html', status="404 Not Found"), 404


@app.route('/content/<string:text>/<int:num>')
def specified_subject(text, num):
    if len(list_dir(text)) > num:
        dire = list_dir(text)
        with open('content/{}/{}.md'.format(text, dire[num]), 'r', encoding='utf8') as file:
            data = file.read()
        return data
    else:
        return render_template('status.html', status="404 Not Found"), 404


if __name__ == '__main__':
    app.run()

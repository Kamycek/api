from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/course')
def course():
    return jsonify(os.listdir('./course'))


@app.route('/exercises')
def course():
    return jsonify(os.listdir('./exercises'))


if __name__ == '__main__':
    app.run()

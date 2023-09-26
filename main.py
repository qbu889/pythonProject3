import flask

app = flask.Flask(__name__)  # 实例化类flask


@app.route('/')
def hello():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2023,debug=True)

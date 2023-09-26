import flask

app = flask.Flask(__name__)  # 实例化类flask


@app.route('/blog/<int:ID>')
def show_blog(ID):
    return '我的年龄是是：% d' % ID + '岁！'

@app.route('/rev/<float:NO>')
def revision(NO):
    return '我身上只有：% f' % NO + '元钱了！'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2023, debug=True)

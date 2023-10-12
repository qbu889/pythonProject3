import flask

html_txt = """
<!DOCTYPE html>
<html>
    <body>
        <h2>如果收到了GET请求</h2>
        <form method='post'>
        <input type='submit' value='按下我发送POST请求'/>
        </form>
    </body>
</html>
"""

app = flask.Flask(__name__)  # 实例化类flask


@app.route('/aaa', methods=['GET', 'POST'])
def hello():
    if flask.request.method == 'GET':
        return html_txt
    else:
        return '我司已经收到POST请求！'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2024, debug=True)

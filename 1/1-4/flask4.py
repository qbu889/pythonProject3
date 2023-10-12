from flask import Flask, redirect, url_for

app = Flask(__name__)  # 实例化类flask

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


@app.route('/admin', methods=['GET', 'POST'])
def hello_admin():
    return "您好管理员！"


@app.route('/guest/<guest>', methods=['GET', 'POST'])
def hello_guest(guest):
    return '您好% s ,你是游客' % guest


@app.route('/user/<name>', methods=['GET', 'POST'])
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2025, debug=True)

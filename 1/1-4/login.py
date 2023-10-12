from flask import url_for, request
from werkzeug.utils import redirect

from main import app
@app.route('/success/<name>')
def success(name):
    return '欢迎% s' % name + '登录本系统'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['biaodan']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('biaodan')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)

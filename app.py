from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    output = '<h1>Hello World!</h1>'
    output += '<hr />'
    output += '<p>{}</p>'.format(user_agent)
    return output


@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
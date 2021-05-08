from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'hello to Web Course!'

@app.route('/about')
def about1():
    return 'learn about me!'

@app.route('/hi')
def hi():
 return redirect('/about')

@app.route('/menu')
def errorpage():
 return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()

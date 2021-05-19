from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('cv.html')

@app.route('/assignment8')
def assignment8():
    name = 'Tal'
    hobby = ['to play soccer', 'climb', 'go to a party with friends']
    return render_template('assignment8.html',
                           name=name,
                           hobbies=hobby)

@app.route('/food')
def food():
    name = 'Tal'
    food = ['Pizza', 'Hummos', 'Hamburger']
    return render_template('food.html',
                           name=name,
                           foods=food)


@app.route('/userList')
def contactlist():
    return render_template('Assignment7.html')


if __name__ == '__main__':
    app.run(debug=True)

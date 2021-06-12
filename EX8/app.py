from flask import Flask, render_template, url_for , request , redirect , session ,blueprints ,jsonify
import  mysql, mysql.connector

app = Flask(__name__)
app.secret_key = '123'
users =   [{"userName":"talosh","firstName": "Tal","lastName":"Bracha", "email": "talbracha123@gmai.com"},
            {"userName":"avosh","firstName": "Avi", "lastName": "Nimni", "email": "avinimni123@gmai.com"},
            {"userName":"itizikosh","firstName": "Itzik", "lastName": "Zohar", "email": "itzikzohar123@gmai.com"},
            {"userName":"elosh","firstName": "Eli", "lastName": "Ohana", "email": "eliohana123@gmai.com"},
            {"userName":"leosh","firstName": "Leo", "lastName": "Messi", "email": "leomessi@gmai.com"},
           {"userName": "yoni", "firstName": "yoni", "lastName": "Abuksis", "email": "yoni@gmai.com"},
           {"userName": "rafi", "firstName": "rafi", "lastName": "Ohana", "email": "rafi@gmai.com"},
           {"userName": "ben", "firstName": "beni", "lastName": "Cohen", "email": "leomessi@gmai.com"},
            {"userName":"yossosh","firstName": "Yossi", "lastName": "Bracha", "email": "yossibracha123@gmai.com"},
            {"userName":"lucasosh","firstName": "Lucas", "lastName": "Podolsky", "email": "lucaspodolsky@gmai.com"}]

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='d6sktfTh',
                                         database='assignment10_schema')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

@app.route('/')
def hello_world():
    return render_template('cv.html')

# -----EX11--------#
@app.route('/assignment11/users')
def assignment11():
    current_method = request.method
    if current_method == 'GET':
        query = "SELECT * FROM assignment10_schema.users;"
        query_result = interact_db(query=query, query_type='fetch')
        response = {}
        if len(query_result) != 0:
            response = query_result
        response = jsonify(users=response)
        return response
    else:
        return jsonify(users)

@app.route('/assignment11/users/selected/id/', defaults={'SOME_USER_ID':3})
@app.route('/assignment11/users/selected/id/<int:SOME_USER_ID>')
def get_user(SOME_USER_ID=None):
    if SOME_USER_ID:
        query = "SELECT * FROM assignment10_schema.users WHERE id='%s'" % SOME_USER_ID
        query_result = interact_db(query, query_type='fetch')
        if len(query_result) != 0:
            return jsonify(users=query_result)
    return jsonify({'success': False,
                    'error': 'this Id is not appear in DB'
                    })
from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route('/assignment8')
def assignment8():
    name = ''
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

@app.route('/assignment9' , methods = ['GET','DELETE','POST','PUY'])
def ex_9func():
    current_method = request.method
    if current_method == 'GET':
            if 'userName' in request.args:
                userName = request.args['userName']
                if userName is '':
                    return render_template('assignment9.html', search=True, users=users)
                searchuser=[]
                for user in users:
                    if (userName is '' or user['userName'] == userName):
                     searchuser.append(user)
                if len(searchuser) != 0:
                    return render_template('assignment9.html',search=True, haveUser=True, user=searchuser)
                else:
                    return render_template('assignment9.html', haveUser=False, search=True)
            else:
                 return render_template('assignment9.html')
    else:
        if request.form['userName'] not in users:
            users.append({'userName': request.form['userName'],
                          'firstName': request.form['firstName'],
                          'lastName': request.form['lastName'],
                          'email': request.form['email']})
            session['userName'] = request.form['userName']
            session['firstName'] = request.form['firstName']
            session['lastName'] = request.form['lastName']
            session['email'] = request.form['email']
            session['login'] = True
            return render_template('assignment9.html')
        else:
            session['userName'] = request.form['userName']
            session['firstName'] = request.form['firstName']
            session['lastName'] = request.form['lastName']
            session['email'] = request.form['email']
            session['login'] = True
            return render_template('assignment9.html')


@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    session['login'] = False
    return redirect('assignment9')


if __name__ == '__main__':
    app.run(debug=True)

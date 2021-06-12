from flask import Flask, render_template, url_for, session, request, redirect, Blueprint , flash

app = Flask(__name__)
app.secret_key = "123"

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/assignment10',
    template_folder='templates'
)

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


@assignment10.route('/assignment10')
@assignment10.route('/users')
def users():
    query = "select * from assignment10_schema.users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insertUser', methods=['GET','POST'])
def insertUsers():
    if request.method == 'POST':
        userName = request.form['firstName']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        check_input = "SELECT userName FROM assignment10_schema.users WHERE userName='%s';" % userName
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into assignment10_schema.users(userName, firstName ,lastName, email)\
                            value ('%s', '%s', '%s','%s');" % (userName,firstName ,lastName, email)
            interact_db(query=query, query_type='commit')
            flash('added successfully!')
            return redirect('/users')
        else:
            flash('this user name is already registered')
            return redirect('/users')
    return render_template('assignment10.html', req_method=request.method)



@assignment10.route('/deleteUser', methods=['POST'])
def deleteUsers():
    userId = request.form['id']
    check = "SELECT userName FROM assignment10_schema.users WHERE id='%s';" % userId
    answer = interact_db(query=check, query_type='fetch')
    if len(answer) > 0:
        query = "delete from assignment10_schema.users where id='%s';" % userId
        interact_db(query=query, query_type='commit')
        flash('The user is deleted from DB ')
        return redirect('/users')
    else:
        flash('Invalid input - this ID is not in DB')
        return redirect('/users')


@assignment10.route('/updateUser', methods=['GET','POST'])
def updateUsers():
        id = request.form['id']
        username = request.form['userName']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        email = request.form['email']
        query = " UPDATE assignment10_schema.users SET userName='%s',firstName='%s' ,lastName='%s', email='%s' WHERE id='%s';"%\
                (username, firstname, lastname, email, id)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
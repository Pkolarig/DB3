from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

#==Welcome Page==#

@app.route("/")
def hello():
	return render_template('page1.html')

#==Log in as Staff==#

@app.route("/staff_log_in")
def hello():
	return render_template('staff_log_in.html')

#==Movie==#
@app.route('/s_movie')
def showmovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Movie ORDER BY MovieName")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('/movie/list.html', users=users)


#==Genre==#

#==Showings==#

#==Attend==#

#==Room==#

#==Customer==#






#==Log in as Customer==#

@app.route("/cust_log_in")
def hello():
	return render_template('cust_log_in.html')




@app.route("/")
def hello():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Customer")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('users.html',users=users)

@app.route('/movie')
def showmovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Movie ORDER BY MovieName")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('/movie/list.html', users=users)


@app.route('/entername')
def helloName(name=None):
    return render_template('form.html', name=name)

@app.route('/submit', methods=["POST"])
def submit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Customer (firstname, lastname) "
        "VALUES (%s, %s)"
    )
    data = (request.form['firstname'], request.form['lastname'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('index.html', firstname=request.form['firstname'], lastname=request.form['lastname'])

@app.route('/sqlInjection')
def sqlInjection(name=None):
    return render_template('form2.html')

@app.route('/submitSqlInjection', methods=["POST"])
def sqlInjectionResult():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    firstName = request.form['firstname']
    query = ("SELECT * from Customer where firstname = '" + firstName + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

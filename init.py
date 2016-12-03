from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

#Welcome Page

@app.route("/")
def hello():
	return render_template('Page1.html')

#Log in as Staff

@app.route("/staff_log_in")
def staff_log_in():
	return render_template('staff_log_in.html')

#MOVIE

#LIST
@app.route('/movie')
def showmovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Movie ORDER BY MovieName")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('/movie/list.html', users=users)

#ADD
@app.route("/movie/add")
def movielist():
	return render_template('/movie/add.html')


@app.route('/addmovie', methods=["GET","POST"])
def addmovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_movie= (
        "INSERT INTO Movie (idMovie, MovieName, MovieYear) "
        "VALUES (%s, %s, %s)"
    )
    data = (request.form['idMovie'], request.form['MovieName'], request.form['MovieYear'])
    

    try:
        cursor.execute(insert_movie, data)
        cnx.commit()
        cursor.close()
        cnx.close()
        return render_template('/movie/success.html')

    except:
        
        return render_template('fail.html')

#MODIFY
@app.route('/movie/modifyselect', methods=["POST"])
def modify_select():
    id = request.args.get('id')
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()    
    sql = "SELECT * FROM `Movie` WHERE idMovie = %s;"
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    return render_template("/movie/modify.htm", id=id, MovieYear=result[0][2], MovieName=result[0][1])


@app.route('/movie/modify', methods=["GET","POST"])
def modifymovie():
    id = request.args.get('id')
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query= (
        "UPDATE Movie SET MovieName =%s, MovieYear = %s where idMovie = %s;"
    )
    data = (request.form['MovieName'], request.form['MovieYear'],id,)
    cursor.execute(query, data)
    cnx.commit()
    cnx.close()
    return render_template('/movie/success.html')

#DELETE

@app.route('/movie/delete', methods=["GET","POST"])
def del_movie():
    id = request.args.get('id')
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM Movie WHERE idMovie = %s;"
    )
    data = (id,)
    cursor.execute(delete_stmt, data)
    print (cursor._executed)
    cnx.commit()
    cnx.close()
    return render_template('/movie/success.html')


############GENRE

#ADD

@app.route("/genre/add")
def genrelist():
	return render_template('/genre/add.html')


@app.route('/addgenre', methods=["GET","POST"])
def addgenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_genre= (
        "INSERT INTO Genre (Genre, Movie_idMovie) "
        "VALUES (%s, %s)"
    )
    data = (request.form['Genre'], request.form['Movie_idMovie'])
    

    try:
        cursor.execute(insert_genre, data)
        cnx.commit()
        cursor.close()
        cnx.close()
        return render_template('/genre/success.html')

    except:
        
        return render_template('fail.html')

#LIST

@app.route('/genre')
def showmoviegenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT Genre, MovieName from Genre, Movie WHERE Genre.Movie_IDMovie = Movie.idMovie ORDER BY Genre")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('/genre/list.html', users=users)

#DELETE

@app.route('/genre/delete', methods=["GET","POST"])
def del_genre():
    id = request.args.get('id')
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM Genre WHERE Genre= %s and Movie_idMovie=%s;"
    )
    data = (id)
    cursor.execute(delete_stmt, data)
    print (cursor._executed)
    cnx.commit()
    cnx.close()
    return render_template('/genre/success.html')








#==Log in as Customer

@app.route("/cust_log_in")
def cust_log_in():
	return render_template('cust_log_in.html')


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

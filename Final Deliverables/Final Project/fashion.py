from flask import Flask,render_template,request,redirect,url_for,session
import ibm_db
import re

app=Flask(__name__)
app.secret_key='a'
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ktb49368;PWD=clKwviKTgdS7EdbM",'','')
@app.route('/')
def login():
	return render_template('Login.html')
@app.route('/login', methods=[ "GET", "POST"])
def loginframe():
	global userid
	msg=''
	if request.method == "POST":
		username=request.form.get("username")
		password=request.form.get("password")
		sql="SELECT * FROM users WHERE USERNAME=? AND PASSWORD=?"
		stmt=ibm_db.prepare(conn,sql)
		ibm_db.bind_param(stmt,1,username)
		ibm_db.bind_param(stmt,2,password)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			session['loggedin']=True
			session['id']=account['USERNAME']
			userid=account['USERNAME']
			session['username']=account['USERNAME']
			msg="logged in suceccfully"
			return render_template('Home-Page.html')
		else:
			return render_template('loginfailure.html')
	return render_template('Login.html')
@app.route('/registerpage')
def registerpage():
	return render_template('registers.html')
@app.route('/register', methods=['GET','POST'])
def registers():
	if request.method== "POST":
		username=request.form.get("username")
		email1=request.form.get("email")
		password=request.form.get("password")
		sql="SELECT * FROM users WHERE USERNAME=?"
		stmt=stmt=ibm_db.prepare(conn,sql)
		ibm_db.bind_param(stmt,1,username)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		if account:
			return render_template('usernamefailure.html')
		elif not re.match(r'[^@]+@[^@]+\.[^@]+',email1):
			return render_template(emailfailure.html)
		elif not re.match(r'[A-Za-z0-9]+',password):
			return render_template('passwordfailure.html')
		else:
			insert_sql="INSERT INTO users VALUES(?,?,?)"
			prep_stmt=ibm_db.prepare(conn,insert_sql)
			ibm_db.bind_param(prep_stmt,1,username)
			ibm_db.bind_param(prep_stmt,2,password)
			ibm_db.bind_param(prep_stmt,3,email1)
			ibm_db.execute(prep_stmt)
			return render_template('registersuccessfully.html')
	return render_template('registers.html')
		
@app.route('/category')
def category():
    return render_template('Category-Page.html')

@app.route('/Men')
def men():
    return render_template('men.html')

@app.route('/Women')
def women():
    return render_template('women.html')

if __name__=='__main__':
    app.run(debug=True, port=9000)
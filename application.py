from flask import Flask, render_template, request, redirect, url_for,flash,session
import os
import resumeMatcher
import validate2
import getuserdata

# UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'zip'}

application = app = Flask(__name__)
app.secret_key =os.urandom(12)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		return render_template('home.html',imgurl=getuserdata.getmasterimage(session['email']))
	 
@app.route('/fileUpload.html')
def upload():
    if not session.get('logged_in'):
	    return render_template("fileUpload.html")
    else:
        return render_template("fileUpload.html")

@app.route('/index.html')
# @exception_handler
def indexRedirect():
    return render_template("index.html")

@app.route('/logout')
# @exception_handler
def logout():
    session['logged_in'] = False
    session.clear()
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/services.html')
def services():
    return render_template("services.html")

@app.route('/userdata.html')
def userdata():
    if session.get('logged_in'):
        namelist = getuserdata.resumename(session['email'])
        return render_template("userdata.html",namelist=namelist,len = len(namelist))

@app.route('/feedback.html')
def feedback():
    return render_template("feedback.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/file', methods=['GET', 'POST'])
def handleFileUpload():
    if request.method == "POST":
    	file=request.files['uploadResume']
    	email=request.form['email']
    	if file.filename != '':
    		filePath=os.path.join('./UploadedResume',file.filename)
    		file.save(filePath)
    	if len(email)>0:
    		resumeMatcher.process(filePath,email)

    flash("Email Has been sent!")      
    return render_template('index.html')

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    email = request.form['email']
    password = request.form['pass']
    if validate2.init(email,password):
        session['email'] = email
        session['logged_in'] = True
        imgurl= getuserdata.getmasterimage(email)
        return render_template("home.html",imgurl=imgurl)
    else:
	    return render_template("index.html")
if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.run(debug=True)

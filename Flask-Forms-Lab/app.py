from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
	

username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]



@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
		return 'You just made a GET request!'
	else:
		name = request.form['username']
		password = request.form['password']

		return redirect(url_for('home',u = username,p = password))


@app.route('/home')
def home():
	return render_template('home.html', friends= facebook_friends)


@app.route('/friends_exists/Fouad', methods=['GET', 'POST'])
def friends_exists():
	return render_template('friend_exists.html',friend=facebook_friends,no_friends=False)
if __name__ == "__main__":  
	app.run(debug=True)


  		




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)


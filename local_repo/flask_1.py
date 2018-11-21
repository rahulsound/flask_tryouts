from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
	#return '<h1> Hello World! </h1>'
	#response = make_response('<h1> This document contains a cookie!</h1>')
	#response.set_cookie('answer', '42')
	#return response
	return redirect('http://127.0.0.1:5000/browser')
	
@app.route('/user/<name>')
def user(name):
	return'<h1> Hello , %s! </h1>' %name
	
@app.route('/browser')
def index1():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello 404, %s</h1>' % user.name
 
if __name__ == '__main__':
	app.run(debug=True)
	
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
   name = "Hello World"
   return name

@app.route('/check/<username>/profile')
def _test(test):
	return render_template('profile.html')
	# return test

@app.route('/check2/')
def _test2():	
	query = request.args.get('q')
	return "done!"

@app.route('/good', methods=['POST'])
def good():
	return str(request.form['name'])

if __name__ == "__main__":
   app.run(debug=True)

# http://localhost:5000/check2/?q=asdf
# http://localhost:5000/check/asdf
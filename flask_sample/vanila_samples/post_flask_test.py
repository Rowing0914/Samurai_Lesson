from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
   name = "Hello World"
   return name

@app.route('/post', methods=['POST'])
def good():
	name = request.form['name']
	print(name)
	return "Hello " + str(name)

@app.route('/test')
def test():
	return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True, host = "0.0.0.0")
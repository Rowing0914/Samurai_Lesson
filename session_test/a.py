from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/<name>')
def index(name):
	# print(name)
	return name
	# return redirect('https://google.com', code=302)
	# return render_template('https://google.com')

@app.route('/test')
def test():
	return request.args.get('name')

if __name__ == '__main__':
    app.run(debug=True)
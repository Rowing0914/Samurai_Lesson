from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
from mail import create_message, send

# for flask app
app = Flask(__name__)
app.secret_key = 'norio'

@app.route("/test")
def test():
	to_addr = 'kosakaboat@gmail.com'
	subject = 'test'
	body = 'test'

	msg = create_message(to_addr, subject, body)
	send(to_addr, msg)
	return "Sent"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if form.validate() == False:
		flash('All fields are required.')
		return render_template('contact.html', form=form)
	else:
		print(request.form['email'])
		msg = create_message(request.form['email'], "Thank you for your applying", str(request.form))
		send(msg)
		return render_template('success.html')

if __name__ == '__main__':
	app.run(debug=True)
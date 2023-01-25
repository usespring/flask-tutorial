from flask import Flask, render_template
from forms import ContactForm # pip install flask-WTF

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact')
def contact():
   form = ContactForm()
   return render_template('/etf/contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)
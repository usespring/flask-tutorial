from flask import Flask, redirect, url_for, render_template, request, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "feyr6eehgdterhsdhfrwsg"


@app.route('/')
def index():
    return render_template('/layout/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            "flash(message, category)"
            "message parameter is the actual message to be flashed."
            "category parameter is optional. It can be either ‘error’, ‘info’ or ‘warning’."
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('/layout/login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)

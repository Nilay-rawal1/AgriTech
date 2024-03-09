from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/crop')
def crop():
    return render_template('Crop.html')

@app.route("/home", endpoint="home()")
def home():
    return render_template('home.html')

@app.route("/team", endpoint="team()")
def team():
    return render_template('team.html')


@app.route("/login", endpoint="login()")
def login():
    return render_template('login.html')

@app.route("/services", endpoint="services()")
def services():
    return render_template('services.html')

@app.route("/weather", endpoint="weather()")
def services():
    return render_template('weather.html')

@app.route("/404", endpoint="e404()")
def e404():
    return render_template('404.html')

@app.route('/auth', endpoint="auth()", methods=['POST'])
def auth():
    email = request.form['Login-Email']
    password = request.form['Login-Password']
    
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return redirect(url_for('success'))
        # return jsonify({'success': True})
    else:
        return jsonify({'success': False,  # Handle this JSON response on client-side in JS for invalid login
                        'message': 'Invalid email or password. Please try again.'})

@app.route('/register', methods=['POST'])
def signup():
    email = request.form['Register-Email']
    password = request.form['Register-Password']
    
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'success': False, # Handle this JSON response on client-side in JS for existing user
                        'message': 'User already exists. Please log in.'})
    else:
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('home.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

#TODO authentication with database
#current one is a dummy for backend test
def authenticate(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False

@app.route('/success')
def success():
    return render_template('404.html') # route this to whatever page you want to

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if authenticate(username, password):
        return redirect(url_for('success'))
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

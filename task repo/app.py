from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2.ext import debug

app = Flask(__name__, template_folder='template', static_folder='static')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route for the first page
@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/')
def index():
    return render_template('index.html')

# Route for the second page
@app.route('/page2')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=67500,debug= True)

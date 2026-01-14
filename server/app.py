import os
from flask import Flask
from flask_migrate import Migrate

try:
    # Try relative import first (when running from server directory)
    from models import db
except ImportError:
    # Fall back to absolute import (when running from project root)
    from server.models import db

app = Flask(__name__)
# Use absolute path to the database in server directory
db_path = os.path.join(os.path.dirname(__file__), 'instance', 'app.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

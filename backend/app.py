from flask import Flask
from config import config
from models import db
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CORS(app)

from routes import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)// Test comment

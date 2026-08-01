from flask import Flask
from flask_cors import CORS

from routes import api
from database import engine
from models import Base

app = Flask(__name__)


CORS(app)

# Register Blueprint
app.register_blueprint(api)

# Create Database Tables
Base.metadata.create_all(bind=engine)


@app.route("/")
def home():
    return {
        "project": "RecruitFlow Intelligence Engine",
        "status": "Backend Running Successfully"
    }


if __name__ == "__main__":
    app.run(debug=True)
from app import app
from populate_db import populate_database

if __name__ == '__main__':
    populate_database(app)
    app.run(debug=True)

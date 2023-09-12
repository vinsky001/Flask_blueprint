from flask import Flask
from extensions import db 

#Create an app
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.sqlite3'
    
    db.init_app(app)
    
    return app 

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from extensions import db  # Import db here as well
        db.create_all()
    app.run()


from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Set configuration variables (e.g., secret key)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a secure key in production

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Initialize other extensions here (e.g., database, login manager)
    
    return app

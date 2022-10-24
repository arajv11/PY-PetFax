from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import facts_create
    app.register_blueprint(facts_create.bp)

    # return the app
    return app
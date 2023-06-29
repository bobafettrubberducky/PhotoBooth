from flask_app import app

# import flask_app.controllers and registered in  Flask application
import flask_app.controllers.user_controller
import flask_app.controllers.upload_controller
import flask_app.controllers.gallery_controller

if __name__ == "__main__":
    app.run(debug=True, port=5005)

from flask import request, render_template, redirect, flash, session, send_from_directory, abort, jsonify, url_for, session

from flask_app import app

from flask_app.models.file import File

@app.route("/gallery", methods=["GET"])
def gallery_view():
    user_id = session["user_id"]
    images = File.get_all(user_id)
    return render_template("gallery/view.html", images=images)


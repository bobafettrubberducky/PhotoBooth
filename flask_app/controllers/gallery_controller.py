from flask import request, render_template, redirect, flash, session, send_from_directory, abort, jsonify, url_for, session

from flask_app import app

from flask_app.models.file import File

from flask_app.utilities import delete_image_file


@app.route("/gallery", methods=["GET"])
def gallery_view():
    
    #& STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')
    
    user_id = session["user_id"]
    images = File.get_all(user_id)
    return render_template("gallery/view.html", images=images)


#! DELETE FILE in gallery 
@app.route("/delete/<int:id>", methods=["POST"])
def delete_file(id):

    #& STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')
    
    file = File.get_by_id(id)
    if not file:
        flash("File not found", "error")
        return redirect("/gallery")
    
    file_name = file.file_name
    
    File.destroy_file(id)

    delete_image_file(file_name)

    flash("File deleted successfully!", "success")
    return redirect("/gallery")

    


from flask import request, render_template, redirect, flash, session, send_from_directory, abort, jsonify, url_for, session
from flask_app import app
from flask_app.models.user import User

import os
import uuid

from flask_app.utilities import save_profile_pic, delete_profile_pic,save_gallery_image

@app.route('/uploads/<filename>') #/uploads/filename.png with filename = "filename.png"
def serve_uploads(filename):

    # STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')
    
    return send_from_directory(app.config["UPLOAD_DIR"], filename)

# Upload Profile Pics 
@app.route('/set-profile-pic', methods=['GET'])
def show_profile_pic():

    # STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')
    
    user = User.get_by_id({"id": session["user_id"]})
    return render_template("uploads/set-profile-pic.html", user=user)

@app.route('/set-profile-pic', methods=['POST'])
def show_profile_uploads():

    # STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')
    
    file = request.files["my_file"] # file has methods and attributes like file.filename, file.save 
    save_profile_pic(file,session["user_id"])
    flash("Your profile pic has been updated!", "success")
    return redirect('/set-profile-pic')

@app.route('/delete-profile-pic', methods=['POST'])
def delete_profile_uploads():
    
    # STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')
    
    delete_profile_pic(session["user_id"])
    flash("Your profile pic has been deleted!", "success")
    return redirect('/set-profile-pic')


#! Upload Gallery Pics
@app.route('/uploads', methods=['GET'])
def upload_image():

    # STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')
    
    return render_template("gallery/uploads.html")

@app.route('/uploads/gallery', methods=['POST'])
def store_image():

    # STEP 0A - check if user_id in session 
    if 'user_id' not in session:
        return redirect ('/logout')

    file = request.files["my_file"]
    title = request.form["title"]
    description = request.form["description"]
    save_gallery_image(file,session["user_id"],title,description)
    flash("Gallery Image uploaded!", "success")
    return render_template("gallery/uploads.html")


from flask import session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.file import File


import os
import uuid

# Upload Files function 
def save_profile_pic(file, user_id):

    delete_profile_pic(user_id) # delete the profile pic first before uploading a new one

    file_extension = os.path.splitext(file.filename)[1] # get the file extension (.png for ex) (note .splitext returns a tuple)
    unique_string = uuid.uuid4().hex # generate hex a unique string (hex is a string of 32 characters)
    file_name = unique_string + file_extension # concatenate the unique string and the file extension

    # print(app.config["UPLOAD_DIR"]) # check the path instance/uploads printed in terminal

    file.save(os.path.join(app.config["UPLOAD_DIR"], file_name))
    # store the file to the path to instance/uploads/asd234werasdf.png
    # os.path.join(app.config["UPLOAD_DIR"] =  instance/uploads/asd234werasdf.png

    User.set_profile_pic({
        "id": session["user_id"],
        "profile_pic": file_name
    })

    return True

# Delete Profile Pic function
def delete_profile_pic(user_id):

    #! Delete the file from the path instance/uploads/asdfasdf.png

    user = User.get_by_id({"id": user_id}) # get the user by id

    #* Check if user trying to delete doesn't have a profile pic then return False
    #* Prevents error if user does not have a profile pic
    if not user.profile_pic:
        return False
    
    file_path = os.path.join(app.config["UPLOAD_DIR"], user.profile_pic)
    #file_path =  instance/uploads/asdfasdf.png

    #* Check if file exists then delete it from the path instance/uploads/asdfasdf.png
    #*  Prevents error if file does not exist
    if os.path.exists(file_path):
        os.remove(file_path)
        # os.remove = delete the file from the path instance/uploads/asdfasdf.png

    #! Delete from database at profile_pic column: asdfasdf.png is file name
    User.set_profile_pic({
        "id": session["user_id"],
        "profile_pic": "",
    })

    return True


def save_gallery_image (file, user_id, title, description):
    file_extension = os.path.splitext(file.filename)[1] 
    unique_string = uuid.uuid4().hex 
    file_name = unique_string + file_extension
    file_new_path = os.path.join(app.config["UPLOAD_DIR"], file_name) 
    #var/v1/instance/uploads/asdf123sdq.png
    file.save(file_new_path)

    File.save ({
        "file_name": file_name,
        "title": title,
        "description": description,
        "extension": file_extension,
        "size": os.stat(file_new_path).st_size, # get the size of the file
        "user_id": user_id
    })


    return True

#! Delete file from the instance/uploads path when photo deleted in /gallery
def delete_image_file(file_name):
    file_path = os.path.join(app.config["UPLOAD_DIR"], file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False


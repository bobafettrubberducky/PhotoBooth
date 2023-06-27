from flask import Flask
import os

app = Flask(__name__)
app.secret_key="your_mama"

#building a path for our file user/file/uploads
app.config["UPLOAD_DIR"] = os.path.join(app.instance_path,"uploads")
# app.instance_path - user/file/instance, give the path to the instance folder
# os.path.join - join the path to the instance folder with uploads folder
# app.config["UPLOAD_DIR"] = user/file/instance/uploads, app.config like dictionary key that can access by app.config["UPLOAD_DIR"]

#if path exist okay (exist_ok=True) but not then create the path directory /instance/uploads on the user computer
os.makedirs(app.config["UPLOAD_DIR"], exist_ok=True)

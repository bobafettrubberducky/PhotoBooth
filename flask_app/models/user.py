from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "gallery"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.user_name = data["user_name"]
        self.profile_pic = data["profile_pic"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.files = []

    @staticmethod
    def validate_register(user):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(User.DB).query_db(query,user)

        is_valid = True
        if len(result) >= 1:
            flash("Email already taken")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email!')
            is_valid = False
        if len(user["first_name"]) < 2:
            flash("First name must be at least 2 characters")
            is_valid = False
        if len(user["last_name"]) < 2:
            flash("Last name must be at least 2 characters")
            is_valid = False
        if len(user["user_name"]) < 2:
            flash("User name must be at least 2 characters")
            is_valid = False
        if len(user["password"]) < 8:
            flash("PASSWORD must be at least 8 characters")
            is_valid = False
        if user["password"] != user["confirm"]:
            flash("Passwords don't match")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,user_name,email,password,profile_pic) VALUES(%(first_name)s,%(last_name)s,%(user_name)s,%(email)s,%(password)s,%(profile_pic)s);"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        if len(result) <1:
            return False
        return cls(result[0])
    
    @classmethod
    def set_profile_pic(cls,data):
        query = "UPDATE users SET profile_pic=%(profile_pic)s WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return cls(result[0])

    

    

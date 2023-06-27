from flask_app.config.mysqlconnection import connectToMySQL

class File:
    DB = "gallery"
    def __init__(self,file_dict):
        self.id = file_dict["id"]
        self.title = file_dict["title"]
        self.description = file_dict["description"]
        self.file_name = file_dict["file_name"]
        self.size = file_dict["size"]
        self.extension = file_dict["extension"]
        self.user_id = file_dict["user_id"]
        self.created_at = file_dict["created_at"]
        self.updated_at = file_dict["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO files (file_name, title, description, size, extension, user_id) VALUES (%(file_name)s, %(title)s, %(description)s, %(size)s, %(extension)s, %(user_id)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result


    @classmethod
    def get_all(cls,user_id):
        query = "SELECT * FROM files WHERE user_id = %(user_id)s;"
        data = {
            "user_id": user_id
        }
        results = connectToMySQL(cls.DB).query_db(query,data)
        files = []
        for file in results:
            files.append(cls(file))
        return files
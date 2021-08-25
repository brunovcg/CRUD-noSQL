from datetime import datetime
import pymongo
from app.models.post_model import Post


client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


def list_posts():
    
    post_list = list(db.posts.find())

    if post_list != []:

        for post in post_list:
           post.pop("_id")
           

    return post_list


def id_generator():

    post_list = list_posts()

    if len(post_list) < 1:
        my_id = 1
    else:
        my_id = max([item["id"] for item in post_list])+1

    return my_id


def add_post(*args):

    next_id = id_generator()

    new_entry = Post(next_id,*args).__dict__
    
    db.posts.insert_one(new_entry)

    return new_entry


def del_post(id):

    post_list = list_posts()

    id_list = [item["id"] for item in post_list]

    if not id in id_list:
        return False

    db.posts.delete_one({"id":id})

    return True

def upd_post(id, *args):

    post_list = list_posts()

    time_now = datetime.utcnow()

    id_list = [item["id"] for item in post_list]

    if not id in id_list:
        return False

    db.posts.update_one({"id":id})

    return True



    return ...

def get_one_post(id):

    post = db.posts.find_one({"id":id})

    if not post:
        return "Not found"

    post.pop("_id")

    return post

def get_many_posts():
    all_posts = list_posts()
    return all_posts



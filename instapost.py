def instapost(username, password, path,  caption):
    
    from instagrapi import Client
    cs=Client()
    cs.login("username", "password")
    cs.photo_upload(r"path", "caption")


instapost("username", "password", "path", "caption")

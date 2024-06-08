import requests

class Post:
    def __init__(self) -> None:
        response = requests.api.get(url='https://api.npoint.io/c790b4d5cab58020d391')
        self.all_posts = response.json()
        self.count = 0
        
    def get_title(self):
        post_title = self.all_posts[self.count].get('title')
        return post_title
    
    def get_subtitle(self):
        post_subtitle = self.all_posts[self.count].get('subtitle')
        self.count+=1
        return post_subtitle
    
    def get_blog(self,number):
        blog = self.all_posts[number-1]
        return blog
    
    def get_blog_collection(self):
        return self.all_posts
_author_ = 'Ta-Seen Junaid'

import uuid
import datetime
from src.models.post import Post
from src.common.database import Database

class Blog(object):
    def _init__(self, author, title, description, author_id, id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if id is None else id

    def new_post(self, title, content, date = datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(colllection='blogs',
                        data=self.json())


    def json(self):
        return {
            'author': self.author,
            'author_id': self.author_id,
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }


    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(colllection='blogs',
                                      query={'_id': id})
        return cls(**blog_data)


    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find(colllection='blogs',query={'author_id':author_id})

        return [cls(**blog) for blog in blogs]


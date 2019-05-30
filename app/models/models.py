from sqlalchemy import Column,String
from sqlalchemy import Integer
from .base import db

class Admin(db.Model):
    __tablename__ = 'admin'

    id = Column(Integer,primary_key=True)
    username = Column(String(20))
    password_hash = Column(String(128))
    blog_title = Column(String(60))
    blog_sub_title = Column(String(100))
    name = Column(String(30))
    about = Column(db.Text)  

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer,primary_key=True)
    name = Column(String(30),unique=True)
    posts = db.relationship('Post',back_populates='post')

from datetime import datetime
class Post(db.Model):
    __tablename__ = 'post'
    __table_args__ = (
        db.PrimaryKeyConstraint('id'),
    )

    id = Column(Integer,primery_key=True)
    title = Column(String(60))
    body = Column(db.Text)
    timestamp = Column(db.DateTime,default=datetime.utcnow)
    category_id = Column(Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',back_populates='posts')   #分类和文章一对多关系，集合关系属性'post'
    comments = db.relationship('Comment', back_populates='post', cascade='all, delete-orphan') #每篇文章多个评论

class Comment(db.Model):
    id = Column(Integer,primary_key=True)
    author = Column(String(30))
    email = Column(String(254))
    site = Column(String(255))
    body = Column(db.Text)
    from_admin = Column(db.Boolean,default=False)
    reviewed = Column(db.Boolean,default=False)
    timestamp = Column(db.DateTime,default=datetime.utcnow,index=True)
    post_id = Column(Integer,db.ForeignKey('post.id'))  #存储Post记录的主键置
    post = db.relationship('Post',back_populates='comments')
    replied_id = Column(Integer,db.ForeignKey('comment.id'))    #设置评论的回复的自身外键指向自身的id
    replied = db.relationship('Comment',back_populates='replies',remote_side=[id])
    replies = db.relationship('Comment',back_populates='replied',cascade='all')
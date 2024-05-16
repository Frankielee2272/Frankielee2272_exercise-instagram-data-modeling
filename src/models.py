from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    posts = relationship('Post', backref='user')
    comments = relationship('Comment', backref='user')
    followers = relationship('Follower', backref='user')

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    image_url = Column(String(255), nullable=False)
    caption = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    comments = relationship('Comment', backref='post')

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    text = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    follower_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    follower_user_id = Column(Integer, ForeignKey('user.user_id'))

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    posts = relationship("Post", backref = "user")
    followers = relationship("Follower", backref = "user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_text = Column(String(250), nullable=False)
    user = Column(Integer, ForeignKey("user.id"))
    comments = relationship("Comment", backref = "post")
    reactions = relationship("Reaction", backref = "post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    post = Column(Integer, ForeignKey("post.id"))
    

class Reaction(Base):
    __tablename__ = 'reaction'
    id = Column(Integer, primary_key=True)
    reaction_type = Column(String(250), nullable=False)
    post = Column(Integer, ForeignKey("post.id"))


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    following = Column(Integer, ForeignKey("user.id"))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

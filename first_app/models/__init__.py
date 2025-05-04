__all__ = [
    'PostAuthor',
    'BlogPost',
    'Comment', 
    'ContactUs',
    'TimeStampModel',
    'UserLogin',
    'User',
    'Customer',
    'Staff'
]

from first_app.models.blog import PostAuthor, BlogPost, Comment, ContactUs
from first_app.models.abstract_model import TimeStampModel, UserLogin
from first_app.models.inheritance import User, Customer, Staff
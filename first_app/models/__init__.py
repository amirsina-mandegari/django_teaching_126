__all__ = [
    'PostAuthor',
    'BlogPost',
    'Comment', 
    'ContactUs',
    'TimeStampModel',
    'UserLogin',
    'CustomUser',
    'Customer',
    'Staff',
    'Book',
    'PublishedBook'
]

from first_app.models.blog import PostAuthor, BlogPost, Comment, ContactUs
from first_app.models.abstract_model import TimeStampModel, UserLogin
from first_app.models.inheritance import CustomUser, Customer, Staff
from first_app.models.proxy_models import Book, PublishedBook
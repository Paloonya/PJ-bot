from sqlalchemy import Column, Integer, String, Text

from .db import db


class Questions(db.Model):
    id = Column(Integer, primary_key=True)
    ques = Column(
        Text,
        nullable=False,
        unique=True,
        default="",
        server_default="",
    )
    topic = Column(
        String,
        nullable=False,
        default="",
        server_default="",
    )
    pic = Column(
        String,
        nullable=True,
        default="",
        server_default="",
    )
    description = Column(Text, nullable=False, default="", server_default="")

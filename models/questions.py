from sqlalchemy import Column, Integer, String, Text

from .db import db


class Questions(db.Model):
    id = Column(Integer, primary_key=True)
    q_name = Column(
        String,
        nullable=False,
        unique=True,
        default="",
        server_default="",
    )
    description = Column(Text, nullable=False, default="", server_default="")

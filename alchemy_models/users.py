from sqlalchemy import Column, Integer, String

from .db import db


class Questions(db.Model):
    id = Column(Integer, primary_key=True)
    u_name = Column(
        String,
        nullable=False,
        unique=True,
        default="",
        server_default="",
    )
    u_tag = Column(
        String,
        nullable=False,
        unique=True,
        default="",
        server_default="",
    )
    u_full_name = Column(String, nullable=False, default="", server_default="")

#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Table, MetaData

from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from base import get_engine

BaseModel = declarative_base()
DynamicDModel = declarative_base()

"""

class Franchise(BaseModel):
    __tablename__ = 'franchise'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    name = Column(VARCHAR(50))

class ContentRatingSystem(BaseModel):
    __tablename__ = 'content_rating_system'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    name = Column(VARCHAR(50))

class ContentRatingSystemValue(BaseModel):
    __tablename__ = 'content_rating_system_value'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    parent_code = Column(VARCHAR(36), nullable=False)
    name = Column(VARCHAR(50))

class GameGenre(BaseModel):
    __tablename__ = 'game_genre'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    name = Column(VARCHAR(50))

class Region(BaseModel):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    name = Column(VARCHAR(50))


class GameInfo(BaseModel):
    __tablename__ = 'game_info'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    en_name = Column(VARCHAR(50))
    display_name = Column(VARCHAR(50))
    other_name = Column(VARCHAR(200))
    platform = Column(VARCHAR(50))
    release_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    publisher = Column(VARCHAR(50))
    developer = Column(VARCHAR(50))
    metascore = Column(Integer, default=0)
    other_platform = Column(VARCHAR(100))
    franchise_code = Column(VARCHAR(36))
    content_rating_codes = Column(VARCHAR(200))
    genre_code = Column(VARCHAR(200))
    num_players = Column(Integer, default=1)
    lng_codes = Column(VARCHAR(200))
    describe = Column(VARCHAR(500))

    def to_dict(self):
       return {c.name: getattr(self, c.name, None).strftime('%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name, None), datetime) else getattr(self, c.name, None) for c in self.__table__.columns}


class GameCover(BaseModel):
    __tablename__ = 'game_cover'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    game_code = Column(VARCHAR(36), nullable=False)
    imgurl = Column(VARCHAR(200))
    client_type = Column(SMALLINT, default=1)
    region_code = Column(VARCHAR(36))
    versions = Column(VARCHAR(50))
    issue_no = Column(VARCHAR(36))
    describe = Column(VARCHAR(500))

    def to_dict(self):
       return {c.name: getattr(self, c.name, None).strftime('%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name, None), datetime) else getattr(self, c.name, None) for c in self.__table__.columns}

class GameVideo(BaseModel):
    __tablename__ = 'game_video'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    game_code = Column(VARCHAR(36), nullable=False)
    video_url = Column(VARCHAR(200))
    describe = Column(VARCHAR(500))

    def to_dict(self):
       return {c.name: getattr(self, c.name, None).strftime('%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name, None), datetime) else getattr(self, c.name, None) for c in self.__table__.columns}


class GameImage(BaseModel):
    __tablename__ = 'game_image'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    game_code = Column(VARCHAR(36), nullable=False)
    img_url = Column(VARCHAR(200))
    describe = Column(VARCHAR(500))

    def to_dict(self):
        return {
        c.name: getattr(self, c.name, None).strftime('%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name, None),
                                                                                        datetime) else getattr(self,
                                                                                                               c.name,
                                                                                                               None) for
        c in self.__table__.columns}


class IssueInfo(BaseModel):
    __tablename__ = 'issue_info'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    game_code = Column(VARCHAR(36), nullable=False)
    edition_code = Column(VARCHAR(36))
    client_type = Column(SMALLINT, default=1)
    img_url = Column(VARCHAR(200))
    region_code = Column(VARCHAR(36))
    publisher = Column(VARCHAR(50))
    product_id = Column(VARCHAR(100))
    release_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    edition_info = Column(VARCHAR(500))
    is_promotion = Column(BOOLEAN, default=False)
    promotion_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    ori_price = Column(FLOAT)
    general_price = Column(FLOAT)
    plus_price = Column(FLOAT)

    def to_dict(self):
       return {c.name: getattr(self, c.name, None).strftime('%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name, None), datetime) else getattr(self, c.name, None) for c in self.__table__.columns}

class DLC(BaseModel):
    __tablename__ = 'dlc'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(36), nullable=False)
    name = Column(VARCHAR(50))
    game_code = Column(VARCHAR(36), nullable=False)
    describe = Column(VARCHAR(500))

    def to_dict(self):
       return {c.name: getattr(self, c.name, None).strftime('%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name, None), datetime) else getattr(self, c.name, None) for c in self.__table__.columns}
"""

class Franchise(BaseModel):
    __tablename__ = 'game_code'
    id = Column(Integer, primary_key=True)
    store_game_code = Column(VARCHAR(255), nullable=False)
    type = Column(SMALLINT, default=1)

def register_db():
    engine = get_engine()
    BaseModel.metadata.create_all(engine)


def unregister_db():
    engine = get_engine()
    BaseModel.metadata.drop_all(engine)
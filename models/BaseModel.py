from sqlalchemy.ext.declarative import declarative_base

from config.Database import Engine

# BaseEntity Model Schema
EntityMeta = declarative_base()


def init_db():
    EntityMeta.metadata.create_all(bind=Engine)

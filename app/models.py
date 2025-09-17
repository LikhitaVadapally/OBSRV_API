from sqlalchemy import Column, String, Integer, JSON, TIMESTAMP, ARRAY
from sqlalchemy.sql import func
from .database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(String, primary_key=True, index=True)
    dataset_id = Column(String, index=True)
    type = Column(String, nullable=False)
    name = Column(String)
    validation_config = Column(JSON)
    extraction_config = Column(JSON)
    dedup_config = Column(JSON)
    data_schema = Column(JSON)
    denorm_config = Column(JSON)
    router_config = Column(JSON)
    dataset_config = Column(JSON)
    status = Column(String)
    tags = Column(ARRAY(String))
    data_version = Column(Integer)
    created_by = Column(String)
    updated_by = Column(String)
    created_date = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_date = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    published_date = Column(TIMESTAMP(timezone=True), server_default=func.now())


  
class sampletable(Base):
    __tablename__ = "sampletable"
    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
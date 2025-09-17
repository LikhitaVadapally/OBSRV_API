from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from typing import Type
from sqlalchemy.orm import DeclarativeMeta



def generate_pydantic_model(sqlalchemy_model: Type[DeclarativeMeta]):
    """
    Generate a Pydantic model from a SQLAlchemy model dynamically.
    """
    return sqlalchemy_to_pydantic(sqlalchemy_model)

from app.models import sampletable 
SampleTableSchema = sqlalchemy_to_pydantic(sampletable)


#, model_name="SampleTable"
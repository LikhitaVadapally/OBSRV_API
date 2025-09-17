from fastapi import FastAPI, HTTPException, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import AsyncSessionLocal, Base, engine
from app.models import Dataset, sampletable  # import models here
#print("Imported models: ", Datasets, SampleTable)
from app.crud import create, get, update, delete
from app.schemas import generate_pydantic_model
from typing import Dict, Any, Optional
from pydantic import create_model


#helper fucn for patch
def create_partial_model(sqlalchemy_model):
    fields = {}
    for column in sqlalchemy_model.__table__.columns:
        python_type = column.type.python_type
        fields[column.name] = (Optional[python_type], None)
    return create_model(f"{sqlalchemy_model.__name__}Partial", **fields)

app = FastAPI()

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Map table names to models
TABLE_MODELS = {
    "datasets": Dataset,
    "sampletable": sampletable,
}

@app.on_event("startup")
async def startup():
    # Creates tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/v1/{table_name}", response_model=Dict[str, Any])
async def create_record(table_name: str, payload: Dict[str, Any], db: AsyncSession = Depends(get_db)):
    model = TABLE_MODELS.get(table_name)
    if not model:
        raise HTTPException(status_code=404, detail="Table not found")
    PydanticModel = generate_pydantic_model(model)
    validated_data = PydanticModel(**payload)
    obj = await create(db, model, validated_data.dict())
    return obj.__dict__

@app.get("/v1/{table_name}/{id}", response_model=Dict[str, Any])
async def read_record(table_name: str, id: str = Path(...), db: AsyncSession = Depends(get_db)):
    model = TABLE_MODELS.get(table_name)
    if not model:
        raise HTTPException(status_code=404, detail="Table not found")
    obj = await get(db, model, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Record not found")
    return obj.__dict__

@app.patch("/v1/{table_name}/{id}", response_model=Dict[str, Any])
async def update_record(table_name: str, id: str, payload: Dict[str, Any], db: AsyncSession = Depends(get_db)):
    model = TABLE_MODELS.get(table_name)
    if not model:
        raise HTTPException(status_code=404, detail="Table not found")
    obj = await get(db, model, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Record not found")

    PydanticModel = create_partial_model(model)
    validated_data = PydanticModel(**payload)

    updated_obj = await update(db, model, id, validated_data.dict(exclude_unset=True))
    return updated_obj.__dict__

@app.delete("/v1/{table_name}/{id}", status_code=204)
async def delete_record(table_name: str, id: str, db: AsyncSession = Depends(get_db)):
    model = TABLE_MODELS.get(table_name)
    if not model:
        raise HTTPException(status_code=404, detail="Table not found")
    obj = await get(db, model, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Record not found")
    await delete(db, model, id)
    return
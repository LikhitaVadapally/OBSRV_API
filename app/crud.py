from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete
from typing import Type, Any, Dict

async def create(db: AsyncSession, model: Type, obj_in: Dict[str, Any]):
    db_obj = model(**obj_in)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def get(db: AsyncSession, model: Type, id: Any):
    result = await db.execute(select(model).filter_by(id=id))
    return result.scalars().first()

async def update(db: AsyncSession, model: Type, id: Any, obj_in: Dict[str, Any]):
    await db.execute(sqlalchemy_update(model).where(model.id == id).values(**obj_in))
    await db.commit()
    return await get(db, model, id)

async def delete(db: AsyncSession, model: Type, id: Any):
    await db.execute(sqlalchemy_delete(model).where(model.id == id))
    await db.commit()
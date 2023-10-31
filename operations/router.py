from fastapi import APIRouter, Depends, Query
from fastapi.exceptions import HTTPException
from database.database import get_async_session
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import new_order
from answer.schemas import Answer

router = APIRouter(
    prefix='/new_orders',
    tags=['NewOrders']
)


@router.get('/', response_model=Answer)
async def get_new_orders(offset: int = 0, limit: int = Query(default=100, le=100),
                         session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(new_order).offset(offset).limit(limit).order_by('sendAt')
        result_items = await session.execute(query)
        query = select(func.count()).select_from(new_order)
        result_all_items = await session.execute(query)
        return {
            'status': 'success',
            'data': result_items.all(),
            'data_count': result_all_items.scalar(),
            'details': None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'data_count': None,
            'details': None
        })

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from database.database import get_async_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import new_order
from answer.schemas import Answer

router = APIRouter(
    prefix='/new_orders',
    tags=['NewOrders']
)


@router.get('/', response_model=Answer)
async def get_new_orders(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(new_order).order_by('sendAt')
        result = await session.execute(query)
        return {
            'status': 'success',
            'data': result.all(),
            'details': None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': None
        })

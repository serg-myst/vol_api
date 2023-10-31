from sqlalchemy import MetaData, Table, Column, Integer, DateTime, Boolean

metadata = MetaData()

new_order = Table(
    'new_order',
    metadata,
    Column('orderId', Integer, primary_key=True),
    Column('send', Boolean),
    Column('sendAt', DateTime),
)

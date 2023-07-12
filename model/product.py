from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column("pk_product", Integer, primary_key=True)
    name = Column(String(255), unique=True)
    category = Column(String(255), default='')
    quantity = Column(Integer, default=0)
    description = Column(String(255), default='')
    src = Column(String(255), default='https://placehold.co/300x400')
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, name:str = '', category:str = '', quantity:int = 0, description:str = '', src:str = 'https://placehold.co/300x400'):
        """
        Cria um Produto

        Arguments:
            name: Nome do produto.
            quantity: quantidade disponível do produto
            description: Descrição do produto.
            src: URL de imagem do produto
        """
        self.name = name or ''
        self.category = category or ''
        self.quantity = quantity or 0
        self.description = description or ''
        self.src = src or 'https://placehold.co/300x400'

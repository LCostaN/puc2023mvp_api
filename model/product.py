from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column("pk_product", Integer, primary_key=True)
    name = Column(String(255), unique=True)
    category = Column(String(255))
    quantity = Column(Integer)
    description = Column(String(255))
    src = Column(String(255))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, name:str, category:str, quantity:int, description:str, src:str):
        """
        Cria um Produto

        Arguments:
            name: Nome do produto.
            quantity: quantidade disponível do produto
            description: Descrição do produto.
            src: URL de imagem do produto
        """
        self.name = name
        self.category = category
        self.quantity = quantity
        self.description = description
        self.src = src

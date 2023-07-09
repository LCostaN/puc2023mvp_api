from pydantic import BaseModel
from typing import Optional, List
from model.product import Product

class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    name: str = "Nome da Ração"
    category: str = "Ração"
    quantity: Optional[int] = 200
    src: str = "https://placehold.co/600x400"
    description: str = 'Exemplo de descrição de ração.'


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca.
    """
    name: Optional[str] = "Nome"
    category: Optional[str] = "Ração"
    minimo: int = 0


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    data: List[ProdutoSchema]


def apresenta_produtos(produtos: List[Product]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "name": produto.name,
            "category": produto.category,
            "quantity": produto.quantity,
            "src": produto.src,
            "description": produto.description,
        })

    return {"products": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado.
    """
    id: int = 1
    name: str = "Nome da Ração"
    category: str = "Ração"
    quantity: Optional[int] = 200
    src: str = "https://placehold.co/600x400"
    description: str = 'Exemplo de descrição de ração.'


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    name: str

def apresenta_produto(produto: Product):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "name": produto.name,
        "category": produto.category,
        "description": produto.description,
        "src": produto.src,
        "quantity": produto.quantity,
    }

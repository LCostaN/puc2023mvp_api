from pydantic import BaseModel, Field
from typing import Optional, List
from model.product import Product

class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    name: str = Field(title="Nome", description="Nome do Produto", default="Nome da Ração")
    category: str = Field(title="Categoria", description="Nome da Categoria do Produto", default="Ração")
    quantity: Optional[int] = Field(title="Quantidade", description="Quantidade em estoque", default=200) 
    src: Optional[str] = Field(title="Foto", description="Imagem do Produto (URL)", default="https://placehold.co/600x400")
    description: str = Field(title="Descrição", description="Descrição do Produto", default="Descrição longa do produto")


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca.
    """
    name: Optional[str] = Field(title="Nome", description="Nome ou parte do nome do produto", default="Nome da Ração")
    category: Optional[str] = Field(title="Categoria", description="Nome ou parte do nome da categoria do produto", default="Ração")
    min: Optional[int] = Field(title="Mínimo", description="Quantidade mínima para incluir na pesquisa", default=200) 


class ProdutoDelBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca do produto a ser apagado
    """
    id: int = Field(title="Id Produto", description="Id do produto a ser removido", default="1")

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

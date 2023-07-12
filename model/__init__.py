from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.schedule import Schedule
from model.product import Product

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

# popula com produtos iniciais se estiver vazio
session = Session()
if(session.query(Product).count() == 0):
    # Ração
    session.add(Product(
       name='Natural Formula', 
       category='Ração', 
       quantity=200, 
       description='Feita somente com produtos naturais, ideal para raças mais sensíveis',
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='Ração Industrial', 
       category='Ração', 
       quantity=100, 
       description='Ração fruto de pesquisa química na produção de ração. Não há um produto natural se quer, mas a ciência diz que é especialmente nutritiva.',
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='Ração Vira-lata', 
       category='Ração', 
       quantity=1000, 
       description='A ração mais barata do mercado. Não recomendado para consumo por seres vivos',
       src='https://placehold.co/300x400',
    ))

    # Brinquedos
    session.add(Product(
       name='Bola', 
       category='Brinquedos', 
       quantity=50, 
       description='Borracha sintética que massageia a boca do pet ao morder. Tamanhos S, M e G disponíveis',
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
        name='Osso de Borracha', 
        category='Brinquedos', 
        quantity=1, 
        description='Brinquedo clássico de cães! Temos opções nas cores azul, verde, rosa e branco, além de com ou sem barulho extra!',
        src='https://placehold.co/300x400',
    ))
    session.add(Product(
        name='Corda sintética', 
        category='Brinquedos', 
        quantity=0,
        description='Para aqueles que adoram um cabo de guerra, essa corda é feita especialmente para brincar com seu pet sem que um dos dois saia machucado! Mas bom senso no uso da força ainda é recomendado.',
        src='https://placehold.co/300x400',
    ))

    # Acessórios
    session.add(Product(
        name='Laço de cabeça', 
        category='Acessórios', 
        quantity=20, 
        description='Laço para cabeça, orelhas e outros.',
        src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='Coleira Eu amo meu Dono', 
       category='Acessórios', 
       quantity=20, 
       description='Seu companheiro não é indigente! Informe seu dados de contato e informações básicas do pet se for adicionar gravação na parte de trás da coleira.',
       src='https://placehold.co/300x400',
    ))

    # Roupas
    session.add(Product(
       name='Hello Kitty',
       category='Roupas', 
       quantity=8, 
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='I am the king',
       category='Roupas', 
       quantity=2, 
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='Muscles are life',
       category='Roupas', 
       quantity=0, 
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='I love my owner',
       category='Roupas', 
       quantity=0, 
       src='https://placehold.co/300x400',
    ))

    # Suplementos
    session.add(Product(
       name='Vitamina Dogão',
       category='Suplementos', 
       quantity=2,
       description='Todas as vitaminas que seu Pet precisa.',
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='Dog Muscle',
       category='Suplementos', 
       quantity=0,
       description='Suplementos para desenvolvimento muscular do pet. Não utilize sem recomendação veterinária.',
       src='https://placehold.co/300x400',
    ))
    session.add(Product(
       name='Dogbiótico',
       category='Suplementos', 
       quantity=0,
       description='Probiótico canino. Adicione uma dose diária para que seu dog tenha um intestino saudável e eficiente.\n**Observação: Redução no tamanho das fezes é normal.',
       src='https://placehold.co/300x400',
    ))

    session.commit()
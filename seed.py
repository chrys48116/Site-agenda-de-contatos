import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random, datetime
from contatos.models import  Contato, Categoria

def criando_contato(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        name = fake.name()
        sobrenome = name.split(' ')[1]
        telefone = "(61) 9{}-{}".format(random.randrange(1000, 9999),random.randrange(1000, 9999)) 
        email = f'{name}@gmail.com'
        descricao = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Etiam sit amet sapien metus. Proin non justo purus. Class aptent taciti 
        sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. """
        categoria = random.choice(['1','2','3'])
        a = Contato(nome=name, 
                    sobrenome=sobrenome, 
                    telefone=telefone, 
                    email=email, 
                    descricao=descricao, 
                    categoria=Categoria(categoria))
        a.save()

criando_contato(100)

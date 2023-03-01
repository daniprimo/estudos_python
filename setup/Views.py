from django.http import HttpResponse


def hello(request) :
    return HttpResponse('Ola Mundooooo')


def lerBancoDeDados (nome) :
      lista_nomes = [
            {'nome': 'Ana', 'idade': 17},
            {'nome': 'Lavinia', 'idade': 5},
            {'nome': 'Anthony', 'idade': 12},
            {'nome': 'Pedro', 'idade': 20}
      ] 
      for pessoa in lista_nomes:
            if pessoa['nome'] == nome:
                  return pessoa
            else:
                  return {'nome': 'Não encontrado', 'idade': 0}




def articles (request, years) : 
        return HttpResponse('O ano enviado foi: ' + str(years))

def fname (request, nome) :
    result = lerBancoDeDados(nome)
    if result['idade'] > 0:
        return HttpResponse('Nome: '+ result['nome'] + ' / Idade: ' + str(result['idade']))
    else : 
        return HttpResponse('Pessoa não encontrada')
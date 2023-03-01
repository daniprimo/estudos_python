from django.http import HttpResponse
from django.shortcuts import render

def hello(request) :
    return render(request, 'index.html')



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
    
def fname2 (request, nome):
     idade = lerBancoDeDados(nome)
     return render(
          request, 'pessoa.html', {'v_idade': idade['idade']})

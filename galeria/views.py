from django.shortcuts import render

 

def index(request):
    dados = {
        1: {"nome": "nebulosa de carina",
            "legenda": "webbtelecope.org / NASA /  Webb"},
        2: {"nome": "Galáxia ngc 1079",
            "legenda": "nasa.org / NASA / Neymar "},
        3: {"nome": "nebussosa de carina",
            "legenda": "websbtelecope.org / NASA /  Webb"},
        4: {"nome": "Galássxia ngc 1079",
            "legenda": "nasas.org / NASA / Neymar "}
  
    }
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html', {"cards": dados})


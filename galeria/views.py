from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia
 

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
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


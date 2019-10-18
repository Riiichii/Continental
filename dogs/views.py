from django.shortcuts import render

# Create your views here.

def post_index(request):
    return render(request, 'dogs/index.html', {})
def post_formulario(request):
    return render(request, 'dogs/formulario.html', {})
from django.shortcuts import render
from django.views import View

class CadastroView(View):

    def get(self, request):
        return render(request, 'authentication/cadastrar.html')


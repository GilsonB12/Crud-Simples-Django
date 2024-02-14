from django.shortcuts import get_object_or_404, redirect, render
from .models import Pessoas

def homepage(request):
    return render(request, 'crud/homepage.html')

def pessoas(request):
    if request.method == 'POST':
        nova_pessoa = Pessoas()
        nova_pessoa.nome = request.POST.get('nome')
        nova_pessoa.descricao_nome = request.POST.get('descricao_nome')
        nova_pessoa.save()
    
    pessoas = {
        'pessoas': Pessoas.objects.all()
    }
    return render(request, 'crud/newpage.html', pessoas)


def delete(request, id_pessoa):
    deletar_pessoa = get_object_or_404(Pessoas, id_pessoa=id_pessoa)
    deletar_pessoa.delete()
    return redirect('listagem_nomes')

def atualizar_pessoa(request, id_pessoa):
    pessoa = get_object_or_404(Pessoas, id_pessoa=id_pessoa)
    if request.method == 'POST':
        pessoa.nome = request.POST.get('nome')
        pessoa.descricao_nome = request.POST.get('descricao_nome')
        pessoa.save()
        return redirect('listagem_nomes')  # Redireciona para a URL de listagem

    # Se não for POST, renderiza o formulário de edição
    return render(request, 'newpage.html', {'pessoa': pessoa})
    
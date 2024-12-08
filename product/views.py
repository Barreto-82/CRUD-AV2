from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'product/lista.html', {'produtos': produtos})

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'product/detalhe.html', {'produto': produto})

def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'product/form.html', {'form': form})

def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'product/form.html', {'form': form})

def deleta_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'product/confirmar_delete.html', {'produto': produto})

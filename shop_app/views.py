from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductModelForm
from django.shortcuts import render
from .tasks import create_product, ActionName


def index(request):
    return render(request, 'shop_app/base.html')


class ProductListView(ListView):
    model = Product
    template_name = 'shop_app/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop_app/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop_app/create_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        response = super().form_valid(form)
        create_product.delay(
            action_name=ActionName.created, product_name=form.instance.name
        )
        messages.success(
            self.request, f'Продукт "{form.instance.name}" успешно создан!'
        )
        return response


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'shop_app/edit_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop_app/delete_product'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')

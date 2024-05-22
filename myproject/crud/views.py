from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product



class TopView(TemplateView):
    template_name = "top.html"


class ProductListView(ListView):
     model = Product
     template_name = "list.html"
     paginate_by = 3
        
'''
from django.views import View
class TopView(View):
    def get(self, request, *args, **kwargs):
        print("実践ではここに機能を追加していく")
        return render(request, "top.html")

        

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        # Productモデルの全データを取り出す。
        context["object_list"]   = Product.objects.all()

        return render(request, "crud/product_list.html", context)
'''
        

    
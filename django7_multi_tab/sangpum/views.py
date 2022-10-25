from django.shortcuts import render
from sangpum.models import Maker, Product

# Create your views here.
def Main(request):
    return render(request, 'main.html')


def List1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'makers':makers})


def List2(request): # 전체 상품
    products = Product.objects.all()
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})



def List3(request): # 특정 상품
    mid = request.GET.get("id")
    products = Product.objects.filter(maker_name=mid)
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

    


from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def page1Func(request):
    return render(request, 'page1.html')


def page2Func(request):
    return render(request, 'page2.html')


def cartFunc(request):
    name = request.POST["name"] #post방식으로 넘어오는 값
    price = request.POST["price"]
    product = {'name':name, 'price':price} # java의 dto 클래스 역할
    
    productList = [] #java의 formbean 역할
    
    if "shop" in request.session:
        # shop 을 꺼내서 productList 집어넣음
        productList = request.session['shop'] #세션 내에 'shop' 이라는 key로 rpoductList가 등록됨(세션이 이미 만들어진 상태)
        productList.append(product)
        request.session['shop'] = productList
    else : #최초의 상품인 경우
        productList.append(product)
        request.session['shop'] = productList
        # 'shop' 가 이제 만들어졌으니 2번째 상품부턴 만든 shop을 꺼내는 절차를 하는 것
        
    context={}
    context['products']=request.session['shop']
    return render(request, 'cart.html', context)


def buyFunc(request):
    if "shop" in request.session:
        productList = request.session['shop']
        total = 0
        
        for p in productList:
            total += int(p['price'])
            
        print('결제 총액 :', total)
        request.session.clear() # 세션 내의 모든 키 삭제
        del request.session['shop'] # 특정 키를 가진 세션 내용 삭제

    return render(request, "buy.html", {'total':total})


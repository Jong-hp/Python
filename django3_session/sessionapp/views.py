from django.shortcuts import render
from django.http.response import HttpResponseRedirect


# Create your views here.

def mainFunc(request):
    return render(request, 'main.html')

def setOsFunc(request):
    if "favorite_os" in request.GET:
        # print(request.GET.get("favorite_os"))
        print(request.GET["favorite_os"])
        
        # "f_os"라는 키로 세션을 생성
        request.session["f_os"] = request.GET["favorite_os"]
        # return render() 형식은 forwardin이기 떄문에 클라이언트를 통한 요청 불가
        # 다시말해 메인 urls.py를 만날 수 없다.
    
        # forwarding 말고 redirect 방식을 사용한다면 가능함
        return HttpResponseRedirect("/showos")
    else:
        return render(request, 'selectos.html')    # 요청값에 "favorite_os"이 없는 경우
    
    
def showOsFunc(request):
    # print("여기까지 도착")
    dict_context = {}
    
    if "f_os" in request.session:
        print('유효 시간: ', request.session.get_expiry_age())
        dict_context['sel_os'] = request.session["f_os"]
        dict_context['message'] = "그대가 선택한 운영체제는 %s"%request.session["f_os"]
    else:
        dict_context['sel_os'] = None
        dict_context['message'] = "운영체제를 선택하지 않았군요"
        
    # del request.session["f_os"] # 특정 세션 삭제
    request.session.set_expiry(5)   # 새로운 요청 이후 5초 후 세션 삭제
    # set_expiry(0) 브라우저가 닫힐 때 세션이 해제됨
    
    return render(request, 'show.html', dict_context)
        
from django.shortcuts import render

def home(request):
    return render(request, 'index.html') # 어떤 요청이 들어왔을 때 index.html을 띄워 보내줘라라는 뜻

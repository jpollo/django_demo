from django.shortcuts import render

# Create your views here.


# 主页
def home(request):
    args = dict()
    return render(request, 'index.html', args)


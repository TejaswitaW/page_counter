from django.shortcuts import render

# Create your views here.
def home(request):
    cnt = request.session.get('count',0)
    newcnt = cnt + 1 
    request.session['count'] = newcnt
    return render(request,'pagecount/home.html',{'c':newcnt})

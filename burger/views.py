from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request,"homepage.html")
    
def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def blog(request):
    # return HttpResponse('Blog')
    return render(request,'blog.html')
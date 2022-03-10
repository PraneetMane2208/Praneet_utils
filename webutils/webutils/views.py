from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse(''' <h1>Harry</h1> <a href=" https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">
#     djang0 code with harry>''')

def about(request):
    return HttpResponse("hello praneet bhai friend of aatama")


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps' , 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    if removepunc=="on":

        punctuations='''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = ""
        for char in djtext  :
            if char not in punctuations:
                analyzed=analyzed +char
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":

                analyzed=analyzed+char
        params = {'purpose': 'new line remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcount=="on":
        analyzed=len(djtext)

        params = {'purpose': 'charcount', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
#   return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("Capitalize first")
#
# def newlineremover(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("Char Count")
#
#

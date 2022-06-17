# I have created this website by using django frame work



from django.http import HttpResponse
from django.shortcuts import render
# code for video 6
# def index (request):
#     return HttpResponse ('''<h1>Hello Ashraf</h1> <a href = "https://quran.com/">Noble Quran</a>''')

# def about (request):
#     return HttpResponse (" Ashraf is Muslim")

# code for video 7
def index (request):
    return render(request, 'index.html')

   # return HttpResponse ('Home')


def analyze (request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    lineremover = request.GET.get('lineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    #analyzed = djtext
    if removepunc == "on":
        punctuations = ''':;()[]-?/&*%$#@!^_~"'|><'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed }
        return render(request, 'analyze.html' , params )
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper() 
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed }
        return render(request, 'analyze.html' , params )
    elif (lineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        return render (request, 'analyze.html', params)
    elif(spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " " :
                pass
            else:   
                analyzed = analyzed+char

        params = {'purpose': 'Removed Space ', 'analyzed_text': analyzed }
        return render(request, 'analyze.html' , params )

    elif(charcounter == "on"):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        
        params = {'purpose': 'character counter', 'analyzed_text': analyzed }
        return render(request, 'analyze.html' , params )
    else:
        return HttpResponse ('ERROR')

# def Capitalize (request):
#     return HttpResponse('CapFirst')

# def newlineremove (request):
#     return HttpResponse('newlineremove')

# def spaceremove (request):
#     return HttpResponse('spaceremove')

# def charcount (request):
#     return HttpResponse('charcount')


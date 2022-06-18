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
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    
    if removepunc == "on":
        punctuations = ''':;()[]-?/&\,*%$#@!^_~"'|><'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed }
        djtext = analyzed
        
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper() 
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed }
        djtext = analyzed
        
    
    if lineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!= "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        
    
    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " " :
                pass
            else:   
                analyzed = analyzed+char

        
        params = {'purpose': 'Removed Space ', 'analyzed_text': analyzed }
        djtext = analyzed
       
    if charcounter == "on":
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        
        params = {'purpose': 'character counter', 'analyzed_text': analyzed }
        

    if (removepunc != "on" and lineremover !="on" and spaceremover != "on" and fullcaps != "on" and charcounter != "on"):
        return HttpResponse("ERROR: please select any operation!")
    
    return render(request, 'analyze.html' , params )

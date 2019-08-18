#I HAVE CREATED THIS FILE - YASH KHANDELWAL

from django.http import HttpResponse
from django.shortcuts import render

# def about(request):
#     return HttpResponse("hello")
#
# def index(request):
#     return HttpResponse('''<h1>hello yash</h1> <a
#     href="https://www.codingninjas.in/"> coding ninjas</a>''')

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    print(removepunc)
    print(djtext)


    #check which checkbox is on
    if removepunc=="on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,.<>/?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext=analyzed
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        djtext = analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)







#
# def capfirst(request):
#     return HttpResponse("capitalize first")
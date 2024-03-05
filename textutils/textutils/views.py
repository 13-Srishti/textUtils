from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello Srishti")
    param={'name':'Srishti', 'age':14}
    return render(request, 'index.html', param)

def about(request):
    return HttpResponse("<a href='https://www.linkedin.com/feed/'>About</a>")




def analyze(request):
    textRecieve= request.POST.get('text', 'text not recieved')
    removepunc= request.POST.get('removepunc', 'off')
    allcaps= request.POST.get('allcaps', 'off')
    removenewline= request.POST.get('removenewline', 'off')
    removespace= request.POST.get('removespace', 'off')
    countchar= request.POST.get('countchar', 'off')
    
    
    if removepunc=='on':
         analyzed= ""
         punctuation= '''.,?!:;()[]{}"'-`<>/*&@#$%^_=+'''
         for char in textRecieve:
             if char not in punctuation:
                 analyzed= analyzed+char
                 
         params={'purpose': 'Removing Punctuation', 'analyzed_text': analyzed} 
         textRecieve= analyzed
    
    if allcaps=='on':
        analyzed=""
        for char in textRecieve:
            analyzed= analyzed+ char.upper()
        params={'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        textRecieve= analyzed 
    
    if removenewline=='on':
        analyzed=""
        for char in textRecieve:
            if char != '\n':
                analyzed= analyzed+ char
        params={'purpose': 'Removing new line', 'analyzed_text': analyzed}
        textRecieve= analyzed

    if removespace=='on':
        analyzed=""
        for char in textRecieve:
            if char != ' ':
                analyzed= analyzed+ char
        params={'purpose': 'Removing space', 'analyzed_text': analyzed} 
        textRecieve= analyzed
    

    

    if countchar=='on':
        analyzed_count=0
        for char in textRecieve:
            analyzed_count=analyzed_count+1
        params={'purpose': 'Counting Characters', 'analyzed_text_count': analyzed_count, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        
    return render(request, 'analyze.html', params)
        
        



    
    
   
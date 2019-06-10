from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['texthere']
    words=text.split()
    word_num={}

    for word in words:
        if word in word_num:
            word_num[word]+=1
        else:
            word_num[word]=1





    return render(request, 'result.html', {'full': text, 'total' : len(words), 'number': word_num.items()}) 
      
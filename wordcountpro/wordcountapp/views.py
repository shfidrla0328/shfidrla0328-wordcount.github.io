from django.shortcuts import render
from .models import Save

# Create your views here.
def save(request):
    saves = Save.objects
    return render(request, 'index.html', {'saves': saves})

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary': word_dictionary.items()})
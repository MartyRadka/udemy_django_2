from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
    # the fulltext will contain the input from user
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()  # this will split up the string into a list of words

    worddictionary = {}  # key is word, value is number of this word

    for word in wordlist:
        if word in worddictionary:
            # if word is already in worddictionary increase the number of words
            worddictionary[word] += 1
        else:
            # if not add it to the worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'totalcount': len(wordlist), 'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html')

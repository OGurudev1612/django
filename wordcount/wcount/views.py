from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'wcount/home.html')
def about(request):
    return render(request,'wcount/about.html')
def count(request):
    fulltext=request.GET['text']
    word_count=len(fulltext.split())
    word_dict={}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    word_list=[(i,word_dict[i]) for i in word_dict.keys()]
        

    return render(request,"wcount/count.html",{'fulltext':fulltext,'word_count':word_count,'word_dict':word_dict,'word_list':word_list})

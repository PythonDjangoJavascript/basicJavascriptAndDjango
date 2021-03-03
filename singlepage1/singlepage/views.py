from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

text = ["This is page one. The quick brown fox jumps over the lazy dog",
        "page two has nothing to do with you, just move to the next page ",
        "Finally you made it. Hope you enjoyed our pages. If you do don't forget to leave an appreciation and thank you for being with us"
        ]


def index(request):
    return render(request, "singlepage/index.html")


def sections(request, num):
    if 1 <= num <= 3:
        return HttpResponse(text[num-1])
    else:
        raise Http404("No such section")

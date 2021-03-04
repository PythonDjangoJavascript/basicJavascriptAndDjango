from django.http.response import JsonResponse
from django.shortcuts import render
import time


# Create your views here.


def index(request):
    return render(request, "posts/index.html")


def posts(request):

    # get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # generate posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    time.sleep(1)

    return JsonResponse({"posts": data})


def alu(request):
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or start+9)

    data = []
    for i in range(start, end+1):
        data.append(f"Post #{i}")

    time.sleep(1)

    return JsonResponse({"post": data})

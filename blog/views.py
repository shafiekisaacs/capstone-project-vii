from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    """Render the blog page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the blog page.
    :rtype: HttpResponse
    """    
    return render(request, "blog.html")


def post(request):
    """Render the POST page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the post page.
    :rtype: HttpResponse
    """    
    return render(request, "post.html")

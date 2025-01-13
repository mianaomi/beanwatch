from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    html_content = """
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h1 style="color: brown; font-family: Helvetica;">Hello, Coffee@UMD!</h1>
        </body>
    </html>
    """
    return HttpResponse(html_content)
from django.shortcuts import render


# Create your views here.
def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def server_failure(request):
    return render(request, 'pages/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)
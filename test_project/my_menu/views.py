from django.shortcuts import render, redirect


def redirect_menu(request):
    response = redirect('menu/')
    return response


def index(request, *args, **kwargs):
    return render(request, 'base.html', context={})


def show_selected(request, *args, **kwargs):
    context = {
        'selected_name': kwargs['selected']
    }

    return render(request, 'base.html', context=context)


def another(request):
    return render(request, 'another_page.html')

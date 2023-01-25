from django.shortcuts import render, redirect

from .models import Menu


def redirect_menu(request):
    response = redirect('menu/')
    return response


def index(request, *args, **kwargs):
    print('index')
    # root_item = Menu.objects.filter(is_root=True, url=kwargs['url'])
    #
    # context = {
    #     'roots': root_item,
    #     'column_count': len(root_item)
    # }
    # print(root_item)
    # --------------

    return render(request, 'base.html', context={})


def show_selected(request, *args, **kwargs):
    print('selected', kwargs['selected'])
    context = {
        'selected_name': kwargs['selected']
    }

    return render(request, 'base.html', context=context)


def another(request):
    print('another')
    return render(request, 'another_page.html')


# def show_selected(request, *args, **kwargs):
#     print('selected')
#     print(kwargs['url'])
#     selected_item = Menu.objects.filter(is_root=True, url=kwargs['url'])
#     context = {
#         'roots': selected_item,
#         'selected_name': kwargs['selected']
#     }
#     return render(request, 'index2.html', context=context)

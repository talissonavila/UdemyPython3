from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'text': 'Welcome to home page.'
    }
    
    return render(request=request, template_name='home/index.html', 
    context=context
                )

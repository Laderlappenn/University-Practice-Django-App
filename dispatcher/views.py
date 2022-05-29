from django.shortcuts import render, HttpResponse

from .forms import ActForm

def act(request):
    if request.method == 'POST':
        form = ActForm(request.POST)
        if form.is_valid():
            return HttpResponse('OK')
    else:
        form = ActForm()

    return render(request, 'dispatcher/act.html', {'form':form})



from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show

def index(request):
    return redirect ('/shows')

def shows(request):
    context = {
        "all_the_shows": Show.objects.all(),
    }
    return render(request, 'index.html', context)

def shows_new(request):
    context = {
        "all_the_shows": Show.objects.all(),
    }
    return render(request, 'create.html', context)

def add_show(request):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    else:
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], desc=request.POST['notes'])
        
        return redirect(f'/shows/{show.id}')

def shows_page(request, shows_id):
    one_show = Show.objects.get(id=shows_id)

    context = {
        "all_the_shows": Show.objects.all(),
        "one_show": one_show
    }
    return render(request, 'shows.html', context)

def edit_page(request, shows_id):

    one_show = Show.objects.get(id=shows_id)

    context = {
        "one_show": one_show
    }
    
    return render(request, 'edit.html', context)

def destroy(request, shows_id):

    one_show = Show.objects.get(id=shows_id)

    context = {
        "one_show": one_show
    }
    
    return render(request, 'destroy.html', context)

def delete(request):
    shows_id = request.POST['shows_id']

    show_to_destroy = Show.objects.get(id=shows_id)
    show_to_destroy.delete()

    return redirect('/')

def edit(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            shows_id = request.POST['shows_id']
        return redirect('/shows/' + shows_id + '/edit')
    else:
        shows_id = request.POST['shows_id']

        shows_to_update = Show.objects.get(id=shows_id)
        shows_to_update.title = request.POST['title']
        shows_to_update.network = request.POST['network']
        shows_to_update.release_date = request.POST['date']
        shows_to_update.desc = request.POST['notes']
        shows_to_update.save()
        messages.success(request, "Show successfully updated")
        
        return redirect('/shows/' + shows_id)


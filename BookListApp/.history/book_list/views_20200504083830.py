from django.shortcuts import render, redirect
from .models import book
from .forms import bookForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):

	if request.method == 'POST':
		form = bookForm(request.POST or None)
        
		if form.is_valid():
			form.save()
			all_items = book.objects.all
			messages.success(request, ('Item Has Been Added To Book List!'))
			return render(request, 'home.html', {'all_items': all_items})

	else:
		all_items = book.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def about(request):
	context = {'first_name': 'John', 'last_name': "Doe's"}
	return render(request, 'about.html', context)

def delete(request, book_id):
	item = book.objects.get(pk=book_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect('home')

def cross_off(request, book_id):
	item = book.objects.get(pk=book_id)
	item.completed = True
	item.save()
	return redirect('home')	

def uncross(request, book_id):
	item = book.objects.get(pk=book_id)
	item.completed = False
	item.save()
	return redirect('home')	

def edit(request, book_id):
	if request.method == 'POST':
		item = book.objects.get(pk=book_id)

		form = bookForm(request.POST or None, instance=item)
        
		if form.is_valid():
			form.save()
			messages.success(request, ('Item Has Been Edited!'))
			return redirect('home')

	else:
		item = book.objects.get(pk=book_id)
		return render(request, 'edit.html', {'item': item})




from django.shortcuts import render
from .models import book
from .forms import bookForm
from django.contrib import messages


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
	context = {'first_name': 'Mohammed', 'last_name': 'Kemal'}
	return render(request, 'about.html', context)

def delete(request, book_id):
	item = book.objects.get(pk=book_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect('home')
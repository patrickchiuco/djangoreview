from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.http import Http404
from .models import Notes
from .forms import NotesForm
# Create your views here.

class NotesListView(ListView):
	model = Notes
	context_object_name = 'notes' # default is objects
	template_name = 'notes/notes_list.html' # followed default so no need

class NotesDetailView(DetailView):
	model = Notes
	context_object_name = 'note'

class NotesCreateView(CreateView):
	model = Notes
	#fields = ['title', 'text']
	form_class = NotesForm
	success_url = '/smart/notes/'

class NotesUpdateVIew(UpdateView):
	model = Notes
	#fields = ['title', 'text']
	form_class = NotesForm
	success_url = '/smart/notes/'

class NotesDeleteView(DeleteView):
	model = Notes
	success_url = '/smart/notes/'
	template_name = 'notes/notes_delete.html'

	
"""
def list(request):
	all_notes = Notes.objects.all()
	return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
	try:
		note = Notes.objects.get(pk=pk)
		return render(request, 'notes/notes_detail.html', {'note': note})
	except Notes.DoesNotExist:
		raise Http404('Note doesn\'t exist')
"""
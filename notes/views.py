from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # mixin for login required
from django.http import Http404
from .models import Notes
from .forms import NotesForm
from django.http.response import HttpResponseRedirect
# Create your views here.

class NotesListView(LoginRequiredMixin,ListView):
	model = Notes
	context_object_name = 'notes' # default is objects
	template_name = 'notes/notes_list.html' # followed default so no need
	login_url = '/login'

	def get_queryset(self):
		return self.request.user.notes.all()

class NotesDetailView(DetailView):
	model = Notes
	context_object_name = 'note'

class NotesCreateView(CreateView):
	model = Notes
	#fields = ['title', 'text']
	form_class = NotesForm
	success_url = '/smart/notes/'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

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
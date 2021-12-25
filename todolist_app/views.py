from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login

from django.urls import reverse_lazy
from .models import Task

class TaskList(LoginRequiredMixin, ListView):
	model = Task
	context_object_name = 'tasks'	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = context['tasks'].filter(user=self.request.user)
		context['count'] = context['tasks'].filter(complete=False).count()

		search_input = self.request.GET.get('search-area') or ''
		if search_input:
			context['tasks'] = context['tasks'].filter(title__icontains=search_input)
			context['search_input'] = search_input


		return context

class TaskDetail(LoginRequiredMixin, DetailView):
	model = Task 
	context_object_name = 'tasks'
	# how to change the name of the template
	# template_name = 'todolist_app/name.html'



class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task 
	fields = ['title', 'description', 'complete']
	success_url = reverse_lazy('todolist_app:tasklist')

	def form_valid(self, form):
		form.instance.user =self.request.user
		return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
	model = Task 
	fields = ['title', 'description', 'complete']
	success_url = reverse_lazy('todolist_app:tasklist')



class TaskDelete(LoginRequiredMixin, DeleteView):
	model = Task
	context_object_name = 'tasks'
	success_url = reverse_lazy('todolist_app:tasklist')



class CustomLoginView(LoginView):
	template_name = 'todolist_app/login_page.html'
	fields = '__all__'
	redirect_authenticated_user = False

	def get_success_url(self):
		return reverse_lazy('todolist_app:tasklist')



class CustomLogOutView(LogoutView):
	template_name = 'todolist_app/logout_page.html'

	def get_success_url(self):
		return reverse_lazy('todolist_app:logout_page')


class TaskRegister(FormView):
	template_name = 'todolist_app/register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('todolist_app:login_page')
	
	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(TaskRegister, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('todolist_app:tasklist')
		return super(TaskRegister, self).get(*args, **kwargs)



def home(request):
	return render(request, 'todolist_app/home.html')





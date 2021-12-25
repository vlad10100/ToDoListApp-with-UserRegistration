from django.urls import path  
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, CustomLogOutView, TaskRegister
from. import views



app_name = 'todolist_app'
urlpatterns = [
	path('tasklist', TaskList.as_view(), name='tasklist'),
	path('taskcreate/', TaskCreate.as_view(), name='taskcreate'),
	path('task/<int:pk>', TaskDetail.as_view(), name='taskdetail'),
	path('taskupdate/<int:pk>', TaskUpdate.as_view(), name='taskupdate'),
	path('taskdelete/<int:pk>', TaskDelete.as_view(), name='taskdelete'),


	path('login/', CustomLoginView.as_view(), name='login_page'),
	path('logout/', CustomLogOutView.as_view(), name='logout_page'),
	path('register/', TaskRegister.as_view(), name='register'),

	path('home/', views.home, name='home'),
]	



# path('logout/', LogoutView.as_view(next_page='/login/'), name='logout_page')
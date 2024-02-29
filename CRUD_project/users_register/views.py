from django.shortcuts import render,redirect
from .forms import UsersForm
from .models import Users

# Create your views here.

def users_list(request):
    context = {'users_list' : Users.objects.all()}
    return render(request, "users_register/users_list.html", context)

def users_form(request,id=0):
   if request.method == "GET":
      if id==0:
         form = UsersForm()
      else:
         user = Users.objects.get(pk=id)
         form = UsersForm(instance=user)
      return render(request, "users_register/users_form.html", {'form':form})
   else:
      if id==0:
          form = UsersForm(request.POST)
      else:
         user = Users.objects.get(pk=id)
         form =  UsersForm(request.POST, instance=user)
      if form.is_valid():
         form.save()
      return redirect('/users/lists')
   
def users_delete(request,id):
    user = Users.objects.get(pk=id)
    user.delete()
    return redirect('/users/lists')
from django.shortcuts import render,HttpResponseRedirect
from.forms import studentregistration
from .models import user
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
from django.contrib import messages

#add_and show 
class AddAndShow(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     fm = studentregistration()
     stud = user.objects.all()
     context = {'stu':stud,'form':fm}
     return context
    def post(self, request, *args, **kwargs):
      fm = studentregistration(request.POST)
      if fm.is_valid():
         fw = fm.cleaned_data['first_name']
         ln = fm.cleaned_data['last_name']
         ph = fm.cleaned_data['phone']
         ad = fm.cleaned_data['address']
         em = fm.cleaned_data['email']
         pw = fm.cleaned_data['password']
         reg = user(first_name=fw,last_name=ln,phone=ph,address=ad, email=em, password=pw)
         reg.save()
         return HttpResponseRedirect('/')
     
     
     
#this class is used to update
class UpdateUser(View):
  def get(self, request,id):
     pi=user.objects.get(pk=id)
     fm=studentregistration(instance=pi)  
     return render(request,'enroll/update.html',{'form':fm})
  def post(self, request,id):
        pi=user.objects.get(pk=id)
        fm=studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'updated successfully')
        return render(request,'enroll/update.html',{'form':fm})
        

#this class is used to delete
class DeleteStudent(RedirectView): 
    url = '/'
    def get_redirect_url(self,*args, **kwargs):
        del_id = kwargs['id']
        user.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    

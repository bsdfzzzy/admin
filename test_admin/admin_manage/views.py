from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from model.models import Admin, User, Contact, Event, RecommendEvent
import json

def index(request):
	return render(request, 'admin_manage/login.html')
def users(request):
	users = User.objects.all()
	context = {'choice' : 1, 'users' : users}
	return render(request, 'admin_manage/users.html', context)
def users_id(request, id):
	user = User.objects.get(id=id)
	event = user.event_set.all()
	context = {'choice' : 1, 'user' : user, 'events' : events}
	return render(request, 'admin_manage/user.html', context)
def admins(request):
	admins = Admin.objects.all()
	context = {'choice' : 4, 'admins' : admins}
	return render_to_response('admin_manage/admins.html', context)
def admin_add_account(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		#this should judge if the user is super
		new_admin = Admin(name=data['name'], password=data['password'], admin_type=data['type'])
		new_admin.save()
		code = JsonResponse({'code' : 1})
		return(code)
def admin_delete_account(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		delete_admin = Admin.objects.get(id=data['id'])
		delete_admin.delete()
		code = JsonResponse({'code' : 1})
		return(code)
def admin_power(request):
	if request.method == 'GET':
		admins = Admin.objects.all()
		context = {'choice' : 4 , 'admins' : admins}
		return render_to_response('admin_manage/admin-power.html', context)
	if request.method == 'POST':
		data = json.loads(request.body)
		p = Admin.objects.get(id=data['id'])
		p.admin_type = data['type']
		p.save()
		code = JsonResponse({'code': 1})
		return (code)
def users_daily_id(request, id):
	user0 = User.objects.get(id=id)
	dailys = user0.event_set.all()
	context = {'choice' : 1, 'user0' : user0, 'dailys' : dailys}
	return render(request, 'admin_manage/user-daily.html', context)
def users_contact_list_id(request, id):
	user0 = User.objects.get(id=id)
	users = user0.contact_set.all()
	context = {'choice' : 1, 'user0' : user0, 'users' : users}
	return render(request, 'admin_manage/user-contact-list.html', context)
#def users_activity_id(request, id):
def users_contact(request):
	return render(request, 'admin_manage/user-contact.html')
def users_notice(request):
	return render(request, 'admin_manage/user-notice.html')
def recommends(request):
	recommends = RecommendEvent.objects.all()
	context = {'choice' : 2, 'recommends' : recommends}
	return render(request, 'admin_manage/recommends.html', context)
def recommends_id(request, id):
	recommend = RecommendEvent.objects.get(id=id)
	context = {'choice' : 2, 'recommend' : recommend}
	return render(request, 'admin_manage/recommend.html', context)
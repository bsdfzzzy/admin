from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'users/daily/(\d+)', views.users_daily_id, name='user_daily_id'),
	url(r'users/contact_list/(\d+)', views.users_contact_list_id, name='users_contact_list_id'),
	#url(r'users/activity/(\d+)', views.users_activity_id, name='users_activity_id'),
	url('users/contact', views.users_contact, name='users_contact'),
	url('users/notice', views.users_notice, name='users_notice'),
	url(r'users/(\d+)', views.users_id, name='users_id'),
	url('users', views.users, name='users'),
	url('admins/admin_power', views.admin_power, name='admin_power'),
	url('admins/admin', views.admins, name='admins_admin'),
	url('add_account', views.admin_add_account, name='add_account'),
	url('delete_account', views.admin_delete_account, name='delete_account'),
	url(r'recommends/(\d+)', views.recommends_id, name='recommends_id'),
	url('recommends', views.recommends, name='recommends'),
]
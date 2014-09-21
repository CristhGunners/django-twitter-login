from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Login(TemplateView):
	template_name = "system/login.html"

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('home')
		return super(Login, self).dispatch(request, *args, **kwargs)

class Home(TemplateView):
    template_name = "system/home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Home, self).dispatch(*args, **kwargs)
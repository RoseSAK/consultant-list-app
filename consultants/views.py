from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Consultant, User, is_manager
from .forms import ConsultantForm
from consultants.utils import search_consultants

@login_required
@user_passes_test(is_manager)
def manager_home(request):
    template = loader.get_template('consultants/manager_home.html')
    context = RequestContext(request, {})

    context.update(csrf(request))
    return HttpResponse(template.render(context))

@login_required
def search_candidates(request):
    # shows the search bar only 

    user = request.user
    manager = is_manager(user)

    if request.method == 'GET':
        try:
            search_query = request.GET.get('search-consultant')
            consultant_list = search_consultants(search_query)
        except:
            consultant_list = Consultant.objects.all()

        template = loader.get_template('consultants/consultant_database.html')
        context = RequestContext(request, {
            'user': user,
            'consultant_list': consultant_list,
            'manager': manager,
        })
        context.update(csrf(request))
        return HttpResponse(template.render(context))

    else:
        template = loader.get_template('consultants/search_candidates.html')
        context = RequestContext(request, {})

        context.update(csrf(request))
        return HttpResponse(template.render(context))

@login_required
def candidate_detail(request, candidate_id=None):
   # shows the info for a single candidate

   user = request.user
   candidate = Consultant.objects.get(id=candidate_id)
   manager = is_manager(user)

   template = loader.get_template('consultants/candidate_detail.html')

   context = RequestContext(request, {
       'user': user,
       'consultant': candidate,
       'manager': manager
   })

   context.update(csrf(request))
   return HttpResponse(template.render(context))

@login_required
@user_passes_test(is_manager)
def edit_candidate(request, candidate_id=None):

    if request.method == 'POST':
        print("POSTED")
        if candidate_id:
            candidate = Consultant.objects.get(id=candidate_id)
            form = ConsultantForm(request.POST, instance=candidate)
            print(candidate)
        else:
            form = ConsultantForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            Consultant.objects.update()
            if candidate_id:
                return HttpResponseRedirect(reverse('candidate_detail', kwargs={'candidate_id': candidate_id}))
            else:
                candidate = Consultant.objects.latest('pk')
                return HttpResponseRedirect(reverse('candidate_detail', kwargs={'candidate_id': candidate.id}))
        else:
            print("invalid")
            print(form.errors)
            template = loader.get_template('consultants/edit_candidate.html')
            context = RequestContext(request, {
                'form': form,
                'candidate': candidate,
            })
            context.update(csrf(request))
            return HttpResponse(template.render(context))
    else:
        if candidate_id:
            candidate = Consultant.objects.get(id=candidate_id)
            form = ConsultantForm(instance=candidate)
        else:
            candidate = None
            form = ConsultantForm()

        template = loader.get_template('consultants/edit_candidate.html')
        context = RequestContext(request, {
            'form': form,
            'candidate': candidate,
        })

        context.update(csrf(request))
        return HttpResponse(template.render(context))

def delete_candidate(request, candidate_id):
    candidate = Consultant.objects.get(pk=candidate_id)
    candidate.delete()
    Consultant.objects.update()
    return HttpResponseRedirect(reverse('consultant_database'))

@login_required
def consultant_database(request):
   # database view from search results

   user = request.user
   manager = is_manager(user)

   if request.method == 'GET':
       try:
            search_query = request.GET.get('search-consultant')
            consultant_list = search_consultants(search_query)
       except:
            consultant_list = Consultant.objects.all()
   else:
        consultant_list = Consultant.objects.all()

   template = loader.get_template('consultants/consultant_database.html')

   context = RequestContext(request, {
       'user': user,
       'consultant_list': consultant_list,
       'manager': manager,
   })

   context.update(csrf(request))
   return HttpResponse(template.render(context))

@login_required
def view_selection(request):
    template = loader.get_template('consultants/view_selection.html')
    context = RequestContext(request, {})

    context.update(csrf(request))
    return HttpResponse(template.render(context))

@login_required
def view_all(request):
    user = request.user

    consultant_list = Consultant.objects.all()

    template = loader.get_template('consultants/view_all.html')

    context = RequestContext(request, {
       'user': user,
       'consultant_list': consultant_list,
       'view_all_staff': True,
    })

    context.update(csrf(request))
    return HttpResponse(template.render(context))

def index(request, filter=None, search=None, sort_by=None):

    user = request.user
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'user': user,
    })

    context.update(csrf(request))
    return HttpResponse(template.render(context))
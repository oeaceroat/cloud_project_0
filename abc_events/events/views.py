from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from .forms import CustomUserCreationForm, EventForm
from .models import Event
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserEventsList(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'all_events_by_user'

    def get_queryset(self):
        return Event.objects.filter(owner=self.kwargs['pk'])


def events(request):
    return render_to_response("events/events.html", {"events": Event.objects.filter(owner=request.user).order_by('start_date'), "messages": messages.get_messages(request)})


def add_event(request):
    form = EventForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            event_form = form.save(commit=False)
            print( request.user)
            event_form.owner = request.user

            event_form.save()
            messages.add_message(request, messages.SUCCESS, "The event has been saved!")
            return HttpResponseRedirect("/events/list/")

    return render(request, 'events/form_events.html', {'form': form})


def update_event(request, eventid):
    instance = get_object_or_404(Event, id=eventid)
    form = EventForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The event has been updated!")
            return HttpResponseRedirect("/events/list/")

    return render(request, 'events/form_events.html', {'form': form})


def delete_event(request, eventid):

    instance = get_object_or_404(Event, id=eventid)
    instance_name = instance.name
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "The event with name %s has been deleted!" % instance_name)
    return HttpResponseRedirect("/events/list")
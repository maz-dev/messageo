from django.shortcuts import render
from django.http import HttpResponse
from chat.models import Message
from chat.forms import SubmitForm
from datetime import datetime
import json


def index(req):

    context = {
        'message_list': Message.objects.all(),
        'form': SubmitForm()
    }
    return render(req, 'chat/index.html', context)

def submit_message(request):
    if request.method == 'POST':
        message_body = request.POST.get('message')
        response_data = {}

        message = Message(body=message_body)
        message.save()

        response_data['result'] = 'Create message successful!'
        response_data['text'] = message.body
        response_data['posted'] = message.posted.strftime('%B %d, %Y %I:%M %p')

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



# class MessageView(FormMixin, ListView):
#     template_name = 'chat/index.html'
#     model = Message


# class MessageCreate(CreateView):
#     model = Message
#     form_class = SubmitForm
#     template_name = 'chat/form.html'
#     success_url = '/'

#     def get_context_data(self, **kwargs):
#         kwargs['object_list'] = Message.objects.all()
#         return super(MessageCreate, self).get_context_data(**kwargs)



# from django.views import generic


# class AjaxTemplateMixin(object):
#     ajax_template_name = None

#     def get_template_names(self):
#         assert self.ajax_template_name, 'You must supply an ajax_template_name for {}'.format(self.__class__.__name__)
#         template_names = super(AjaxTemplateMixin, self).get_template_names()
#         if self.request.is_ajax():
#             template_names.insert(0, self.ajax_template_name)
#         return template_names


# class MasterDetailMixin(AjaxTemplateMixin, generic.list.MultipleObjectMixin):
#     def get_context_data(self, **kwargs):
#         if 'object_list' not in kwargs:
#             self.object_list = self.get_queryset()
#         return super(MasterDetailMixin, self).get_context_data(**kwargs)


# class MasterDetailView(MasterDetailMixin, generic.DetailView):
#     pass


# class MasterEditView(MasterDetailMixin, generic.UpdateView):
#     def form_valid(self, form):
#         if self.request.is_ajax():
#             self.object = form.save()
#             return self.render_to_response(self.get_context_data(form=form))
#         return super(MasterEditView, self).form_valid(form)

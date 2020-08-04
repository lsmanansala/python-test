import json

from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from python_test.models import Client
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def clients(request, code=None, action=None):
    if request.is_ajax():
        return clients_ajax(request)
    if request.method == "POST":
        if action is None:
            client = Client.objects.filter(client_name=request.POST.get('client_name'))
            if client:
                return HttpResponseRedirect('/already-exists')
            Client.objects.create(
                client_name=request.POST.get('client_name'),
                contact_name=request.POST.get('contact_name'),
                street_name=request.POST.get('street_name'),
                suburb_name=request.POST.get('suburb_name'),
                post_code=request.POST.get('post_code'),
                state=request.POST.get('state'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
            )
        if action == 'edit':
            _client = Client.objects.get(code=code)
            
            _client.client_name = request.POST.get('client_name')
            _client.contact_name = request.POST.get('contact_name')
            _client.street_name = request.POST.get('street_name')
            _client.suburb_name = request.POST.get('suburb_name')
            _client.post_code = request.POST.get('post_code')
            _client.state = request.POST.get('state')
            _client.email = request.POST.get('email')
            _client.phone_number = request.POST.get('phone_number')

            _client.save()
    if (code is not None) and (action is None) and (request.method == 'GET'):
        return client_page(request, code)

   
    return render(request, 'pages/clients.html')


def clients_ajax(request):

    client_list = Client.objects.all()

    json_data = []
    for client in client_list:
        json_data.append({
            'client_name': client.client_name,
            'contact_name': client.contact_name,
            'street_name': client.street_name,
            'suburb_name': client.suburb_name,
            'post_code': client.post_code,
            'state': client.state,
            'email': client.email,
            'phone_number': client.phone_number,
            'code': client.code
        })
    
    data = {
        'data': json_data
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def client_page(request, code=None):
    client = get_object_or_404(Client, code=code)

    context = {
        'client': client
    }

    return render(request, 'pages/client.html', context)


def already_exists(request):

    return render(request, 'components/already_exists.html')
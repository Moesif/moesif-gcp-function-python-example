from flask import Flask, Response, request, make_response
import functions_framework
from functions_framework import create_app
from datetime import *
import json
from moesif_gcp_function.middleware import *

def identify_user(request, response):
    return 'my_user_id'

def identify_company(request, response):
    return 'my_company_id'

def get_api_version(request, response):
    return '1.1.1'

def get_session_token(request, response):
    return '23jdf0owekfmcn4u3qypxg09w4d8ayrcdx8nu2ng]s98y18cx98q3yhwmnhcfx43f'

def get_metadata(request, response):
    return { 'foo' : 'gcp', 'bar' : 'google cloud function metadata', }

def mask_event(event_model):
    return event_model

def should_skip(request, response):
    return "skip" in request.url

moesif_options = {
    'LOG_BODY': True,
    'DEBUG': False,
    'IDENTIFY_USER': identify_user,
    'IDENTIFY_COMPANY': identify_company,
    'GET_METADATA': get_metadata,
    'MASK_EVENT_MODEL': mask_event,
    'GET_SESSION_TOKEN': get_session_token,
    'GET_API_VERSION': get_api_version,
    'SKIP': should_skip
}

@MoesifLogger(moesif_options)
@functions_framework.http
def hello_get(request):

    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """

    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]

    headers = {
        'Content-Type': 'application/json',
        'Custom-Header': 'Custom Value',
        'xx': '1234'
    }

    json_body = json.dumps({'tasks': tasks})
    output = Response(response=json_body, status=201, headers=headers, mimetype='application/json')

    return output

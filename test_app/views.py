from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import TestUser

@api_view(['GET'])
def hello_world(request):
    data = {
        'message': 'Hello, world!'
    }
    return Response(data)


@api_view(['GET'])
def userName(request):
    users = TestUser.objects.all()
    return Response(users)

@api_view(['POST'])
def create_user(request):
    data = {
        "username": "Debby",
        "email": "debby@gmail.com"
    }
    user = TestUser.objects.create(username=data.username, email=data.email)

    return Response(user)

# API Methods
# Response Status Codes
# CRUD operations

# 200 - ok
# 201 - created
# 204 - no content
# 404 - not found
# 500 - internal server error
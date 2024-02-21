from rest_framework import permissions, generics
from .serializers import RegisterSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse

@extend_schema(
    request={
        'application/json': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'email': {'type': 'string'},
                'first_name': {'type': 'string'},
                'last_name': {'type': 'string'},
                'password': {'type': 'string'},
               
            }
        },
    },
    responses={
        200: RegisterSerializer, 
        400: OpenApiResponse(response= 400, description="Bad Request",
            examples= [
                OpenApiExample(name="Example 1", description="Username is required to register user",
                    value= {
                        "username": [
                            "This field may not be blank."
                        ]
                    }
                ),
                OpenApiExample(name="Example 2", description="Password is required to register user",
                    value= { 
                        "password": [
                            "This field may not be blank."
                        ]
                    }
                ),
                OpenApiExample(name="Example 3", description="Username and password is required to register user",
                    value= { 
                        "username": [
                         "This field may not be blank."
                        ],
                        "password": [
                            "This field may not be blank."
                        ]
                    }
                ),
        ]),
    
    },
    description= 
    """
    Endpoint to register user with username, email, first_name, last_name, and password.
    """
)

class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
    
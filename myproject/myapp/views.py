from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import os

@api_view(['GET'])
def get_data(request):
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    
    return Response(data)
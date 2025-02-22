import json

from fastapi import Response

from .common import getData
from fastapi import APIRouter


router = APIRouter()

@router.post('/api/v1/jenkins')
@router.get('/api/v1/jenkins')
async def jobs(pretty: bool = False):
    response = await getData("JENKINS")
    if pretty:
        json_str = json.dumps(response, indent=4)
        return Response(content=json_str, media_type='application/json')
    return response

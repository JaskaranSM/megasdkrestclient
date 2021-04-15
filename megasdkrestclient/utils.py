from .constants import ResponseStatus
from .errors import MegaSdkRestClientException

def constructUrl(endpoint,path):
    return endpoint + '/' + path 

def checkAndRaise(obj,key):
    if obj[key] == ResponseStatus.TYPE_RESPONSE_FAILED:
        raise MegaSdkRestClientException(obj)
    return obj
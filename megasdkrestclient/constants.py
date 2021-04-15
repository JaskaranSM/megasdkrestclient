class ResponseStatus:

    TYPE_RESPONSE_SUCCESS = 'success'
    TYPE_RESPONSE_FAILED = 'failed'

class State:

    TYPE_STATE_NONE = 0
    TYPE_STATE_QUEUED = 1
    TYPE_STATE_ACTIVE = 2
    TYPE_STATE_PAUSED = 3
    TYPE_STATE_RETRYING = 4
    TYPE_STATE_COMPLETING = 5
    TYPE_STATE_COMPLETED = 6
    TYPE_STATE_CANCELED = 7
    TYPE_STATE_FAILED = 8

class RoutePath:
    PATH_LOGIN = 'login'
    PATH_ADD_DL = 'adddl'
    PATH_CANCEL_DL = 'canceldl'
    PATH_DL_INFO = 'dlinfo/{}'
    PATH_PING = 'ping'
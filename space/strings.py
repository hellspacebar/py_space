import uuid

def xstr(s):
    if s is None:
        return ''
    return str(s)

def get_uuid():
    return uuid.uuid4().hex

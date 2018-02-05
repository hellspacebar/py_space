import uuid


class String:

    @staticmethod
    def xstr(s):
        if s is None:
            return ''
        return str(s)

    @staticmethod
    def get_uuid():
        return uuid.uuid4().hex
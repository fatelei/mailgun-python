#-*-coding: utf8-*-


class MGBaseException(Exception):

    def __init__(self, code=code, msg=msg):
        """
        :param code: http status code
        :param msg: detail error message
        """
        self.code = code
        self.msg = msg

    def __str__(self):
        return "code = {0}: message = {1}".format(self.code, self.msg)

    def __repr__(self):
        return "code = {0}: message = {1}".format(self.code, self.msg)


class BadRequestException(MGBaseException):

    def __init__(self, code=400, msg=msg):
        super(BadRequestException, self).__init__(code=code, msg=msg)


class UnauthorizeException(MGBaseException):

    def __init__(self, code=401, msg=msg):
        super(UnauthorizeException, self).__init__(code=code, msg=msg)


class RequestFailedException(MGBaseException):

    def __init__(self, code=402, msg=msg):
        super(RequestFailedException, self).__init__(code=code, msg=msg)


class NotFoundException(MGBaseException):

    def __init__(self, code=404, msg=msg):
        super(NotFoundException, self).__init__(code=code, msg=msg)


class ServerErrorsException(MGBaseException):

    def __init__(self, code=code, msg=msg):
        super(ServerErrorsException, self).__init__(code=code, msg=msg)

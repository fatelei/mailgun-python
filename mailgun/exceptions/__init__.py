#-*-coding: utf8-*-


"""
custom exceptions

usage:

    >>> from mailgun.exceptions import BadRequest
    >>> raise BadRequest("missing a required parameter")

"""

from .exceptions import BadRequestException
from .exceptions import NotFoundException
from .exceptions import RequestFailedException
from .exceptions import ServerErrorsException
from .exceptions import UnauthorizeException

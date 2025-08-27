from enum import Enum


class HttpStatusCode(int, Enum):
    # 2XX Success status codes
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    # 3XX Redirection status codes
    MULTIPLE_CHOICES = 300
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308
    # 4xx Client error status codes
    BAD_REQUEST = 400
    Unauthorized = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    # 5XX Server error status codes
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

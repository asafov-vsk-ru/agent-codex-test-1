from enum import Enum


class ContentType(str, Enum):
    JSON = "application/json"
    XML = "application/xml"
    TEXT = "application/text"
    FORM = "application/x-www-form-urlencoded"

import allure
import json

from requests import Response
from allure_commons.types import AttachmentType


class Helper:

    @staticmethod
    def attach_response(response: Response):
        response_body = json.dumps(response.text, indent=4)
        content_type = response.headers.get("Content-Type")
        if content_type == "application/json":
            attachment_type = AttachmentType.JSON
        elif content_type == "application/xml":
            attachment_type = AttachmentType.XML
        else:
            attachment_type = AttachmentType.TEXT
        allure.attach(body=response_body, name="API Response", attachment_type=attachment_type)

from requests import Response

from core.rest.config.content_type import ContentType
from core.utils.allure_helper import Helper
from core.utils.config_helper import logger


class ApiMethods:

    def __init__(self, host: str):
        self.host = host

    def validate_response(self, response: Response, status_code: int = 200, content_type: str = ContentType.JSON):
        assert response is not None, ("Response is empty!", logger().info("Response is empty!"))
        assert response.status_code == status_code, \
            (f"Response status-code is not equal {status_code}! {Helper.attach_response(response)}",
             logger().info(f"Response status-code is not equal {status_code}!"))
        assert response.headers.get("Content-Type") == content_type, \
            (f"Response content-type is not equal {content_type}! {Helper.attach_response(response)}",
             logger().info(f"Response content-type is not equal {content_type}!"))
        return response

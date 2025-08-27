from enum import Enum


class ApiEndpoints(str, Enum):
    # pet api endpoints
    UPLOAD_PET_IMAGE = "{host}/pet/{pet_id}/uploadImage"
    CREATE_PET = "{host}/pet"
    UPDATE_EXISTING_PET = "{host}/pet"
    FIND_PET_BY_STATUS = "{host}/pet/findByStatus"
    FIND_PET_BY_TAGS = "{host}/pet/findByTags"
    GET_PET_BY_ID = "{host}/pet/{pet_id}"
    UPDATE_PET_IN_STORE = "{host}/pet/{pet_id}"
    DELETE_PET = "{host}/pet/{pet_id}"

    # store api endpoints
    STORE_INVENTORY = "{host}/store/inventory"
    CREATE_STORE_ORDER = "{host}/store/order"
    GET_ORDER_BY_ID = "{host}/store/order/{order_id}"
    DELETE_ORDER = "{host}/store/order/{order_id}"

    # user api endpoints
    CREATE_USERS_WITH_LIST = "{host}/user/createWithList"
    GET_USER_BY_NAME = "{host}/user/{user_name}"
    UPDATE_USER = "{host}/user/{user_name}"
    DELETE_USER = "{host}/user/{user_name}"
    LOGIN_USER = "{host}/user/login"
    LOGOUT_USER = "{host}/user/logout"
    CREATE_USERS_WITH_ARRAY = "{host}/user/createWithArray"
    CREATE_USER = "{host}/user"

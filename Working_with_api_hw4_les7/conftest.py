import pytest
import requests


# class APIClient:
#     """
#     Упрощенный клиент для работы с API
#     Инициализируется базовым url на который пойдут запросы
#     """
#     def __init__(self, base_address):
#         self.base_address = base_address
#
#     def post(self, path="/", params=None, data=None, headers=None):
#         url = self.base_address + path
#         return requests.post(url=url, params=params, data=data, headers=headers)
#
#     def get(self, path="/", params=None):
#         return requests.get(url=self.base_address + path, params=params)



def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://dog.ceo/api",
        help="This is request url"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))




# def pytest_addoption(parser):
#     parser.addoption(
#         "--url",
#         default="https://httpbin.org/",
#         help="This is request url"
#     )
#
#     parser.addoption(
#         "--method",
#         default="get",
#         choices=["get", "post", "put", "patch", "delete"],
#         help="method to execute"
#     )
#
#
# @pytest.fixture
# def base_url(request):
#     return request.config.getoption("--url")
#
#
# @pytest.fixture
# def request_method(request):
#     return getattr(requests, request.config.getoption("--method"))

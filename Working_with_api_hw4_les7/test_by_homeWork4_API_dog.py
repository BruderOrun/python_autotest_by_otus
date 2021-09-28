import pytest
import requests


@pytest.mark.parametrize("code", [200, 300, 400, 404, 500, 502])
def test_url_status(base_url, code, request_method):
    target = base_url + f"/status/{code}"
    print(target)
    response = requests.get(url=target)
    assert response.status_code == code


def test_api_one__all_sub_breeds_dog(base_url, request_method):
    """Description: тест по домашнему заданию № 4 api: https://dog.ceo/dog-api/. запрос на все изображения пород,
    получаем список всех изображений и статус успешно выполненого запроса"""
    res = request_method(url=base_url + "/breed/hound/list").json()
    assert res['status'] == "success"
    assert res['message'] == ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker']


@pytest.mark.parametrize('input_image, output_code',
                         [("n02088094_1003.jpg", 200), (" ", 403), ("dfdbfbngn", 404)], ids=["200", "403", "404"])
def test_api_two_image_breeds(base_url, request_method, input_image, output_code):
    """Description: тест по домашнему заданию № 4 api: https://dog.ceo/dog-api/. запрос возаращает изображений из породы afghan:
    проверяем корректный ответ по конктреному изображению, запрос без изображения и некорректное имя изображения"""
    res = request_method(url=base_url + "/breeds/hound-afghan/" + input_image)
    # res.status_code = output_code
    assert res.status_code == output_code


@pytest.mark.parametrize('input, output',
                         [("random", "success"), ("", "error"), ("dfdbfbngn", "error")])
def test_api_three_image_breeds_random(api_client, input, output):
    """Description: тест по домашнему заданию № 4 api: https://dog.ceo/dog-api/. запрос возаращает изображений из породы afghan:
    проверяем корректный ответ по конктреному изображению, запрос без изображения и некорректное имя изображения"""
    res = api_client.get(path="/breeds/image/" + input).json()
    assert res['status'] == output


def test_api_four_list_all_breeds(api_client):
    """Description: тест по домашнему заданию № 4 api: https://dog.ceo/dog-api/. запрос на все породы, получаем список
     всех пород и статус успешно выполненого запроса"""
    res = api_client.get(path="/breeds/list/all").json()
    # Проверяем что возвращаемые параметры верны
    assert res['status'] == "success"


def test_api_five_list_all_breeds(api_client):
    """Description: тест по домашнему заданию № 4 api: https://dog.ceo/dog-api/. запрос на все изображения пород,
    получаем список всех изображений и статус успешно выполненого запроса"""
    res = api_client.get(path="/breed/hound/images").json()
    # Проверяем что возвращаемые параметры верны
    assert res['status'] == "success"

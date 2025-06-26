# post related test cases
import json
import pytest
from api_testing_framework.apis.post_api import PostAPI


@pytest.fixture(scope='module')
def post_api():
    return PostAPI()

def test_get_all_posts(post_api):
    response = post_api.get_all_posts()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post(post_api):
    with open('data/post_data.json') as f:
        data = json.load(f)
    response = post_api.create_post(data=data)
    assert response.status_code == 201
    assert response.json()['title'] == data['title']

def test_update_post(post_api):
    update_data = {"title": "updated_title"}
    response = post_api.update_post(post_id=1, data=update_data)
    assert response.status_code == 200
    assert response.json()['title'] == update_data['title']

def test_delete_data(post_api):
    res = post_api.delete_post(1)
    assert res.status_code in [200, 204]

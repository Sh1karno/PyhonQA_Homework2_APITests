import pytest
import random

from unittest.mock import patch
from mocks.mock_dogs_response import MockDogsResponse


@pytest.mark.dogs
class TestDogsAPI:

    @patch("wrappers.dogs.Dogs.get_all_breeds_list")
    def test_list_all_breed(self, dogs, status_code):
        dogs.get_all_breeds_list.return_value = MockDogsResponse(95)
        response = dogs.get_all_breeds_list()
        json_response = response.json()
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert json_response['status'] == 'success'
        assert len(json_response['message']) == 95

    @patch("wrappers.dogs.Dogs.get_multiple_img_from_breeds")
    def test_multiple_random_img_from_breed(self, dogs, status_code):
        random_count = random.randint(1, 10)
        dogs.get_multiple_img_from_breeds.return_value = MockDogsResponse(random_count)
        response = dogs.get_multiple_img_from_breeds(random_count)
        json_response = response.json()
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert json_response['status'] == 'success'
        assert len(json_response['message']) == random_count

    @patch("wrappers.dogs.Dogs.get_img_from_breed")
    def test_random_img_from_breed(self, dogs, status_code, random_breed):
        dogs.get_img_from_breed.return_value = MockDogsResponse()
        response = dogs.get_img_from_breed(random_breed)
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert response.json()['status'] == 'success'

    @patch("wrappers.dogs.Dogs.get_all_sub_breeds_list")
    @pytest.mark.parametrize("sub_breed, count_sub_breed", [('hound', 7), ('poodle', 3), ('retriever', 4)])
    def test_all_sub_breeds_list(self, dogs, status_code, sub_breed, count_sub_breed):
        dogs.get_all_sub_breeds_list.return_value = MockDogsResponse(count_sub_breed)
        response = dogs.get_all_sub_breeds_list(sub_breed)
        json_response = response.json()
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert json_response['status'] == 'success'
        assert len(json_response['message']) == count_sub_breed

    @patch("wrappers.dogs.Dogs.get_img_from_sub_breed")
    @pytest.mark.parametrize("breed, sub_breed", [('hound', 'afghan'), ('hound', 'blood'), ('bulldog', 'french')])
    def test_random_img_from_sub_breed(self, dogs, status_code, breed, sub_breed):
        dogs.get_img_from_sub_breed.return_value = MockDogsResponse()
        response = dogs.get_img_from_sub_breed(breed, sub_breed)
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert response.json()['status'] == 'success'

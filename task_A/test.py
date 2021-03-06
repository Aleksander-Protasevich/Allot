import requests
import pytest
import json


def test_create_user():
    response = requests.post("https://petstore.swagger.io/v2/user", json = {
  "id": 2,
  "username": "Ivan7",
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "email": "string",
  "password": "Ivan777",
  "phone": "string",
  "userStatus": 0
  })
    assert response.status_code == 200

def test_get_user():
    response = requests.get("https://petstore.swagger.io/v2/user/Ivan7")
    assert response.status_code == 200

def test_update_user():
    response = requests.put("https://petstore.swagger.io/v2/user/Ivan7", json = {
  "id": 2,
  "username": "Ivan7",
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "email": "string",
  "password": "Ivan777",
  "phone": "+375291111111",
  "userStatus": 0
  })
    assert response.status_code == 200
    
def test_delete_user():
    response = requests.delete("https://petstore.swagger.io/v2/user/Ivan7")
    assert response.status_code == 200    
    
    
    
    











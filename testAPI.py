#!/usr/bin/python3

import requests
import sys
import json

dataCreate = sys.argv[1]
dataUpdate = sys.argv[2]

def is_json(data):
    assert json.loads(data), "Data must be in Json"
    print('OK : Data is in Json')
    return True

def testCreate(data):
    url = "http://rest-bookmarks.herokuapp.com/api/bookmarks/"
    data = {'name': 'Raphael', 'description': 'cc', 'url': 'http://www.raphael.com'}
    test = requests.post(url, data=data)
    assert test.status_code == 201, 'Server should return 201 status code after POST request'
    url2 = test.headers['Location']
    test2 = requests.get(url2)
    assert test2.status_code == 200, 'Server should return 200 status code after GET request to Bookmark url'
    assert test2.json() == data, 'Bookmark data should be equal to data send previously'
    print('OK : Bookmark successfully added')
    return True, url2

def testUpdate(url, data):
    data = {"name": "test update", 'description': 'raph update', 'url': 'http://raph.update'}
    test = requests.put(url, data=data)
    assert test.status_code == 204, 'Server should return 204 status code after updating data with PUT method'
    test2 = requests.get(url)
    assert test2.json() == data, 'Bookmark data should be equal to new'
    print('OK : Bookmark successfully updated')
    return True

def testDelete(url):
    test = requests.delete(url)
    assert test.status_code == 204, 'Server should return 204 status code after deleting bookmark with DELETE method'
    test2 = requests.get(url)
    assert test2.status_code == 404, 'Server should return 404 status code after using GET method on previously Bookmark'
    print('OK : Bookmark successfully deleted')
    return True

is_json(dataCreate)
(useless, urlB) = testCreate(dataCreate)
testUpdate(urlB, dataUpdate)
testDelete(urlB)


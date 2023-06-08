import requests
from typing import List


def api(url_lst:List[str]):
    for url in url_lst:
        print(url)
        get_response=requests.get(url)
        if get_response:

            print("Get response was successful!")
            print(f"Get response status code: {get_response.status_code}")
            # print(get_response.content.decode('utf-8')) #str format
            # print(get_response.json())#json format
        else:

            print("Get response was not successful!")
            print(f"Get response status code: {get_response.status_code}")


        my_json = {'name': 'farzam'}
        post_response = requests.post(url,json = my_json)
        if post_response:

            print("Post response was successful!")
            print(f"Post response status code: {post_response.status_code}")
            # print(post_response.content.decode('utf-8'))#str format
            # print(post_response.json())#json format
        else:

            print("Post response was not successful!")
            print(f"Post response status code: {post_response.status_code}")

        print("****************************************************************")



urls = ['https://api.thecatapi.com/v1','https://jsonplaceholder.typicode.com/users']

api(urls)
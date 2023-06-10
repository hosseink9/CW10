import requests

url1 = "https://api.thecatapi.com/v1"
url2 = "https://jsonplaceholder.typicode.com/users"
url3 = "https://reqbin.com/"


def dict_to_str(dictionary: dict, space=0) -> str:
    result = ""
    for item in dictionary.items():
        if isinstance(item[1], dict):
            result += str(" " * space) + str(item[0]) + ": ▼\n"
            result += dict_to_str(item[1], space + len(item[0])+3)
        else:
            result += str(" " * space) + str(item[0]) + ": " + str(item[1]) + '\n'
    return result


def api_caller(url: str, mode="get") -> (requests, str):
    req = {"get": requests.get, "post": requests.post}
    res = ""
    result = req[mode](url)
    if result.status_code == 200:
        result = result.json()[0]
        res = "Successful"
    else:
        response = {403: "Permission denied", 404: "Not found"}
        res = response[result.status_code]
    return result, res


if __name__ == '__main__':
    data = api_caller(url1)
    data2 = api_caller(url2)
    data3 = api_caller(url3, "post")
    print(data3[0], data3[1])
    print(dict_to_str(data2[0]), data2[1])







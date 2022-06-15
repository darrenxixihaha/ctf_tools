import requests


def get(url=None, params=None, **kwargs) -> str:
    return requests.get(url, params, **kwargs).content.decode()


def post_form(url=None, params=None, **kwargs) -> str:
    return ""


def post_json(url=None, params=None, **kwargs) -> str:
    return ""


if __name__ == "__main__":
    result = get("https://www.baidu.com", params=dict())
    print(result)
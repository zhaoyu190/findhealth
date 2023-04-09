

import requests

# ISBN书号查询 Python示例代码
if __name__ == '__main__':
    url = 'http://jmisbn.api.bdymkt.com/isbn/query'
    params = {'isbn': '9787555357902'}

    headers = {

        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/9e0959682a41415a97214a2745af2710'
    }
    r = requests.request("POST", url, params=params, headers=headers)
    print(r.content)
    print(r.status_code)

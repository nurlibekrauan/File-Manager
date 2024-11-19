import requests
from pprint import pprint

# print(response.status_code)
# if response.ok:
    # print('do something with')
    
# print(response.text)
# print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
# print(response.content)

# print(response.text)
# response_json = response.json()

# pprint(response_json)

# print(type(response_json))

# print(response_json.get('hub_url','error'))
# hub_url_response = requests.get(response_json.get('hub_url','error'))
# print(hub_url_response.status_code)

# print(response_json['repository_search_url'])

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Content-Length": "49",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "Origin": "https://httpbin.org",
    "Priority": "u=0, i",
    "Referer": "https://httpbin.org/forms/post",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-672f5fa7-3d22fd2960a512a572095652"
}

params = {'q':'python'}

response = requests.get('http://api.github.com/search/repositories',params=params)
print(response.status_code)
response_json = response.json()

pprint(response_json)
# pprint(response.text)

# print('\n\n\n\n\n\n')

# for k,v in response.headers.items():
#     print(f'{k} : {v}')
# print('\n\n\n\n')

# # for k,v in response.request.headers.items():
# #     print(f'{k} : {v}')
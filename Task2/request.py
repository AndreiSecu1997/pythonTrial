import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen

http_proxy  = "194.153.100.20:80"
https_proxy = "203.26.189.28:3128"

basePetStoreUrl = 'https://petstore.swagger.io'
baseJsonPlaceHOlder = 'https://jsonplaceholder.typicode.com'

proxies = {
  "http": http_proxy,
  "https": https_proxy
}
def GET(url):
    return requests.get(url,proxies=proxies).text

def POST(url, body):
    return requests.post(url, urlencode(body).encode())

def PUT(url, body):
    return requests.post(url, urlencode(body).encode())

if __name__ == "__main__":
    # Perform a get request by using https proxy
    # print(basePetStoreUrl + '/v2/store/inventory')
    # print(GET(basePetStoreUrl + '/v2/store/inventory'))
    # print(GET(baseJsonPlaceHOlder + '/posts'))

    # Perform a POST request by using https proxy
    response = POST(baseJsonPlaceHOlder + '/posts', {'title': 'titleName', 'body': 'text body', 'userId': 1})
    print(response)
    print(response.text)


    # Perform a PUT request by using https proxy
    response = PUT(baseJsonPlaceHOlder + '/posts', {'id': 1, 'title': 'titleName', 'body': 'text body', 'userId': 1})
    print(response)
    print(response.text)






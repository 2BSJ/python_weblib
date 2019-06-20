from urllib.parse import urlencode
from urllib.request import urlopen, Request

#GET request가 필요가없음
httpresponse = urlopen('http://www.example.com?a=10&b=20')
body = httpresponse.read()
print(body)


# post
data = {
    'email' : 'yyg0825@naver.com',
    'password' : '1234',
    'name' : '양승준'
}
data = urlencode(data).encode('utf-8')

request= Request('http://www.example.com',data)
request.add_header('Content-Type', 'text/html')

httpresponse = urlopen(request)
print(httpresponse.read())
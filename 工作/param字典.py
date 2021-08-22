import requests

def get_headers(header_raw):
    """
    通过原生请求头获取请求头字典
    :param header_raw: {str} 浏览器请求头
    :return: {dict} headers
    """
    
    return dict(line.split(": ", 1) for line in header_raw.split("\n") if line != '')

header_raw ='''Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/5'''    

data = '''autocomplete-dropdown: Ghana
AuthenticationFG.COUNTRY: GH
AuthenticationFG.USER_PRINCIPAL: WANHENG.YAN
Action.STU_VALIDATE_CREDENTIALS: Login
'''

session = requests.session()

b = get_headers(header_raw)
#print(b)
c = get_headers(data)
#print(c)
url = 'https://ibank.ubagroup.com/eng/AuthenticationController'

#re = requests.post(url,data=c,headers=b)
re = session.post(url, headers=b, data=c)
print(re.status_code)
print(re.text)
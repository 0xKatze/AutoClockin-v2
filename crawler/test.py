import requests
from bs4 import BeautifulSoup
import ddddocr
import urllib.request

def validateCode():
    urllib.request.urlretrieve("https://course.fcu.edu.tw/validateCode.aspx",
    "1.png")
    ocr = ddddocr.DdddOcr()
    with open('1.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    
    return res

def printCode(result):
    soup3 = BeautifulSoup(result.text, "html.parser")
    print(soup3)
    #print(result.headers)
    #print(result.cookies)
    
    if result.history:
        print("Request was redirected")
        for resp in result.history:
            print(resp.status_code, resp.url)
        print("Final destination:")
        print(result.status_code, result.url)
    else:
        print("Request was not redirected")
    
    
    #result = session_requests.get(STUDENT_URL)
    print(result.history)
    #soup = BeautifulSoup(result.text, "html.parser")
    #print(soup.prettify())
    print(result.status_code)



def main():
    USER = input('Username:')
    PASSWORD = input('Password:')
    LOGIN_URL = 'https://signin.fcu.edu.tw/clockin/login.aspx'
    STUDENT_URL = 'https://signin.fcu.edu.tw/clockin/Student.aspx'
    session_requests = requests.session()
    #result = session_requests.get(LOGIN_URL)
    #soup = BeautifulSoup(result.text, "html.parser")
    #print(soup.prettify())
    
    login = session_requests.get(LOGIN_URL)
    soup = BeautifulSoup(login.text, "html.parser")
    viewstate = soup.find_all('input', {"type": "hidden", "name": "__VIEWSTATE"})[
        0]['value']
    eventvalids = soup.find_all('input', {"type": "hidden", "name": "__EVENTVALIDATION"})[
        0]['value']
    
    payload = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    #change v
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': '1C86B585',
    #change v
    '__EVENTVALIDATION': eventvalids,
    'LoginLdap$UserName': USER,
    'LoginLdap$Password': PASSWORD,
    'LoginLdap$LoginButton': '登入',
    }
    
    headers = {
    'Content-Type': 'application/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '635',
    'Content-Type': 'application/x-www-form-urlencoded',
    #'Cookie': 'ga=GA1_.3.1895667935.1638191181; _gid=GA1.3.1056711139.1638970174; ASP.NET_SessionId=rnla4zhzvkvpkfmspj4q5axo; FCU_WAF=SCg9VBNGYl7RfD+l9qEZNH/2R/g0004; _gat=1',
    'Host': 'signin.fcu.edu.tw',
    'Origin': 'https://signin.fcu.edu.tw',
    'Referer': 'https://signin.fcu.edu.tw/clockin/login.aspx',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    result = session_requests.get(LOGIN_URL)
    result = session_requests.post(LOGIN_URL, data = payload, headers=headers)
    #print(result.text)
    #stuck at here
    CHECK_URL = 'https://signin.fcu.edu.tw/clockin/Student.aspx'
    # result = session_requests.get(CHECK_URL)
    #print(result.text)
    soup2 = BeautifulSoup(result.text, "html.parser")
    #print(soup2)
    viewstate2 = soup2.find_all('input', {"type": "hidden", "name": "__VIEWSTATE"})[0]['value']
    #print(viewstate2)
    eventvalids2 = soup2.find_all('input', {"type": "hidden", "name": "__EVENTVALIDATION"})[0]['value']
    #for i in eventvalids2:
    #print(i.value)
    #print(eventvalids2)
    payload2 = {
	"__VIEWSTATE": viewstate2,
	"__VIEWSTATEGENERATOR": "CC355973",
	"__EVENTVALIDATION": eventvalids2,
	"ButtonClassClockin": "學生課堂打卡"
    }
    
    result = session_requests.post(CHECK_URL, data = payload2, headers=headers)
    
    soup3 = BeautifulSoup(result.text, "html.parser")
    #print(soup2)
    viewstate3 = soup3.find_all('input', {"type": "hidden", "name": "__VIEWSTATE"})[0]['value']
    #print(viewstate2)
    eventvalids3 = soup3.find_all('input', {"type": "hidden", "name": "__EVENTVALIDATION"})[0]['value']
    #for i in eventvalids2:
    #print(i.value)
    #print(eventvalids2)
    button0 = soup3.find_all('input', {"type": "submit", "name": "Button0"})[0]['value']
    payload3 = {
	"__VIEWSTATE": viewstate3,
	"__VIEWSTATEGENERATOR": "CE180C50",
	"__EVENTVALIDATION": eventvalids3,
	"Button0": "學生課堂打卡",
    "validateCode": validateCode(),
    "Button0": button0
    }
    
    
    #printCode(result)
    
    CLOCK_URL = "https://signin.fcu.edu.tw/clockin/ClassClockin.aspx"
    result = session_requests.post(CLOCK_URL, data = payload3, headers=headers)
    if result.status_code is 200:
        print("CLOCKIN successful")
        
    printCode(result)
    """
    soup3 = BeautifulSoup(result.text, "html.parser")
    print(soup3)
    #print(result.headers)
    #print(result.cookies)
    
    if result.history:
        print("Request was redirected")
        for resp in result.history:
            print(resp.status_code, resp.url)
        print("Final destination:")
        print(result.status_code, result.url)
    else:
        print("Request was not redirected")
    
    
    #result = session_requests.get(STUDENT_URL)
    print(result.history)
    #soup = BeautifulSoup(result.text, "html.parser")
    #print(soup.prettify())
    print(result.status_code)
    """
    
    print()
    #print(soup.text, "html.parser")
    """
    response = requests.get(
        "https://signin.fcu.edu.tw/clockin/login.aspx")
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())
    """
if __name__ == "__main__":
    main()
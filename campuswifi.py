import requests
import wifi
import logger as log

_ipaddr = ""
_ssid = ""
_password = ""
_uid = ""
_upassword = ""
_cookie_rn = ""

def connect(ssid, password, userid, userpassword):
    
    global _ipaddr
    global _ssid
    global _password
    global _uid
    global _upassword
    global _cookie_rn
    
    _ssid = ssid
    _password = password
    _uid = userid
    _upassword = userpassword

    ret = wifi.connect(_ssid, _password)
    if not ret:
        log.error("Fail to connect to campus wifi!")
        return False
    _ipaddr = wifi.ipaddr
    
    ret = wifi.ping()
    if ret == True:
        return True
    
    log.info("Logging into campus wifi·····")
    ret = _login()
    if ret:
        log.info("Login Success!")
    else:
        return False

    log.info("Submmitting·····")
    ret = _submit()
    if ret:
        log.info("Submit Success!")
    else:
        return False

#     log.info("Testing for the Internet·····")
#     wifi.ping()
    return True

def _login():
    
    global _ipaddr
    global _uid
    global _upassword
    global _cookie_rn
    
    login_url = "http://202.38.64.59/cgi-bin/ip"
    login_data = "cmd=login&url=URL&ip={ip}&name={uid}&password={upassword}&go=%B5%C7%C2%BC%D5%CA%BB%A7".format(ip = _ipaddr, uid = _uid, upassword = _upassword)
    login_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        #"Content-Length": str(len_test), #str(len(login_data)),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "name=; password=",
        "Host": "202.38.64.59",
        "Origin": "http://202.38.64.59",
        "Referer": "http://202.38.64.59/cgi-bin/ip",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    ret = 1
    rq = requests.request(method = "POST", url = login_url, headers=login_headers, data = login_data)
    if rq.status_code != 200:
        log.error("In _login(): \n    login failed with status code {sc}, \n    headers:\n{hd} \n    text:\n{tx}".\
              format(sc = rq.status_code, hd = rq.headers, tx = rq.text))
        ret = 0
  
    if "Set-Cookie" in rq.headers:
        _cookie_rn = rq.headers["Set-Cookie"]
    else :
        log.error("Login Failed!\nNo cookie in headers! \n    headers:\n{hd}\n    text:\n{tx}".format(hd = rq.headers, tx = rq.text))
        ret = 0
    rq.close()
    return ret

def _submit():
    
    global _ipaddr
    global _uid
    global _upassword
    global _cookie_rn
    
    if len(_cookie_rn) == 0:
        raise ValueError("Please Login() before Submit()!")
    
    submit_url = r"http://202.38.64.59/cgi-bin/ip?cmd=set&url=URL&type=8&exp=0&go=+%BF%AA%CD%A8%CD%F8%C2%E7+"
    submit_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'name=; password=; {rn}'.format(rn = _cookie_rn),
        'Host': '202.38.64.59',
        'Referer': 'http://202.38.64.59/cgi-bin/ip',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    submit_data = "cmd=set&url=URL&type=8&exp=0&go=+%BF%AA%CD%A8%CD%F8%C2%E7+"
    
    ret = 1
    rq = requests.get(submit_url, headers = submit_headers, data = submit_data)
    if rq.status_code != 200:
        log.error("In _submit(): \n    submit failed with status code {sc}, \n    headers:\n{hd} \n    text:\n{tx}".\
              format(sc = rq.status_code, hd = rq.headers, tx = rq.text))
        ret = 0
    rq.close()
    return ret

def _logout():
    
    global _ipaddr
    global _uid
    global _upassword
    global _cookie_rn
    
    if len(_cookie_rn) == 0:
        raise ValueError("Please Login() before Submit()!")
    
    logout_url = "http://202.38.64.59/cgi-bin/ip?cmd=logout"
    logout_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'name=; password=; {rn}'.format(rn = _cookie_rn),
        'Host': '202.38.64.59',
        'Referer': 'http://202.38.64.59/cgi-bin/ip?cmd=set&url=URL&type=8&exp=0&go=+%BF%AA%CD%A8%CD%F8%C2%E7+',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }
    logout_data = "cmd=logout"
    
    ret = 1
    rq = requests.get(logout_url, headers = logout_headers, data = logout_data)
    if rq.status_code != 200:
        log.error("In _logout(): \n    logout failed with status code {sc}, \n    headers:\n{hd} \n    text:\n{tx}".\
              format(sc = rq.status_code, hd = rq.headers, tx = rq.text))
        ret = 0
    rq.close()
    return ret

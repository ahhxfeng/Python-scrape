#urllib.request 模块下载URL

import urllib.request
def download(url):
    print ('Downloading:',url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:    
        print ('Download error:', e.reason)
        html = None 
    return html

#html = download("http://www.baidu.com")
#print(html)
#遇到5xx的错误码是，重试num_retries次
def download_retry(url, num_retries):
    print('downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('downloading error', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                #recursivvely retry 5xx HTTP errors
                return download_retry(url, num_retries - 1)
    return html

#html = download_retry('http://httpstat.us/500', 4)
#html = download_retry('http://www.meetup.com', 4)
#设置用户代理
def download_proxy(url, user_agent, num_retries):
    print('downloading:', url)
    headers = {'User_agent:', user_agent}
    request = urllib.request.Request(url, headers = headers)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download_proxy(url, user_agent, num_retries - 1)
    return html
html = download_proxy('http://www.baidu.com', 'wswp', 3)
print(html)


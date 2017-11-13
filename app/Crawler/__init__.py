from urllib import request;


def getWeb():
    open = request.Request('https://www.baidu.com')
    open.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    open.add_header('Upgrade-Insecure-Requests', '1')
    open.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
    open.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
    response = request.urlopen(open)
    with response as f:
        print(f.read().decode('utf-8'))

if __name__ == "__main__":
    getWeb()


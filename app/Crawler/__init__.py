from urllib import request;
from bs4 import BeautifulSoup;
import sqlite3;
import sys;

sys.setrecursionlimit(5000)
CrawInfo = []
Current = set()
LinkArr = set()
OldArr = set()
conn = sqlite3.connect('example.db')
c = conn.cursor()

def getWeb(url):
    try:
        open = request.Request(url)
        open.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        open.add_header('Upgrade-Insecure-Requests', '1')
        open.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
        open.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
        response = request.urlopen(open)
        OldArr.add(url)
        with response as f:
            html = f.read().decode('utf-8')
            print(f.read().decode('utf-8'))
            decodeHtml(html)
    except Exception:
        print('爬取出错啦, 跳过获取')
        newUrl = LinkArr.pop()
        getWeb(newUrl)


def decodeHtml(html):
    global LinkArr
    global Current
    global OldArr

    if CrawInfo.__len__() <= 2000:
        try:
            soup = BeautifulSoup(html, "html.parser")
            dic = {}

            if soup.select('.lemmaWgt-lemmaTitle-title h1').__len__() >= 0:
                dic['title'] = soup.select('.lemmaWgt-lemmaTitle-title h1')[0].string
            if soup.select('[label-module=lemmaSummary]').__len__() >= 0:
                dic['intro'] = soup.select('[label-module=lemmaSummary]')[0].get_text()

            CrawInfo.append(dic)

            c.execute("INSERT INTO crawler (id, title, content) values(null,?,?)", (dic['title'], dic['intro']))
            conn.commit()

            links = soup.select('a[href^="/item/"]')
            for link in links:
                Current.add('https://baike.baidu.com' + link['href'])


            if LinkArr.__len__() == 0:
                LinkArr = Current
                Current = set()

            print('当前进度:' + str(CrawInfo.__len__()))
            print('OldArr长度:' + str(OldArr.__len__()))
            print('LinkArr长度' + str(LinkArr.__len__()))
            print('Current长度' + str(Current.__len__()))
            newUrl = LinkArr.pop()
            OldArr.add(newUrl)


            print('爬取成功')
            getWeb(newUrl)

        except Exception:
            print('爬取出错啦, 跳过获取')
            newUrl = LinkArr.pop()
            getWeb(newUrl)
    else:
        with open('data.txt', 'w', encoding="utf-8") as f:
            f.write(CrawInfo.__str__())
            conn.close()


if __name__ == "__main__":
    tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='crawler'"
    c.executescript('drop table if exists crawler;')

    if not c.execute(tb_exists).fetchone():
        c.execute('''CREATE TABLE crawler (
            id INTEGER PRIMARY KEY,
            title text,
            content text
        )
        ''')

    url = 'https://baike.baidu.com/item/%E7%88%B1%E7%89%B9%E5%AE%89%E4%B8%BA/4734384?fr=aladdin'
    getWeb(url)
    # decodeHtml()

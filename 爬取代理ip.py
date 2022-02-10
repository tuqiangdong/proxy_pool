import requests
from lxml import etree

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
}
url = 'http://www.66ip.cn/areaindex_19/1.html'
resp = requests.get(url, headers=head)
resp.encoding = 'gbk'
html = etree.HTML(resp.text)
trs = html.xpath('//*[@id="footer"]/div/table/tr')[1:]
# print(trs)
ip_list = []
for i in trs:
    print(i)
    temp = i.xpath('./td/text()')
    ip_pro = temp[0]+':'+temp[1]
    print(ip_pro)
    ip_list.append(ip_pro)
s = float(resp.elapsed.microseconds/1000000)
print(resp.elapsed.microseconds)
print(s)
resp.close()
ip = "202.55.5.209:8090"
for i in ip_list:
    print(i, 'testing')
    pro = {
        "http": f"http://{i}",
        "https": f"https://{i}",
    }
    try:
        resp = requests.get(url, headers=head, proxies=pro, timeout=10)
    except Exception as e:
        print(e)
        print(f'{i} fail')
        resp = None
    if resp:
        # print(resp.status_code)
        # print(float(resp.elapsed.microseconds / 1000000), '秒')
        print(f'{i} success timecost:{float(resp.elapsed.microseconds / 1000000)}秒')
        resp.close()

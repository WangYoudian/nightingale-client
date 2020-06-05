# -*- coding:utf-8 -*-
# Author:   Bruce Wang
# Date  :   2020/6/5
from openfalconclient.client import FalconClient
from urllib.parse import urlparse


URL_BASE = 'http://116.85.67.78:80/'
GROUP_PORTAL = 'api/portal/'
portal_urls = [
    ['get', 'self/profile', None],
    ['get', 'collect', None]
]
cli = FalconClient(endpoint="http://116.85.67.78:80/", user='root', password='root')


def call_request(method, url, data=None):
    """使用FalconClient的句柄进行操作
    注意：变量名会作为FalconClient对象的_keys私有属性，故而这里采用'[]'进行调用
    :param method:
    :param url:
    :param data:
    :return:
    """
    chain = [cli]
    for param in urlparse(url).path.split('/')[1:]:
        chain.append(chain[-1][param])

    if method.lower() == 'put' or method.lower() == 'post':
        return chain[-1][method](data=data)
    return chain[-1][method]()


for fake_request in portal_urls:
    method, route, data = fake_request
    url = URL_BASE + GROUP_PORTAL + route
    print('url： %s' % url)
    print('method： %s' % method)
    result = call_request(method, url, data)
    print(result)

from openfalconclient.client import DummyClient


cli = DummyClient()
#
url, method = cli.template['7'].delete()
print(url, method)

url, method = cli.template.a.delete()
print(url, method)

print(dict(method=['GET', 'HEAD']))

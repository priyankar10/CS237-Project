from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683
path ="basic"

client = HelperClient(server=(host, port))
response = client.get(path=path,flag=1)
print response.pretty_print()
client.stop
from filestack import Client
client = Client('<YOUR_API_KEY>')

new_filelink = client.upload(filepath="path/to/file")
print(new_filelink.url)
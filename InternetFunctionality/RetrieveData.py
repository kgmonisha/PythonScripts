import urllib.request

sampleUrl = "https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse"
resp = urllib.request.urlopen(sampleUrl)

print(resp.status)
print(resp.getheaders())
print(resp.getheader("Content-Type"))
print(resp.header['ETag'])



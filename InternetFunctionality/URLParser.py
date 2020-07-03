from urllib.parse import urlparse
import urllib.parse

sampleurl = "https://www.linkedin.com:8080/learning/python-standard-library-essential-training/working-with-urls"

result = urlparse(sampleurl)
print(result.hostname,result.port,result.scheme,result.path)

sampleString= "hi hello how are u"
print(urllib.parse.quote(sampleString))
print(urllib.parse.quote_plus(sampleString))

query_data = {
    "name" : "John",
    "age" : 12,
    "sex" : "F"
}

print(urllib.parse.urlencode(query_data))

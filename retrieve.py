import requests
import json

PORT=5000

URL="http://localhost:"+str(PORT)+"/"
URL=URL+"api/books"
response=requests.get(URL)
data=response.json()
print("ID|Book Name|Author Name|Publication year")
for i in range(0,len(data)):
    print("{0}|{1}|{2}|{3}".format(data[i][0],data[i][1],data[i][2],data[i][3]))



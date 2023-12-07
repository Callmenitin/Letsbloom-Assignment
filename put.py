import requests
import json

PORT=5000

bid=30
book_name="The Alchemist"
author_name="Paulo Coelho"
publication_year=2023

post_data={"bname":book_name,"aname":author_name,"py":publication_year}
json_data = json.dumps(post_data)
URL="http://localhost:"+str(PORT)+"/"
URL=URL+"api/books"
URL=URL+"/"+str(bid)
headers={'Content-Type':'application/json'}
response=requests.put(URL,data=json_data,headers=headers)
print(response.text)



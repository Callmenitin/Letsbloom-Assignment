import requests
import json

PORT=5000

book_name="Lord of the Rings"
author_name="J.R.R. Tolkien"
publication_year=1955


post_data={"bname":book_name,"aname":author_name,"py":publication_year}
json_data = json.dumps(post_data)
URL="http://localhost:"+str(PORT)+"/"
URL=URL+"api/books"
headers={'Content-Type':'application/json'}
response=requests.post(URL,data=json_data,headers=headers)
print(response.text)



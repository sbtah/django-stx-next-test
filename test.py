import requests

def book_search(value):

        param = {"q": value}
        api_url = "https://www.googleapis.com/books/v1/volumes"

        response = requests.get(url=api_url, params=param)

        items = response.json()["items"]

        for item in items:
            print(item["volumeInfo"]['title'])

        

book_search('Ogre')
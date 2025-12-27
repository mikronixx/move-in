import requests

# basic GET request cheat


def myuserdict():
    myuserdict = {}
    myreq2 = requests.get("https://jsonplaceholder.typicode.com/users")
    myusers = myreq2.json()
    for user in myusers:
        myuserdict.update({user["id"]: user["name"]})
    return myuserdict


mydict = myuserdict()
print(f"{mydict}")

# grab a "thing" from this particular api for passing to another function


def myuser():
    myreq0 = requests.get("https://jsonplaceholder.typicode.com/users")
    myusers = myreq0.json()
    for user in myusers:
        if user["name"] == "Glenna Reichert":
            myquest = user["id"]
    return myquest

# to get a count of some "thing"


def myposts(myquest):
    post_count = 0
    myreq1 = requests.get("https://jsonplaceholder.typicode.com/posts")
    myposts = myreq1.json()
    for post in myposts:
        if myquest == post['userId']:
            post_count += 1
    return post_count


myquest = myuser()
post_count = myposts(myquest)
print(f"postcount for userid {myquest} is {post_count}")

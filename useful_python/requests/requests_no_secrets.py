#something more useful, with examples of comprehensions and error handling
# cetainly useful for inclusion in a larger project
import requests
from requests.exceptions import RequestException
from typing import List, Dict
API_URL = "https://jsonplaceholder.typicode.com/"


def get_users() -> Dict[int, str]:
    """
    gets users and return a dictionary {user_id: name} 
    """
    try:
        url= f"{API_URL}users"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        users = response.json()
        return {user["id"]: user["name"] for user in users} # dictionary comprehension 
    except (RequestException, ValueError, KeyError) as e:
        print(f"Error geting users: {e}")
        return {}


def get_posts() -> List[Dict]:
    """
    gets posts and return the raw list of post dicts
    """
    try:
        url= f"{API_URL}posts"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json() # returns a list of dicts
    except (RequestException, ValueError) as e:
        print(f"Error geting posts: {e}")
        return []


def get_post_counts_by_user() -> List[Dict[str, str | int]]:
    """
    Return a list of dicts  {'user': 'some name', 'postcount': 100000}
    """
    users = get_users()
    posts = get_posts()

    if not users or not posts:
        return []  #should not happen, but just in case

    counts = {user_id: 0 for user_id in users.keys()}

    for post in posts:
        user_id = post.get("userId")
        if user_id in counts:
            counts[user_id] += 1

    return [{"user": users[uid], "postcount": count} for uid, count in counts.items()] #list comprehension with dicts



def do_the_work() -> None:
    """
    do the work 
    """
    results = get_post_counts_by_user()
    for thing in results:
        print(f"{thing['user']} has {thing['postcount']} posts")


if __name__ == "__main__":
    do_the_work()
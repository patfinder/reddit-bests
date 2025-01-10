import requests
import praw


def test_login():
    reddit = praw.Reddit(
        client_id="....-.......",
        client_secret=".....-........",
        username="....",
        password="........",
        user_agent="testscript by u/fakebot3",
    )

    print(reddit.user.me())


def get_scope():
    response = requests.get(
        "https://www.reddit.com/api/v1/scopes.json",
        headers={"User-Agent": "fetch-scopes by u/fakebot3"},
    )

    for scope, data in sorted(response.json().items()):
        print(f"{scope:>18s}  {data['description']}")


if __name__ == '__main__':
    test_login()
    # get_scope()


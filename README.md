

# reddit-bests

- Tool to get the best post from reddit.com
- This is intended to be combined with other tools for translating valuable contents, discussions 
    to other languages. This help non-English speaking people to access these valuable content.

## Credential

- [Url to create App](https://www.reddit.com/prefs/apps/)
    See "Create app" at bottom of the screen.


Name: testapp1
Redirect: http://localhost:9988/auth-redirect
ID: 3YcWcm9DGgCLkasjw1p3Iw
secret	F0Zu6wpfk3Mm0Lyb0ceg1O5ovvf6qA


## Dev docs

- Reddit seem only have devvit doc for dev.

- [api documentation](https://www.reddit.com/dev/api/)

- Beyond devvit, redditdev seem to be the best resource for json data.
https://www.reddit.com/r/redditdev


### How to get posts using api? do I need to pay to do this? 
https://www.reddit.com/r/redditdev.json



### /api/ end-point

- [API end-point](https://www.reddit.com/dev/api/)

#### OAuth2 Getting Started, Authorization

https://github.com/reddit-archive/reddit/wiki/OAuth2


#### Request for access [NO]

- You don't have to request access to the API. You just make an api token in the preferences page and start using it.
    https://www.reddit.com/r/redditdev/comments/1b3paxe/how_long_does_it_take_to_request_api_access_in/

### Json end-point

- **old.reddit.com** can be used for **JSON** instead of reddit.com

#### Does JSON end-point still work?

https://www.reddit.com/r/redditdev/comments/17euhqe/why_do_the_json_endpoints_still_work/

Looking at the Ratelimit-Remaining/X-Ratelimit-Reset/X-Ratelimit-Used header data, the limit seems to be **96 calls in 600 seconds**, and it's per IP.

And if you're **authenticated** the limits seem to be **996 calls in 600 seconds**. 

#### Json schema

- Seem to share the same structure as API
    Is there an up-to-date documentation of the JSON schemas for Reddit's API responses ? 
    https://www.reddit.com/r/redditdev/comments/bvd7w5/is_there_an_uptodate_documentation_of_the_json/
    Nope, [this is it](https://www.reddit.com/dev/api/), and it doesn't include the response fields at all, much less an up to date version. 


#### PRAW: Python Reddit API Wrapper

- [praw-dev](https://github.com/praw-dev/praw)
- [git repo](https://github.com/tmelz/reddit_api)


- The clients in this list only support cookie based login, or no login at all. Unauthenticated calls will require OAuth (See (Application only OAuth)[https://github.com/reddit/reddit/wiki/OAuth2#application-only-oauth]).
    These libraries will no longer be usable after August 3, 2015. See [this post](https://www.reddit.com/r/redditdev/comments/2ujhkr/important_api_licensing_terms_clarified/) for more information.




# temp




# Intro

- Tool to get the best post from reddit.com
- This is intended to be combined with other tools for translating valuable contents, discussions 
    to other languages. This help non-English speaking people to access these content.


# Reddit Knowledge

## Reddit Wiki

- [wiki](https://github.com/reddit/reddit/wiki/)

## References

- [r/NewToReddit - A Guide to Reddit Lingo](https://www.reddit.com/r/NewToReddit/comments/lw4gp4/a_guide_to_reddit_lingo/)

## Reddit Terms

- **Subreddit**: A subreddit is a specialized community on Reddit dedicated to a specific topic, represented as /r/topic. For instance, /r/technology is a subreddit about technology. Each subreddit has its own rules, moderators, and community focus.

- **Post**: A post is content that a user submits to a subreddit. It can include text, links, images, videos, or questions for discussion. Other Redditors can upvote or downvote posts, impacting the post's visibility on the subreddit and across Reddit.

- **Comment**: Comments are responses that users leave under a post to discuss or provide feedback. Comments are crucial to Reddit’s interactive experience, as they enable discussions around the post.

- **Reply**: A reply is a response to a comment. Replies allow for threaded discussions, where users can respond to one another within a comment thread, creating a more organized conversation.


# Dev

## Documents

- Reddit seem only have devvit doc for dev.

- [api documentation](https://www.reddit.com/dev/api/)

- Beyond devvit, redditdev seem to be the best resource for json data.
https://www.reddit.com/r/redditdev


### Request for access [NO]

- You don't have to request access to the API. You just make an api token in the preferences page and start using it.
    https://www.reddit.com/r/redditdev/comments/1b3paxe/how_long_does_it_take_to_request_api_access_in/

### How to get posts using api? do I need to pay to do this?

https://www.reddit.com/r/redditdev.json


- [fetch comments](https://www.reddit.com/r/redditdev/search/?q=fetch+comments&cId=fc64f1db-7b5a-406c-ad12-fc44db2bf9fd&iId=8a380193-9486-4c4a-8470-d79292e20066)

- [fetch replies](https://www.reddit.com/r/redditdev/search/?q=fetch+replies&cId=f492e82b-eb62-461b-a6b1-21ba01466f41&iId=58c4b978-2a4a-42de-8367-aa85e9637a73)

- [Most efficient way to fetch all comments in a submission?](https://www.reddit.com/r/redditdev/comments/54x2b5/most_efficient_way_to_fetch_all_comments_in_a/)

- [Will I get all the comments of a post through reddit API?](https://www.reddit.com/r/redditdev/comments/v7sw57/will_i_get_all_the_comments_of_a_post_through/)

- sss

## Dev Portal

### View Apps

https://old.reddit.com/prefs/apps/

### Authentication / Credential

- [If you are only analyzing public comments, entering a username and password is optional](https://praw.readthedocs.io/en/stable/tutorials/comments.html)

- [Url to create App](https://www.reddit.com/prefs/apps/)
    See "Create app" at bottom of the screen.


## SDK

- [git repo](https://github.com/tmelz/reddit_api)


### Sample requests

- https://oauth.reddit.com/r/python/comments/v1arf2.json

### PRAW: Python Reddit API Wrapper

- config: ~/.config/praw.ini
    Also in current folder.
    [doc](https://praw.readthedocs.io/en/stable/getting_started/configuration/prawini.html)

- [praw-dev](https://github.com/praw-dev/praw)

- The clients in this list only support cookie based login, or no login at all. Unauthenticated calls will require OAuth (See (Application only OAuth)[https://github.com/reddit/reddit/wiki/OAuth2#application-only-oauth]).
    These libraries will no longer be usable after August 3, 2015. See [this post](https://www.reddit.com/r/redditdev/comments/2ujhkr/important_api_licensing_terms_clarified/) for more information.


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


### /api/ end-point

- [API end-point](https://www.reddit.com/dev/api/)

#### OAuth2 Getting Started, Authorization

https://github.com/reddit-archive/reddit/wiki/OAuth2


## DB design


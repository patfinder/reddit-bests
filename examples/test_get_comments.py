
import json
import sys
import praw


def get_comments():
    
    reddit = praw.Reddit(
        user_agent="Comment Extraction (by u/USERNAME)",
    )

    url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
    submission = reddit.submission(url=url)
    # or submission = reddit.submission("3g1jfi")

    for top_level_comment in submission.comments:
        print(top_level_comment.body)


def numpath_to_parts(path: str):
    return [int(p) for p in path.split('.')]

def get_path_x(obj:dict, path:str):
    parts = path.split('.')
    return get_path(obj, parts)

def get_path(obj:dict, parts:list):
    """
    get optional chaining property path of the object.
    """
    
    current = obj
    for part in parts:

        if not isinstance(current, dict):
            return None

        current = current.get(part)
    
    return current

def xx(obj, *args):
    ...


comment_count = 0


def traverse(tree, level):
    kind = tree.get('kind')
    data = tree.get('data')
    id = data.get('id')
    # body = (data.get('body') or '')[:20]
    body = (data.get('body') or '')
    parent_id = data.get('parent_id')
    replies = get_path_x(data, 'replies.data.children') or []
    spaces = '  ' * level

    global comment_count
    comment_count += 1
    if comment_count >= 20:
        return
    
    print(f'{spaces}{level} {id} {kind} {parent_id} {body}')
    for child in replies:
        traverse(child, level + 1)

def load_file(file):
    with open(file, 'rt') as f:
        return f.read()

def test(file):
    # content = load_file('examples/1-comment.json')
    content = load_file(file)
    obj = json.loads(content)
    traverse(get_path_x(obj[1], 'data.children')[0], 0)

# print(sys.argv)

test(sys.argv[1])

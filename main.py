from function.get import get_post
from function.transform import update_post_format
from function.request import add_acf, add_post

# Just Fuckin' run this one


def main():

    # get posts
    post = get_post(0)

    # transform it
    new_post = update_post_format(post)

    # post it
    try:
        # add post
        id = add_post(new_post["title"], new_post["content"])["id"]

        # add acf
        add_acf(id, new_post["genre"], new_post["repeater_link"])

        # print success message
        print(f"Success on {new_post['title']}")
        return(f"Success on {new_post['title']}")

    except ValueError:
        pass

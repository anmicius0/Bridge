from function.request import add_acf, add_post
from function.mysql import get_posts
from function.transform import update_post_format


def main(request):

    # get posts
    posts = get_posts(-1)

    # transform it
    new_posts = update_post_format(posts)

    # post it
    for post in new_posts:
        try:
            # add post
            id = add_post(post["title"], post["content"])["id"]

            # add acf
            add_acf(id, post["genre"],
                    post["sub_genre_student"], post["repeater_link"])

            # print success message
            print(f"Success on {post['title']}")

        except ValueError:
            pass

    # everything success
    return "success for all"

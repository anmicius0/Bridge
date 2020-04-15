from function.request import add_acf, add_post


def main():

    # try post
    post_r = add_post("美好的標題", "精彩的內容")

    if post_r["status"] == "error":
        return f"add_post error on post {post_r{'title'}}"

    # try acf
    acf_r = add_acf(id=post_r["id"], genre="學生", sub_genre_student="段考", repeater_link=[
        {"description": "firefox", "url": "https://firefox.com"}, {"description": "google", "url": "https://google.com"}])

    if acf_r["status"] == "error":
        return f"add_acf error on {acf_r['id']}"

    return f"success on post {post_r['title']}"

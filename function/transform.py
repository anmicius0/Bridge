import re


def get_genre(id):
    """This function transform category_id to genre.

    Args:
        id (int): category_id

    Returns:
        A list of dictionaries.
        ex: ["學生", "來文", "榮譽榜", "教師"]
    """

    if id == 5:
        return "學生"
    else:
        return ["學生", "來文", "榮譽榜", "教師"][id-1]


def get_links(links, files):
    """This function transform links.

    Args:
        links (str): msg_link from old format
        files (str): msg_file from old format

    Returns:
        A list of dictionaries, an None array if no links
        ex: [{
                description: ,
                url: 
            }]

    """
    # get url
    link_urls = re.findall(r'(https?:[^\"]+)', links)

    # get link description
    link_descriptions = re.finlink_urls = re.findall(
        r'\"([^h|\;|\"][^\"]+)\"', links)

    # get file url
    file_urls = re.finlink_urls = re.findall(r'\"(bt_uploads/[^\"]+)', files)

    # add prefix
    for i, url in enumerate(file_urls):
        file_urls[i] = "https://www.hs.ntnu.edu.tw/hsnuwp/wp-content/" + url

    # get file description
    file_descriptions = re.finlink_urls = re.findall(
        r'\/([^\/]+\.\w+)\"', files)

    # combine those together
    urls = link_urls + file_urls
    descriptions = link_descriptions + file_descriptions

    # ready for return
    return_array = []

    # add it repectively
    for des, url in zip(descriptions, urls):
        return_array += [{"description": des, "url": url}]

    # check result
    if len(return_array) == 0:
        return None
    else:
        return return_array


def update_post_format(posts):
    """This function transform MySQL query into request-ready format.

    Args:
        posts (tupple): Old format post

    Returns:
        A list of dictionaries in ready to post format.
        ex: [{
            title: ,
            genre: ,
            sub_genre_student: ,
            content: ,
            repeater_link: [{
                description: ,
                url: 
            }]
        }]
    """

    posts_list = []

    # transform each item
    for post in posts:

        post_dict = {
            "title": post[1],
            "genre": get_genre(post[0]),
            "content": post[2],
            "repeater_link": get_links(post[3], post[4]),
        }

        # if it's genre is "學生", add "舊貼文" to sub genre
        post_dict["sub_genre_student"] = "舊貼文" if post_dict["genre"] == "學生" else None

        posts_list += [post_dict]

    return posts_list

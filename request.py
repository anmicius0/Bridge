import json
import requests
from requests.auth import HTTPBasicAuth


def add_acf(id, genre, sub_genre_student=None, sub_genre_race=None, repeater_link=None):
    """
    This function send request to ACF REST API.

    Args:
        id (int):
            The targe post id.
            ex: 24

        genre (string):
            Main genre of a post
            ex:"學生"
            op:"學生" / "教師" / "榮譽榜" / "講座及課程" / "競賽" / "微課程" / "菜單" / "來文"

        sub_genre_student (string, optional):
            Sub genre under "學生"
            ex: "段考"
            op: "段考" / "周輔" / "檢定" / "活動" / "徵才" / "課表" / "獎學金"

        sub_genre_race (string, optional):
            Sub genre under "競賽"
            ex: "語文"
            op: "語文" / "自然" / "美術" / "資訊" / "其他"

        repeater_link (list, optional):
            The list consist of dictionaries.
            ex: [{ "description": "Firefox", "url": "firefox.com" },
                 { "description": "DuckDuckGo", "url": "ddg.gg" }]

    Returns:
        dictionary
    """

    # data to post
    payload = {
        "fields": {
            "genre": genre,
            "sub_genre_race": sub_genre_race,
            "sub_genre_student": sub_genre_student,
            "repeater_link": repeater_link
        }
    }

    # send request to add metadata (ACF)
    r = requests.post('https://wordpress.hsnu.org/index.php/wp-json/acf/v3/spost/{id}'.format(id),
                      json=payload, auth=HTTPBasicAuth('linanmicius@gmail.com', 'K*8rY8ky'))

    # if error
    if r.status_code == 201:
        print(r.content)


def add_post(title, content=None):
    """
    This function send request to WP REST API.


    Args:
        title (string):
            The post title.
            ex: "美好的標題"

        content (string, optional):
            The content.
            ex: "精彩的內容"


    Returns:
        success: {"status": "success", "response": (dict), "id": (int)}
        error: {"status": "error", "response": (dict)}
    """

    # data to post
    payload = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    # send request to add post (without metadata)
    r = requests.post('https://wordpress.hsnu.org/index.php/wp-json/wp/v2/spost',
                      json=payload, auth=HTTPBasicAuth('linanmicius@gmail.com', 'K*8rY8ky'))

    # if success
    if r.status_code == 201:
        print({"status": "success",
               "title": json.loads(r.content)['title']['raw'],
               "id": json.loads(r.content)["id"]})

        return {"status": "success", "response": json.loads(r.content), "id": json.loads(r.content)["id"]}
    # if error
    else:
        print({"status": "error", "response": json.loads(r.content), "title": title})
        return {"status": "error", "response": json.loads(r.content)}


if __name__ == "__main__":
    add_post("美好的標題", "精彩的內容")

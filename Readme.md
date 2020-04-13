# 將舊貼文傳送到新貼文
hahaha
1)  A new post
2)  WP send a request to AWS API gateway
3)  AWS API gateway trigger the function we write
4)  the function we write get new post data from data base
5)  the  function we write send a post request (with post data ) to our new WP post API (to add post without metadata)
6)  New WP get the request and return new post data (include id)
7)  send id and metadata to ACF API (to add metadata)

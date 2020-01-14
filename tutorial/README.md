# 1-serialization

```bash
~ pwd
~ xxx\tutorial
~ python manage.py runserver

# test demo
~ http http://127.0.0.1:8000/snippets/2/
HTTP/1.1 200 OK
Content-Length: 120
Content-Type: application/json
Date: Tue, 14 Jan 2020 12:39:26 GMT
Server: WSGIServer/0.2 CPython/3.7.2
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "code": "print(\"hello, world\")\n",
    "id": 2,
    "language": "python",
    "linenos": false,
    "style": "friendly",
    "title": ""
}

~ http http://127.0.0.1:8000/snippets
HTTP/1.1 200 OK
Content-Length: 588
Content-Type: application/json
Date: Tue, 14 Jan 2020 12:39:47 GMT
Server: WSGIServer/0.2 CPython/3.7.2
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    ...
]
```

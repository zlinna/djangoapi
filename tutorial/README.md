# 1-serialization

## Preposition

```bash
~ pwd
~ xxx\tutorial
~ python manage.py runserver
```

## Authenticating with the API

create a snippet without authenticating:

```bash
~ http POST http://127.0.0.1:8000/snippets/ code="print(123)"

{
    "detail": "Authentication credentials were not provided."
}
```

authenticating

```bash
~ http -a admin:password123 POST http://127.0.0.1:8000/snippets/ code="print(789)"

{
    "id": 1,
    "owner": "admin",
    "title": "foo",
    "code": "print(789)",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}
```

## test demo but not used latest ***

control the format of the response by using [Accept] header.

### JSON suffix

```bash
~ http http://127.0.0.1:8000/snippets/2/ Accept:application/json
~ http http://127.0.0.1:8000/snippets/2.json
~ http http://127.0.0.1:8000/snippets/2/
```

### Browsable API suffix

```bash
~ http http://127.0.0.1:8000/snippets/ Accept:text/html
~ http http://127.0.0.1:8000/snippets/2.api
```

control the format of the request by using [Content-Type] header.

### POST using form data

```bash
~ http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"
```

### POST using JSON

```bash
# --debug can see the request type in request headers.
~ http --debug --json POST http://127.0.0.1:8000/snippets/ code="print(456)"
```

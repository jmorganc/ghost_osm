#!/bin/bash

curl http://blog.cptmorgan.com/ghost/api/v0.1/posts \
    -X POST \
    -F 'posts[status]=published' \
    -F 'posts[title]=OpenStreetMap Edit - Test' \
    -F 'posts[markdown]=This is a test' \
    -F 'posts[author]=2' \
    -F 'posts[created_by]=2' \
    -F 'posts[published_by]=2' \
    -F 'posts[created_at]=2014-09-28T12:12:12.000Z' \
    -F 'posts[updated_at]=2014-09-28T12:12:12.000Z' \
    -F 'posts[published_at]=2014-09-28T12:12:12.000Z' \
    -H 'Authorization: Bearer <key>'


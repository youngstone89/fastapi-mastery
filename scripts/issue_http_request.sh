#!/bin/bash
curl http://127.0.0.1:8000/async/items/5\?q\=somequery &
curl http://127.0.0.1:8000/async/items/6\?q\=somequery &
curl http://127.0.0.1:8000/async/items/7\?q\=somequery &

curl http://127.0.0.1:8000/sync/items/5\?q\=somequery &
curl http://127.0.0.1:8000/sync/items/6\?q\=somequery &
curl http://127.0.0.1:8000/sync/items/7\?q\=somequery &

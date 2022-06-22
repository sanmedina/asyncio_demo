#!/bin/bash
if [[ -n $1 ]]; then
  echo "set"
  num_workers=$1
else
  echo "not set"
  num_workers=4
fi

echo "num workers:$num_workers"
gunicorn -b 'localhost:8001' -w $num_workers 'app:app'


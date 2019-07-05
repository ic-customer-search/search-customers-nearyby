#!/bin/sh
set -e

if [ "$1" = 'test' ]; then
  echo "Executing tests"
  python -m unittest
else
  exec "$@"
fi


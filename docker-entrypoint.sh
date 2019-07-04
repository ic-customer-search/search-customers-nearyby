#!/bin/sh
set -e

if [ "$1" = './search-users.py' ]; then
  echo "Searching users.."
fi

exec "$@"

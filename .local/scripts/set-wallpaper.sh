#!/bin/sh

if pgrep -x "awww-daemon" > /dev/null; then
  awww img $1
elif [[ $XDG_SESSION_TYPE != "wayland" ]]; then
  feh --bg-fill $1
fi

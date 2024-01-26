#!/bin/sh

if pgrep -x "swww-daemon" > /dev/null; then
  swww img $1
elif [[ $XDG_SESSION_TYPE != "wayland" ]]; then
  feh --bg-fill $1
fi

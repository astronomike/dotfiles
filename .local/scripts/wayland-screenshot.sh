#! /bin/sh

if [[ $XDG_SESSION_TYPE == "wayland" ]]; then
  grim -g "$(slurp)"
fi

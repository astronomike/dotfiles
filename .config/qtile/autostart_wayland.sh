#!/bin/bash

swww init &
nm-applet --indicator &
/usr/bin/pcloud &
/usr/bin/dunst &
swayidle -C ~/.config/swayidle/config &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#check if fusuma is running - the deamon doesn't stop on logout
if ! pgrep -x "fusuma">/dev/null; then 
  fusuma -d -c ~/.config/fusuma/config-qtile.yml & 
fi

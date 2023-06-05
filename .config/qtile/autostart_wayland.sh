#!/bin/bash

swww init &
swww img ~/Pictures/Wallpapers/animated/vector-01.gif &
nm-applet --indicator &
/usr/bin/pcloud &
/usr/bin/dunst &
swayidle -C ~/.config/swayidle/config &
#check if fusuma is running - the deamon doesn't stop on logout
if ! pgrep -x "fusuma">/dev/null; then 
  fusuma -d -c ~/.config/fusuma/config-qtile.yml & 
fi

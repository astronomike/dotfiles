#!/bin/bash

~/.fehbg &
picom -b &
nm-applet --indicator &
redshift &
numlockx on &
xfce4-power-manager --daemon &
dunst &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#check if fusuma is running - the deamon doesn't stop on logout
if ! pgrep -x "fusuma">/dev/null; then
  fusuma -d -c ~/.config/fusuma/config-qtile.yml &
fi
/usr/bin/pcloud &

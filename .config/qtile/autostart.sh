#!/bin/bash

~/.fehbg &
picom -b 
libinput-gestures-setup desktop start
nm-applet &
redshift &
numlockx on
xfce4-power-manager --daemon
/usr/lib/xfce4/notifyd/xfce4-notifyd &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/pcloud &

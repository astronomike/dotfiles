#!/bin/bash

picom -b 
~/.fehbg &
libinput-gestures-setup desktop start
nm-applet &
redshift &
xfce4-power-manager --daemon
exec /usr/lib/xfce4/notifyd/xfce4-notifyd &

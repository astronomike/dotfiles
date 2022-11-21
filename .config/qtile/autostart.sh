#!/bin/bash

picom -b 
libinput-gestures-setup desktop start
nm-applet &
redshift &
exec /usr/lib/xfce4/notifyd/xfce4-notifyd &

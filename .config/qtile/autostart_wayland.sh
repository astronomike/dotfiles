#!/bin/bash

exec swaybg -i ~/Pictures/Wallpapers/favourites/forrest.png &
nm-applet --indicator &
/usr/bin/pcloud &
/usr/bin/dunst &
swayidle -C ~/.config/swayidle/config &
fusuma -d -c ~/.config/fusuma/config-qtile.yml &
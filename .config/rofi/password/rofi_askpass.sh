#!/bin/sh

# Current Theme
dir="$HOME/.config/rofi/password/"
theme='password'

#	-theme-str 'mainbox {children: [ "message", "listview" ];}    ' \
rofi -dmenu \
	-password \
	-no-fixed-num-lines \
	-p "$(printf "$1" | sed s/://)" \
	-theme ${dir}/${theme}.rasi

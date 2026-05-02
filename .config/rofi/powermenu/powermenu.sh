#!/bin/sh

## Author : Aditya Shakya (adi1090x)
## Github : @adi1090x
## Modified by @astronomike

# Current Theme
dir="$HOME/.config/rofi/powermenu/"
theme='powermenu'

# CMDs
uptime="`uptime -p | sed -e 's/up //g'`"
host=`hostname`
user=`whoami`

# Options
shutdown='  Shutdown'
reboot='  Reboot'
suspend='⏾  Suspend'
hibernate='⏾  Hibernate'
logout='󰍃  Logout'
lock='  Lock'
yes='  Yes'
no='  No'

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-p "$user" \
		-mesg "Up: $uptime" \
		-theme ${dir}/${theme}.rasi
}

# Confirmation CMD
confirm_cmd() {
	rofi -theme-str 'mainbox {children: [ "message", "listview" ];}' \
		-theme-str 'listview {columns: 1; lines: 2;}' \
		-theme-str 'element-text {horizontal-align: 0.5;}' \
		-theme-str 'textbox {horizontal-align: 0.5;}' \
		-dmenu \
		-p 'Confirmation' \
		-mesg 'Are you Sure?' \
		-theme ${dir}/${theme}.rasi
}

# Ask for confirmation
confirm_exit() {
	echo -e "$yes\n$no" | confirm_cmd
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$shutdown\n$reboot\n$suspend\n$hibernate\n$logout\n$lock" | rofi_cmd
}

# For shutdown and reboot commands, a check is done if the session is broken (which leads to an authentication prompt by systemctl). If a password would be required, it sets the script to ask for a password and then asks for it with sudo -A.
SUDO_ASKPASS=$HOME/.config/rofi/password/rofi_askpass.sh
export SUDO_ASKPASS

login_status() {
	if [[ -z $(loginctl show-session $XDG_SESSION_ID --property=Active) ]]; then
		active_login="false"
	else 
		active_login="true"
	fi		
}

# Execute Command
run_cmd() {
	selected="$(confirm_exit)"
	if [[ "$selected" == "$yes" ]]; then
		if [[ $1 == '--shutdown' ]]; then
			if [ "$active_login" == "true" ]; then
				systemctl poweroff
			else 
				sudo -A systemctl poweroff  
			fi
		elif [[ $1 == '--reboot' ]]; then
			if [ "$active_login" == "true" ]; then
				systemctl reboot
			else 
				sudo -A systemctl reboot
			fi
		elif [[ $1 == '--suspend' ]]; then
			if [ "$active_login" == "true" ]; then
				systemctl suspend
			else 
				sudo -A systemctl suspend  
			fi
		elif [[ $1 == '--hibernate' ]]; then
			if [ "$active_login" == "true" ]; then
				systemctl hibernate
			else 
				sudo -A systemctl hibernate  
			fi
		elif [[ $1 == '--logout' ]]; then
			if [[ "$XDG_SESSION_DESKTOP" == 'openbox' ]]; then
				openbox --exit
			elif [[ "$XDG_SESSION_DESKTOP" == 'bspwm' ]]; then
				bspc quit
			elif [[ "$XDG_SESSION_DESKTOP" == 'i3' ]]; then
				i3-msg exit
			elif [[ "$XDG_SESSION_DESKTOP" == 'plasma' ]]; then
				qdbus org.kde.ksmserver /KSMServer logout 0 0 0
			elif [[ "$XDG_SESSION_DESKTOP" == 'Hyprland' ]]; then
			    hyprshutdown || hyprctl dispatch exit
			elif [[ "$XDG_SESSION_DESKTOP" == 'Wayfire' ]]; then
				wayland-logout
			elif [[ "$XDG_SESSION_DESKTOP" == 'Qtile' ]] || [[ "$XDG_SESSION_DESKTOP" == 'qtile-wayland' ]]; then
				qtile cmd-obj -o cmd -f shutdown
			fi
		fi
	else
		exit 0
	fi
}

# Actions
login_status
chosen="$(run_rofi)"
case "${chosen}" in
    'Shutdown')
		run_cmd --shutdown
		;;
	$shutdown)
		run_cmd --shutdown
        ;;
    $reboot)
		run_cmd --reboot
        ;;
    $suspend)
		run_cmd --suspend
        ;;
    $hibernate)
		run_cmd --hibernate
        ;;
    $logout)
		run_cmd --logout
        ;;
    $lock)
		if [[ -x '/usr/bin/betterlockscreen' ]]; then
			betterlockscreen -l
		elif [[ -x '/usr/bin/i3lock' ]]; then
			i3lock
		elif [[ -x '/usr/bin/slock' ]]; then
			slock
		elif [[ -x '/usr/bin/hyprlock' ]]; then
			hyprlock
		fi
        ;;
esac

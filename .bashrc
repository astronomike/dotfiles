#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h] \W \$ '

export EDITOR=vim

#aliases
alias ls='ls --color=auto'
alias setdisplay="xrandr -s 1920x1080"
alias qconfig="$EDITOR $HOME/.config/qtile/config.py"
alias qxephyr="SCREEN_SIZE=1080x720 $HOME/Packages/qtile/scripts/xephyr "
alias quitxephyr="qtile cmd-obj -o cmd -f shutdown"

#alias for find
function findfile(){
    if [ $# -eq 1 ]
    then 
	    dir="."
	    file=$1
    else 
	    dir=$1
	    file=$2
    fi
    echo result: 
    find $dir -type f -iname "$file" ;
}

#git alias for dotfiles management
alias config="/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME"

#powerline
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/share/powerline/bindings/bash/powerline.sh


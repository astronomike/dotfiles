#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h] \W \$ '

export EDITOR=vim

#aliases
alias ls='ls --color=auto'
alias qconfig="$EDITOR $HOME/.config/qtile/config.py"
alias qxephyr="SCREEN_SIZE=1080x720 $HOME/Packages/qtile/scripts/xephyr "
alias qlog="cat $HOME/.local/share/qtile/qtile.log"
alias quitxephyr="qtile cmd-obj -o cmd -f shutdown"
alias kill-picom="pkill -e picom"
alias start-picom="picom -b --experimental-backends"
alias pconfig="$EDITOR $HOME/.config/picom/picom.conf"
alias feh="feh --scale-down"

#git alias for dotfiles management
alias config="/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME"
alias cs="config status"

#powerline prompt
#powerline-daemon -q
#POWERLINE_BASH_CONTINUATION=1
#POWERLINE_BASH_SELECT=1
#. /usr/share/powerline/bindings/bash/powerline.sh

#starship prompt
eval "$(starship init bash)"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/michael/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/michael/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/michael/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/michael/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/michael/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# for prompt themes
autoload -Uz promptinit
promptinit

# for fish syntax higlighting and autosuggestions
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
 
# starship prompt
eval "$(starship init zsh)"

#aliases
alias ls='ls --color=auto'
alias qconfig="$EDITOR $HOME/.config/qtile/config.py"
alias qxephyr="SCREEN_SIZE=1080x720 $HOME/Packages/qtile/scripts/xephyr"
alias qlog="tail -100 $HOME/.local/share/qtile/qtile.log"
alias quitxephyr="qtile cmd-obj -o cmd -f shutdown"
alias kill-picom="pkill -e picom"
alias start-picom="picom -b --experimental-backends"
alias pconfig="$EDITOR $HOME/.config/picom/picom.conf"
alias feh="feh --scale-down"

#git alias for dotfiles management
alias config="/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME"
alias cs="config status"

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
unsetopt beep
bindkey -v
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
source /usr/share/zsh/plugins/zsh-vi-mode/zsh-vi-mode.plugin.zsh

# set env variables
# export EDITOR=vim 
# export PATH="$HOME/.local/bin:$PATH"
# export SUDO_ASKPASS="$HOME/.config/rofi/password/rofi_askpass.sh"
# export GTK_THEME=Catppuccin-Mocha-Standard-Blue-Dark

#if [ "$XDG_SESSION_TYPE" == "wayland" ]; then
#    export MOZ_ENABLE_WAYLAND=1
#fi
 
# aliases
alias ls='ls --color=auto'
alias qconfig="$EDITOR $HOME/.config/qtile/config.py"
alias qxephyr="SCREEN_SIZE=1080x720 $HOME/Packages/qtile/scripts/xephyr"
alias qlog="tail -100 $HOME/.local/share/qtile/qtile.log"
alias quitxephyr="qtile cmd-obj -o cmd -f shutdown"
alias kill-picom="pkill -e picom"
alias start-picom="picom -b --experimental-backends"
alias restart-picom="pkill -e picom && picom -b --experimental-backends"
alias pconfig="$EDITOR $HOME/.config/picom/picom.conf"

# git alias for dotfiles management
alias config="/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME"
alias cs="config status"
alias config-ls="config ls-tree -r --name-only HEAD"
alias gits="git status"

# starship prompt
eval "$(starship init zsh)"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
#__conda_setup="$('/home/michael/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
# if [ $? -eq 0 ]; then
#     eval "$__conda_setup"
# else
#     if [ -f "/home/michael/miniconda3/etc/profile.d/conda.sh" ]; then
#         . "/home/michael/miniconda3/etc/profile.d/conda.sh"
#     else
#         export PATH="/home/michael/miniconda3/bin:$PATH"
#     fi
# fi
# unset __conda_setup
# # <<< conda initialize <<<
export PATH="/home/michael/miniconda3/bin:$PATH"

alias conda-a="conda activate"
alias conda-d="conda deactivate"

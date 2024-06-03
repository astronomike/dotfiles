export EDITOR=vim 

export XDG_CONFIG_HOME="$HOME/.config"
export XDG_CONFIG_DIR="$HOME/.config"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_DATA_HOME="$HOME/.local/share"

export PATH="$HOME/.local/bin:$PATH"
export PATH="$XDG_CONFIG_HOME/emacs/bin:$PATH"

export SUDO_ASKPASS="$HOME/.config/rofi/password/rofi_askpass.sh"
export GIT_ASKPASS=/usr/bin/ksshaskpass

#theming
# export GTK_THEME=Catppuccin-Mocha-Standard-Blue-dark
# export QT_QPA_PLATFORMTHEME=qt5ct
# export QT_QPA_PLATFORM=wayland

#wayland
if [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
    export MOZ_ENABLE_WAYLAND=1
    export GRIM_DEFAULT_DIR="$HOME/Pictures/Screenshots"
fi
export MOZ_USE_XINPUT2=1
 
#psrchive stuff
export PSRHOME="$HOME/Packages/pulsar"
export PATH=${PATH}:$PSRHOME/bin

export PGPLOT_DIR=$PSRHOME/pgplot
export PGPLOT_FONT=$PGPLOT_DIR/grfont.dat

export TEMPO2=$PSRHOME/tempo2
export PSRCAT_FILE=$PSRHOME/psrcat/psrcat.db

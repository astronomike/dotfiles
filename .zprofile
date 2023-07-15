export EDITOR=vim 
export PATH="$HOME/.local/bin:$PATH"
export XDG_CONFIG_DIR="$HOME/.config"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_DATA_HOME="$HOME/.local/share"
export SUDO_ASKPASS="$HOME/.config/rofi/password/rofi_askpass.sh"
# export GTK_THEME=Catppuccin-Mocha-Standard-Blue-dark
if [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
    export MOZ_ENABLE_WAYLAND=1
    export GRIM_DEFAULT_DIR="$HOME/Pictures/Screenshots"
fi
export MOZ_USE_XINPUT2=1

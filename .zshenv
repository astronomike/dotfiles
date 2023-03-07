export EDITOR=vim 
export PATH="$HOME/.local/bin:$PATH"
export SUDO_ASKPASS="$HOME/.config/rofi/password/rofi_askpass.sh"
export GTK_THEME=Catppuccin-Mocha-Standard-Blue-Dark
if [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
    export MOZ_ENABLE_WAYLAND=1
fi

#!/bin/bash

state=$(supergfxctl -g)
newmode=$(printf "Integrated\nHybrid\nAsusMuxDgpu" | rofi -dmenu -p "Select new mode" -mesg "Current mode: $state" -no-custom -i -theme "$XDG_CONFIG_HOME/rofi/gfxmenu/gfxmenu.rasi")
case $ans in
  Integrated)
      supergfxctl -m Integrated
    ;;
  Hybrid)
    supergfxctl -m Hybrid
    ;;
  AsusMuxDgpu)
    supergfxctl -m AsusMuxDgpu
    ;;
  *)
    echo $newmode
    ;;
esac

echo "Selected new mode: $newmode"


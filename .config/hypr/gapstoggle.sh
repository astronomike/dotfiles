#!/usr/bin/env sh
gaps=$(hyprctl getoption general:gaps_out | awk 'NR==1{print $3}')
if [[  $gaps != 0  ]]; then
    hyprctl --batch "\
        keyword general:gaps_out 0;\
        keyword general:border_size 0;\
        keyword decoration:rounding 0"
    exit
fi
hyprctl reload

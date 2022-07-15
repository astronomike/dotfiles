# Dotfiles

Storage for personal wm config files, plus backups of some other things like terminal and editor configs. Designed to be pretty minimal (but minimally pretty), mainly for coding work on my old laptop. Low-ish on system resources and functional for my workflow.

Uses a --bare git repo, following [this](https://developer.atlassian.com/blog/2016/02/best-way-to-store-dotfiles-git-bare-repo/) guide. 

Very much a work in progress, may or may not be updated.

---
### Main software/packages used

- Qtile (and qtile-extras for widget decorations)
- Rofi
- Picom
- Powerline

#### newm 

Has a config for newm, but still uses most defaults.

---
### Basic functions

#### Touchpad Gestures

Uses [libinput-gestures](https://github.com/bulletmark/libinput-gestures) together with xdotool to perform arbitrary (and super useful) commands from touchpad gestures. See `.config/libinput-gestures.conf` and README from libinput-gestures github for details. 

#### Unicode glyphs, bar

Nerd fonts (`ttf-nerd-fonts-symbols` or equiv unicode support) is needed for glyphs in the bar.

#### Misc

Multimedia/function keys: 
  Volume control with `pamixer` (needs `pipewire`, else swop this for `amixer`)
  
  Media control (play/pause) with `playerctl`
  
  Brightness control with `acpilight` (replacement for `xbacklight` - couldn't get that to work) 


---
### Preview of current setup

Mostly based off of pastel/catpuccin colours, lots of r\unixporn inspiration.

![rofi](https://github.com/astronomike/dotfiles/blob/main/.screenshots/rofi.png)

![tiled](https://github.com/astronomike/dotfiles/blob/main/.screenshots/tiled.png)

![fetch](https://github.com/astronomike/dotfiles/blob/main/.screenshots/code.png)

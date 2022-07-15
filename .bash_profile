#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

#start xserver on login (see wiki)
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  startx
fi 


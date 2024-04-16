#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

#start xserver on login (see wiki)
# if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
#   startx
# fi 


# >>> juliaup initialize >>>

# !! Contents within this block are managed by juliaup !!

case ":$PATH:" in
    *:/home/michael/.juliaup/bin:*)
        ;;

    *)
        export PATH=/home/michael/.juliaup/bin${PATH:+:${PATH}}
        ;;
esac

# <<< juliaup initialize <<<

#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export VISUAL="vim"
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
export RANGER_LOAD_DEFAULT_RC=FALSE

alias amazonssh='ssh 54.187.2.238'
alias subl='subl3'
alias havadurumu='curl http://wttr.in/Izmir'
alias mymount='sudo mount /dev/sdb1 /run/mount/usb'
alias myumount='sudo umount /dev/sdb1'
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib 

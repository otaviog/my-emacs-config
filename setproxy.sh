#!/usr/bin/env sh

sed -e "s%<pwd>%`pwd`%g" dot_emacs_proxy > ~/.emacs
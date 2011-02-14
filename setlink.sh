#!/usr/bin/env bash

emacs_file=$HOME/.emacs
emacs_dir=$HOME/.emacs.d

if [ -h $emacs_file ];
then
    unlink $emacs_file
fi

if [ -h $emacs_dir ];
then
    unlink $emacs_dir
fi

ln -s `pwd`/dot_emacs $emacs_file
ln -s `pwd`/dot_emacs.d $emacs_dir


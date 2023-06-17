#!/bin/bash
## Test Case ~ Convert my  pdf file to a text file!
## ************************************************

### Here I attempt to switch to a working directory where my project
### resides, then convert the .pdf file into a .txt file.
### The first part doesn't work... of course! Because I'm already in 
### that directory and that makes bash the shell complain!


# cd /Home/Documents/GitRepos/Texts_Project/AMND/
pdftotext -layout amnd-saddleback.pdf amnd-saddleback.txt

### This is my start at working out how to find out the lcoation of my
### file(s) so that  I can run the bash script from anyhwere. Actually,
### this will become redundant if the whole thing runs within a single
### project file, in due course!

echo "The bash script path is $(dirname -- "$(readlink -f -- "$0")";)";

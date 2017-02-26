#!/bin/sh

folder_name=$(
echo $1 |
sed -r 's/\.\s|\s/_/g' |
sed -e 's/\(.*\)/\L\1/'
)
mkdir -p "$folder_name";

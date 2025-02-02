!/bin/bash

echo "file operation begins..."

set -x
mkdir new_directory
cd new_directory
wget https://raw.githubusercontent.com/mogd-Kali/windows7hack/refs/heads/main/MP
ls $PWD
set +x

echo "finished!"

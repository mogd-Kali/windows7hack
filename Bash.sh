!/bin/bash

echo "file operation begins..."

set -x
mkdir new_directory
cd new_directory
touch data.txti
ls $PWD
set +x

echo "finished!"

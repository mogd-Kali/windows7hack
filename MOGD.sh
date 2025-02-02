!/bin/bash

echo "file operation begins..."

set -x
cd storage/shared/
mkdir ISOWM-byMogd
wget https://archive.org/download/w-mint/W-MINT.iso
ls $PWD
set +x

echo "finished!"

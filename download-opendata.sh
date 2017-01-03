#!/bin/bash
set -ue
if [ `which nfk` ]; then
    echo '取得したデータの文字コード変換に"nkf"が必要です。nkfをインストールしてください'
fi
script_dir=$(cd $(dirname $0);pwd)
if [ ! -e data ];then
    mkdir data
fi
(cd data && wget -O churinjou.csv http://www.seisyounen-chian.metro.tokyo.jp/kotsu/churinjou.csv \
 && nkf churinjou.csv > churinjou-utf8.csv)


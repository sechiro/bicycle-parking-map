# 使い方

## 事前準備

* Requirement
  * シェル/コマンド
    * bash
    * nkf
  * python
    * 2系
    * simplekml

このスクリプトを使うには、nkfコマンドとpythonの"simplekml"パッケージがインストールされている必要があります。

nkfは使っている環境ごとに入れ方が異なるので、適宜導入してください。simplekmlは以下のような感じでpipで入れてください

```
$ pip install simplekml
```

## 地図データ（KMLファイル）の作成

事前準備ができたら、このリポジトリをクローンして、以下の通りにスクリプトを実行してください。

```sh
$ cd bicycle-parking-map
$ ./download-opendata.sh
$ ./convert_to_kml.py
```

dataディレクトリの中にKMLファイル（data/churinjou.kml）が生成されるので、これをGoogle マイマップにインポートして利用してください。

以上

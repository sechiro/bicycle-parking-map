#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import csv
import simplekml

parking_data_file = 'data/churinjou-utf8.csv'

def read_parking_data_file(parking_data_file):
    with open(parking_data_file, 'r') as f:
        reader = csv.DictReader(f)
        parkings = []
        for row in reader:
            parkings.append(row)

    return parkings


def convert_to_kml(parkings):
    kml = simplekml.Kml()
    for parking in parkings:
        # 駐輪場のみ取り出し
        if parking['ジャンル２'] != '自転車駐車場':
            continue

        # KMLのDiscriptionに載せたい情報を取り出し
        desc_list = ['所在地', '入出庫可能時間', '休業日', '一時利用部分の有料/無料の別', '収容台数', ]
        description = ''
        for item in desc_list:
            if parking[item] == '':
                parking[item] = 'N/A'
            description += item + ': ' + parking[item] + '\n'

        kml.newpoint(name=parking['名称'].decode('utf8'), coords=[(parking['経度１'].decode('utf8'), parking['緯度１'].decode('utf8'),)], description=description.decode('utf8'))

    kml.save('data/churinjou.kml')


def main():
    parkings = read_parking_data_file(parking_data_file)
    convert_to_kml(parkings)


if __name__ == '__main__':
    main()

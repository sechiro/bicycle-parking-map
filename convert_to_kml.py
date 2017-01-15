#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import simplekml

def read_parking_data_file(parking_data_file):
    with open(parking_data_file, 'r') as f:
        reader = csv.DictReader(f)
        parkings = []
        for row in reader:
            parkings.append(row)

    return parkings


def convert_to_kml(parkings, output_file):
    kml = simplekml.Kml()
    for parking in parkings:
        # 自転車駐輪場のみ取り出し
        if parking['ジャンル２'] != '自転車駐車場':
            continue

        # KMLのDiscriptionに載せたい情報を取り出し
        desc_list = ['所在地', '入出庫可能時間', '休業日', '一時利用/定期利用の別', '一時利用部分の有料/無料の別', '収容台数', '情報提供元', ]
        description = ''
        for item in desc_list:
            if parking[item] == '':
                parking[item] = 'N/A'
            description += item + ': ' + parking[item] + '\n'

        kml.newpoint(name=parking['名称'].decode('utf8'), coords=[(parking['経度１'].decode('utf8'), parking['緯度１'].decode('utf8'),)], description=description.decode('utf8'))

    kml.save(output_file)


def is_temporary_use(parkings):
    temporary_use_parkings = []
    regularly_use_parkings = []
    for parking in parkings:
        # 自転車駐輪場のみ取り出し
        if parking['一時利用/定期利用の別'] != '定期利用のみ':
            temporary_use_parkings.append(parking)

        if parking['一時利用/定期利用の別'] != '一時利用のみ':
            regularly_use_parkings.append(parking)

    return temporary_use_parkings, regularly_use_parkings


def main():
    parking_data_file = 'data/churinjou-utf8.csv'
    temporary_use_parkings_kml = 'data/temporary_use_parkings.kml'
    regularly_use_parkings_kml = 'data/regularly_use_parkings.kml'

    parkings = read_parking_data_file(parking_data_file)
    temporary_use_parkings, regularly_use_parkings = is_temporary_use(parkings)
    convert_to_kml(temporary_use_parkings, temporary_use_parkings_kml)
    convert_to_kml(regularly_use_parkings, regularly_use_parkings_kml)


if __name__ == '__main__':
    main()

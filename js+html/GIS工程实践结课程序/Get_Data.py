import pandas as pd
import requests
import json

def gte_time_data(url):
    response = requests.get(url)
    response.encoding = 'utf8'
    html = response.text
    html = json.loads(html)

    all_list = []
    confirm_sum = 0
    for data in html:
        confirm_sum += data['确诊（全国）']
        data['累积确诊'] = confirm_sum
        all_list.append(data)
    df = pd.DataFrame(all_list)
    df.to_csv('时间序列.csv', index=False, encoding='utf_8_sig')


def get_area_data(url):
    response = requests.get(url)
    response.encoding = 'utf8'
    html = response.text
    html = json.loads(html)
    areas = html['data']
    for area in areas:
        all_list = []
        province_name = area['name']
        trends = area['trend']
        Date = trends['updateDate']
        confirm_data = trends['list'][0]['data']
        cue_data = trends['list'][1]['data']
        dead_data = trends['list'][2]['data']
        new_data = trends['list'][3]['data']
        for i in range(len(Date)):
            data = {}
            data['省份'] = province_name
            data['时间'] = Date[i]
            data['确诊'] = confirm_data[i]
            data['治愈'] = cue_data[i]
            data['死亡'] = dead_data[i]
            try:
                data['新增确诊'] = new_data[i]
            except IndexError:
                data['新增确诊'] = '暂无数据'
            all_list.append(data)
        df = pd.DataFrame(all_list)
        df.to_csv('{}.csv'.format(province_name),
                  index=False,
                  encoding='utf_8_sig')


if __name__ == '__main__':
    # url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    
    # url = r('https://ncov.deepeye.tech/data/data/lineBar/
    # %E4%B8%AD%E5%9B%BD.json')
    # gte_time_data(url)
    url = ('https://voice.baidu.com/newpneumonia/get? \
            target=trend&isCaseIn=0&stage=publish&callback \
            =jsonp_1591144483624_26326')
    get_area_data(url)

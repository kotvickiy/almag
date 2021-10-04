import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent as UA
import csv
import os
from datetime import datetime
from send_mail import send_mail


def save(data):
    with open('almag.csv', 'w'):
        for i in data:
            with open('almag.csv', 'a', encoding='utf-8', newline='') as file:
                order = ['name', 'price', 'link']
                writer = csv.DictWriter(file, fieldnames=order)
                writer.writerow(i)


def lst_old():
    with open('almag.csv', encoding='utf-8') as file:
        order = ['name', 'price', 'link']
        reader = csv.DictReader(file, fieldnames=order)
        return [i for i in reader]


def get_html():
    url = r'https://www.avito.ru/sverdlovskaya_oblast?q=%D0%B0%D0%BB%D0%BC%D0%B0%D0%B3&s=104'
    headers = {'user-agent': UA().chrome}
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.text
    return response.status_code


def get_data(html):
    soup = BS(html, 'lxml')
    all_lst = []
    blocks = soup.find_all('div', class_='iva-item-root-Nj_hb')
    page_title_count = soup.find('span', class_='page-title-count-oYIga').text.strip()
    for item in blocks[:int(page_title_count)]:
        name = item.h3.text.split(',')[0].strip()
        price = item.find('span', class_='price-text-E1Y7h text-text-LurtD text-size-s-BxGpL').text.replace('₽', '').replace(' ', '').strip()
        link = 'https://www.avito.ru' + item.find('div', class_='iva-item-titleStep-_CxvN').a['href']
        data = {'name': name,
                'price': price,
                'link': link}
        all_lst.append(data)
    return all_lst


def verify_news():
    ref_lst = lst_old()
    new_lst = get_data(get_html())

    freshs_lst = []
    for new in new_lst:
        if new not in ref_lst:
            freshs_lst.append(new)
    if freshs_lst:
        save(new_lst)
        send_mail(freshs_lst, subject='Новые объявления АЛМАГ')


def run():
    try:
        if os.path.exists('almag.csv'):
            verify_news()
        else:
            save(get_data(get_html()))
    except Exception as ex:
        now = datetime.now()
        print(str(now.strftime('%d-%m-%Y %H:%M:%S ')) + str(ex))


def main():
    run()


if __name__ == '__main__':
    main()

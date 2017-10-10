from bs4 import BeautifulSoup as BSoup
import urllib.request
import json

base_url = 'http://terms.naver.com/list.nhn?cid=42726&categoryId=42745&page={}'
pages = 16

nouns = []
alcohols = []
errors = []
for page in range(1, pages + 1):
    print('Loading page', page)
    index_page = urllib.request.urlopen(base_url.format(str(page)))
    soup = BSoup(index_page.read(), 'html.parser')
    ul = soup.find('ul', {'class': 'content_list'})
    for document in ul.find_all('li'):
        url = 'http://terms.naver.com' + document.find('strong', {'class': 'title'})\
                .find('a')['href']
        page = BSoup(urllib.request.urlopen(url).read(), 'html.parser')
        title = page.find('h2', {'class': 'headword'}).text
        if page.find('img', {'source': '내 취향에 딱 맞는 125가지 위스키 수첩'}) == None \
            or (page.find('div', {'class' : 'att_type'}) == None and page.find('img', {'id': 'innerImage0'}) == None):
            print(title, url, ' => None')
            continue
        try:
            paragraph = page.find('div', {'id': 'size_ct', 'class': 'size_ct_v2'}).find_all('p', {'class' : 'txt'})[0]
        except Exception as e:
            print(page.find('div', {'id': 'size_ct', 'class': 'size_ct_v2'}))
            errors.append({
                'url': url,
                'reason': e
            })
            continue
        print(title, url)
        text = paragraph.text
        table = page.find('table', {'class': 'tmp_profile_tb'}) 
        drink = {
            'name': title,
            'url': url
        }
        if table != None:
            table_row = table.find_all('tr')
            for row in table_row:
                query = row.find('span', {'class': 'title'})
                if query == '알코올 도수':
                    drink['percentage'] = row.find('td').text.replace('ABV', '')
                    break
        drink['explanation'] = text
        alcohols.append(drink)
with open('result.json', 'w') as fw:
    fw.write(json.dumps(alcohols))
with open('errors.json', 'w') as fw:
    fw.write(str(errors))

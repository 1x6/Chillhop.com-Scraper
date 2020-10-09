import random, requests, os

if os.path.exists('Scraped Songs') == False:
    os.mkdir('Scraped Songs')

while True:
    id = random.randint(7000, 10050)
    r = requests.get(f'https://mp3.chillhop.com/serve.php/?mp3={id}')
    

    header = r.headers
    content_type = header.get('content-type')

    if 'mpeg' in content_type.lower():
        print(f'Content OK - Downloaded {id}')
        open(os.path.join('Scraped Songs',f'{id}.mp3'), 'wb').write(r.content)

    else:
        print('Content Type not identified as mp3 OR invalid id.')

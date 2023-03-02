import ebooklib
from ebooklib import epub
import os
from pathlib import Path
import re

def convert(path):
    if not path.endswith('.epub'):
        raise ValueError('Wrong file type there, buddy')
    html_dir = Path(Path(path).stem)
    if html_dir.exists():
        print('Directory already exists.')
        while True:
            confirmation = input(f'Overwrite "{html_dir}"? (y/n) > ')
            if confirmation.lower() == 'n': return
            elif confirmation.lower() == 'y': break
            else: print('Enter "y" for "yes" or "n" for "no"')
    html_dir.mkdir(exist_ok=True)
    book = epub.read_epub(path)
    arr = []
    #ext = ''
    toc = ''
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            arr.append(item.get_name())
            #if ext == '':
            #    ext = os.path.splitext(item.get_name())[1]
            if toc == '' and item.get_name()[0:3] == 'toc':
                toc = item.get_name()
    if toc != '':
        print('Find toc file!')
    else:
        print('Could not find toc file!')
        return
    leng = len(arr)
    jArr = 0
    a3 = ''
    aCont = '<a href="' + toc + '">Contents</a>'
    for item in book.get_items():
        doc = html_dir / item.get_name()
        os.makedirs(os.path.dirname(doc), exist_ok=True)
        content = item.get_content()
        if item.get_type() != ebooklib.ITEM_IMAGE:
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                title = os.path.splitext(item.get_name())[0]
                with open(doc, 'w') as f:
                    content = content.decode()
                    content = re.sub(r'<a (.+?)\/>', r'<a \1></a>', content)
                    content = re.sub(r'<head/>', r'<head><title>%s</title><script type="text/javascript" src="/js-and-css/js/inject.js"></script><script type="text/javascript" src="file:///media/storage418Gb/Users/parsh/Documents/Books/js-and-css/js/inject.js"></script><script type="text/javascript" src="file:///F:/Users/parsh/Documents/Books/js-and-css/js/inject.js"></script></head>'%title, content)
                    if jArr == 0:
                        a3 = aCont + '<span> | </span><a href="' + arr[jArr + 1] + '">Next &gt;</a>'
                    elif jArr >= leng - 1:
                        a3 = '<a href="' + arr[jArr - 1] + '">&lt; Previous</a><span> | </span>' + aCont
                    else:
                        a3 = '<a href="' + arr[jArr - 1] + '">&lt; Previous</a><span> | </span>' + aCont + '<span> | </span><a href="' + arr[jArr + 1] + '">Next &gt;</a>'
                    jArr = jArr + 1
                    content = re.sub(r'<body>', r'<body><header>%s</header>'%a3, content)
                    #if title == 'toc01':
                    if title[0:3] == 'toc':
                        content = content.replace('</head>', f'<link href="/js-and-css/css/collapsible-style.css" rel="stylesheet" type="text/css"></link><link href="file:///media/storage418Gb/Users/parsh/Documents/Books/js-and-css/css/collapsible-style.css" rel="stylesheet" type="text/css"></link><link href="file:///F:/Users/parsh/Documents/Books/js-and-css/css/collapsible-style.css" rel="stylesheet" type="text/css"></link></head>')
                        content = content.replace('</body>', f'<script type="text/javascript" src="/js-and-css/js/collapsible-script.js"></script><script type="text/javascript" src="file:///media/storage418Gb/Users/parsh/Documents/Books/js-and-css/js/collapsible-script.js"></script><script type="text/javascript" src="file:///F:/Users/parsh/Documents/Books/js-and-css/js/collapsible-script.js"></script></body>')
                    f.write(content)
            else:
                with open(doc, 'wb') as f:
                    f.write(content)
        else:
            with open(doc, 'wb') as f:
                f.write(content)
    print(f'"{html_dir}" folder created.')
    print(f'{html_dir}/{toc} - start page with Table of Content')


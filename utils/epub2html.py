import ebooklib
from ebooklib import epub
import os
from pathlib import Path
import html

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
    for item in book.get_items():
        doc = html_dir / item.get_name()
        os.makedirs(os.path.dirname(doc), exist_ok=True)
        content = item.get_content()
        if item.get_type() != ebooklib.ITEM_IMAGE:
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                with open(doc, 'w') as f:
                    content = content.decode().replace('<head/>', '<head><script type="text/javascript" src="/js-and-css/js/inject.js"></script><script type="text/javascript" src="file:///media/storage418Gb/Users/parsh/Documents/Books/js-and-css/js/inject.js"></script><script type="text/javascript" src="file:///F:/Users/parsh/Documents/Books/js-and-css/js/inject.js"></script></head>')
                    f.write(html.unescape(content))
            else:
                with open(doc, 'wb') as f:
                    f.write(content)
        else:
            with open(doc, 'wb') as f:
                f.write(content)
    print(f'"{html_dir}" created.')

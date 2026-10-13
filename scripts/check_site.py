"""Check published pages, gallery assets, and intact standalone interactives."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, urljoin
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
source = Path(__file__).resolve().parents[1] / 'docs'
required = ['index.html', 'research/index.html', 'personal/index.html',
            'teaching/index.html', 'cv/index.html', 'contact/index.html',
            'Interactives/index.html', '404.html', 'sitemap.xml']
errors = []
for name in required:
    if not (root / name).is_file():
        errors.append(f'Missing required output: {name}')

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value:
                self.urls.append(value)

# Validate all generated HTML, including links from the gallery and teaching hub.
# External URLs are outside this build check and are not fetched.
for page in root.rglob('*.html'):
    parser = Links()
    parser.feed(page.read_text(encoding='utf-8'))
    page_url = '/' + page.relative_to(root).as_posix()
    for url in parser.urls:
        u = urlsplit(url)
        if u.scheme not in ('', 'http', 'https'):
            continue
        if u.netloc and u.netloc.lower() != 'jamesdean595.github.io':
            continue
        if not u.path:
            continue
        path = unquote(urlsplit(urljoin(page_url, u.path)).path).lstrip('/')
        target = root / path
        if not target.is_file() and not (target / 'index.html').is_file() and not Path(str(target) + '.html').is_file():
            errors.append(f'{page.relative_to(root)} → {url}')

for original in (source / 'Interactives').rglob('*'):
    if original.is_file():
        output = root / original.relative_to(source)
        if not output.is_file() or original.read_bytes() != output.read_bytes():
            errors.append(f'Interactive missing or changed by build: {original.relative_to(source)}')
if (root / 'archive').exists() or (root / 'WEBSITE_AUDIT.md').exists():
    errors.append('Repository-only materials leaked into published output')
if errors:
    print('\n'.join(sorted(set(errors))))
    sys.exit(1)
print(f'PASS: required pages, all local HTML links, and standalone interactives ({len(list(root.rglob("*.html")))} HTML files).')

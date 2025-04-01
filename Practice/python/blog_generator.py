import os
import markdown
import re
from jinja2 import Template

BLOG_DIR = 'blogs'
OUTPUT_DIR = 'output'
TEMPLATE_PATH = 'templates/post_template.html'
INDEX_TEMPLATE_PATH = 'templates/base.html'
CSS_FILE = 'style.css'
JS_FILE = 'script.js'

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_blog_metadata(content):
    # Extract metadata from markdown frontmatter
    meta = {
        'title': 'Untitled',
        'author': 'Anonymous',
        'tags': [],
    }
    match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        content = content[match.end():]  # Remove frontmatter
        for line in frontmatter.split('\n'):
            key, _, value = line.partition(':')
            if key.strip() == 'tags':
                meta['tags'] = [tag.strip() for tag in value.split(',')]
            else:
                meta[key.strip()] = value.strip()
    return meta, content

def convert_markdown_to_html(md_content):
    return markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])

def generate_blog_page(filename, meta, html_content):
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = Template(f.read())

    rendered = template.render(
        title=meta['title'],
        author=meta['author'],
        tags=meta['tags'],
        content=html_content,
    )

    output_path = os.path.join(OUTPUT_DIR, filename.replace('.md', '.html'))
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered)
    return output_path

def generate_index_page(blog_data):
    with open(INDEX_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = Template(f.read())

    rendered = template.render(blogs=blog_data)

    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(rendered)

def copy_assets():
    for file in [CSS_FILE, JS_FILE]:
        with open(file, 'r', encoding='utf-8') as src:
            with open(os.path.join(OUTPUT_DIR, file), 'w', encoding='utf-8') as dst:
                dst.write(src.read())

def main():
    blog_data = []
    for file in os.listdir(BLOG_DIR):
        if file.endswith('.md'):
            with open(os.path.join(BLOG_DIR, file), 'r', encoding='utf-8') as f:
                content = f.read()
            meta, content_body = get_blog_metadata(content)
            html_content = convert_markdown_to_html(content_body)
            page_path = generate_blog_page(file, meta, html_content)
            blog_data.append({
                'title': meta['title'],
                'author': meta['author'],
                'tags': meta['tags'],
                'filename': os.path.basename(page_path),
            })

    generate_index_page(blog_data)
    copy_assets()
    print(f"✅ Blog generated with {len(blog_data)} posts!")

if __name__ == '__main__':
    main()

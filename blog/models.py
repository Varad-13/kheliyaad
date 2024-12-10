from django.db import models
import markdown2
from bs4 import BeautifulSoup
import re

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Blog(models.Model):
    thumbnail = models.ImageField(upload_to='static/thumbnails/')
    title = models.TextField()
    summary = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='blogs')
    body = models.TextField()
    body_html = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_updated']
    
    def save(self, *args, **kwargs):
        # If body_html is empty, generate it
        self.body_html = self.parse_markdown(self.body)
        
        # Call the parent save method to save the model
        super().save(*args, **kwargs)

    def parse_markdown(self, markdown_text):
        html_content = markdown2.markdown(markdown_text, extras=["fenced-code-blocks", "tables"])
        soup = BeautifulSoup(html_content, 'html.parser')

        # Handle Headers (h1, h2, ..., h6)
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            tag['class'] = tag.get('class', []) + ['font-bold', 'my-4']
            if tag.name == 'h1':
                tag['class'] += ['text-3xl']
            elif tag.name == 'h2':
                tag['class'] += ['text-2xl']
            elif tag.name == 'h3':
                tag['class'] += ['text-xl']
            elif tag.name == 'h4':
                tag['class'] += ['text-lg']
            elif tag.name == 'h5':
                tag['class'] += ['text-base']
            elif tag.name == 'h6':
                tag['class'] += ['text-sm']

            if not tag.get('id'):
                header_id = re.sub(r'\W+', '-', tag.get_text(strip=True)).lower()
                tag['id'] = header_id

        # Handle Paragraphs
        for tag in soup.find_all('p'):
            tag['class'] = tag.get('class', []) + ['my-2']

        # Handle Lists (ul, ol)
        for tag in soup.find_all('ul'):
            tag['class'] = tag.get('class', []) + ['list-disc', 'ml-5']

        for tag in soup.find_all('ol'):
            tag['class'] = tag.get('class', []) + ['list-decimal', 'ml-5']

        # Handle Inline Code
        for tag in soup.find_all('code'):
            tag['class'] = tag.get('class', []) + ['px-1']

        # Handle Preformatted Code Blocks
        for tag in soup.find_all('pre'):
            mockup_code_div = soup.new_tag('div', **{'class': 'mockup-code'})
            tag['class'] = tag.get('class', []) + ['rounded', 'p-4', 'my-4', 'overflow-auto']
            code_tag = tag.find('code')
            if code_tag:
                code_tag.extract()
                tag.append(code_tag)
            tag.wrap(mockup_code_div)

        # Handle Tables
        for tag in soup.find_all('table'):
            tag['class'] = tag.get('class', []) + ['table-auto', 'w-full', 'my-4', 'border-collapse']
            for th in tag.find_all('th'):
                th['class'] = th.get('class', []) + ['border', 'px-4', 'py-2']
            for td in tag.find_all('td'):
                td['class'] = td.get('class', []) + ['border', 'px-4', 'py-2']

        # Handle Links (a)
        for tag in soup.find_all('a'):
            tag['class'] = tag.get('class', []) + ['text-blue-600', 'dark:text-blue-400', 'hover:text-accent']
            tag['target'] = '_blank'  # Open links in a new tab

        return str(soup)
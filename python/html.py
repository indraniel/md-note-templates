#!/usr/bin/env python

from __future__ import print_function

from markdown import markdown
from jinja2 import Template

import sys, os, datetime, re, argparse

def check_extension(filename, type):
    filepath = os.path.basename(filename)
    (basename, extension) = os.path.splitext(filepath)
    if extension != type:
        return False
    return True

class Render(object):
    def __init__(self, mdFile):
        if check_extension(mdFile, '.md'):
            self.md = mdFile
        else:
            msg = "'{}' isn't a markdown file!".format(mdFile)
            raise ValueError(msg)

    def process_header(self):
        attrs = {}

        with open(self.md, 'r') as f:
            header_flag = False
            for line in f:
                if line.startswith('---'):
                    if header_flag == False:
                        header_flag = True
                        continue
                    else:
                        header_flag = False
                        break

                if header_flag:
                    (key, value) = line.split(':', 2)
                    key = key.lower()
                    value = value.rstrip("\n")
                    value = value.strip(" ")
                    attrs[key] = value

        if 'title' not in attrs:
            attrs['title'] = 'Document'

        if 'date' not in attrs:
            today = datetime.date.today()
            attrs['date'] = today.strftime("%Y-%m-%d")

        self.metadata = attrs

    def get_markdown_text(self):
        text = []

        with open(self.md, 'r') as f:
            header_flag = False
            for line in f:
                if line.startswith('---'):
                    if header_flag == False:
                        header_flag = True
                        continue
                    else:
                        header_flag = False
                        continue

                if header_flag == False:
                    text.append(line)

        txt = ''.join(text)
        return txt

    def render_html(self, body):
        base = self.base_template()
        template = Template(base)
        (title, date) = (self.metadata['title'], self.metadata['date'])
        html = template.render(title=title, date=date, body=body)
        return html

    def base_template(self):
        base = """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta http-equiv="content-type" content="text/html; charset=UTF-8">
            <title>{{ title }}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
            <link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/indraniel/md-note-templates/master/css/github-markdown.css" />
            <link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/indraniel/md-note-templates/master/css/github-highlight.css" />
          </head>
          <body>
            <article class="markdown-body">
              <div class="title">
                <p>{{ date }}</p>
                <h1>{{ title }}</h1>
              </div>

              {{ body }}

            </article>
            <script type="text/x-mathjax-config">
            MathJax.Hub.Config({
                  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
            });
            </script>
            <script type="text/javascript"
              src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
              </script>
            <script src="https://cdn.rawgit.com/indraniel/md-note-templates/master/js/highlight.pack.js" type="text/javascript"></script>
            <script>hljs.initHighlightingOnLoad();</script>
          </body>
        </html>
        """
        return base

    def write_html(self, file, text):
        with open(file, 'w') as f:
            print(text, file=f)

    def generate_html(self, html=None):
        if html is None:
            filename = os.path.basename(self.md)
            (basename, extension) = os.path.splitext(filename)
            html = '.'.join([basename, 'html'])

        src = self.get_markdown_text()
        body = markdown(src, extensions=['gfm'])
        rendered_html = self.render_html(body)

        self.write_html(html, rendered_html)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-dir",
                        action="store", type=str, dest="outdir",
                        default="final")
    parser.add_argument("file", type=str)
    args = parser.parse_args()
    r = Render(args.file)
    r.process_header()
    filename = os.path.basename(args.file)
    (basename, extension) = os.path.splitext(filename)
    html = '.'.join([basename, 'html'])
    html = '/'.join([args.outdir, html])
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    r.generate_html(html=html)

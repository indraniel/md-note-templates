# md-note-tools

These are homebrewed templates and scripts I use for rendering my analytical markdown-based notes.  They aren't really considered to be production quality.  A lot of polish is still needed, but they work for my ad-hoc needs so far.

## USAGE

    git clone https://github.com/indraniel/md-note-tools
    cd md-note-tools
        
    # setup python environment
    virtualenv /path/to/venv
    source /path/to/venv/bin/activate
    pip install -r python/requirements.txt
        
    # setup R environment
    export R_LIBS=/path/to/rpkgs
    ./R/install-packages.r
        
    # contruct static html files    
    ./R/knit.r -o /path/to/final-output -i /path/to/note.Rmd
    python python/html.py -o /path/to/final-output /path/to/note.md
        
The `/path/to/final-output` directory contains the static figures and html
files.
    
## NOTES

The `js/highlight.pack.js` and `css/github-highlight.css` code was custom
rendered from [highlightjs.org][1].

The `css/github-markdown.css` stylesheet was based upon
[sindreshorhus/github-markdown-css][2].

The static CSS and JS files are being served via [MaxCDN][3].  See [rawgit][4]
for details on setting this up.

## LICENSE

BSD

[1]: https://highlightjs.org/download/
[2]: https://github.com/sindresorhus/github-markdown-css
[3]: http://www.maxcdn.com/
[4]: http://rawgit.com/

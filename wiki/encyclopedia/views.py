from django.shortcuts import render

from . import util

from markdown2 import Markdown
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page_direct(request, title):
    
    if title in util.list_entries():
        page_entry = util.get_entry(title)
        page = markdowner.convert(page_entry)

        return render(request, "encyclopedia/entries_page.html", {
            'page_entry': page,
            'title': title
        })
    else:
        return render(request, "enclopedia/error_page.html")


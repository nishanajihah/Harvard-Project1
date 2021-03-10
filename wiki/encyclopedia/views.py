from django.shortcuts import render

from . import util

from markdown2 import Markdown

mark = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page_direct(request, title):

    page_entry = util.get_entry(title)
    
    return render(request, "encyclopedia/entries_page.html", {
        'page': mark.cover(page_entry),
        'title': title,
    })
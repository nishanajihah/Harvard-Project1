from django.shortcuts import render

from . import util

from markdown2 import Markdown
markdowner = Markdown()

def index(request):
    # Home Page
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):

    md_file = util.get_entry(title)
    
    if md_file != None:

        # If page exist convert md file to html and display
        convert_md = markdowner.convert(md_file)

        page_content = {
            'title': title,
            'page': convert_md
        }

        return render(request, "encyclopedia/entry_page.html", page_content)
    else:
        # if it does not exist diplay the error message
        return render(request, "encyclopedia/error_page.html", {
            "message": f"Error: '{title}' page does not exist."
        })


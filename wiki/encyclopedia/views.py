from django.http import HttpResponseRedirect
from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from . import util

from markdown2 import Markdown
markdowner = Markdown()


class searchForm (forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
      "class": "search",
      "placeholder": "Search Encyclopedia"}))


def index(request):

    # Home
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        # "search_form" : searchForm()
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
            "message": f"Error: '{title}' page was not found."
        })


def search(request):

    entries = util.list_entries()
    title = request.GET.get("q", "")

    # If the title search exist it show the content
    if util.get_entry(title) != None: 

        return render(request, "encyclopedia/entry_page.html", {
            'title': title,
            'page': markdowner.convert(util.get_entry(title)),
        })
    
    # else if when the search are short form like "py" or "o". T
    # Then it will show the list of the exist file
    # elif util.get_entry(title) == None:

    #     if title in entries:
    #         return redirect(reverse('page', title))

    #     results = [page for page in entries if 'title'.lower() in page.lower()]
    #     return render(request, "encyclopedia/search_page.html", {
    #         "entries": results,
    #     })

    # Else it will show an error message and  
    # it will show a list of the exist file that relate with the query insert in.
    else:
        # if it does not exist diplay the error message
        return render(request, "encyclopedia/error_page.html", {
            "message": f"Error: '{title}' page was not found."
        })

            
        # return render(request, "enc:page", page_content) 
    
    # if title in entries:
    #     return redirect(page, query)

    # results = [page for page in entries if query.lower() in page.lower()]
    # return render(request, "encyclopedia/search_page.html", {
    #     "entries": results,
    # })
  

    

    


   


    

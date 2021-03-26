from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from . import util

from markdown2 import Markdown
markdowner = Markdown()

# class Search(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class' : 'search', 
#             'placeholder': 'Search'
#         }))

def index(request):

    entries = util.list_entries()
   

    # Home
#     if request.method == "POST":
#         form = Search(request.POST)

#         if form.is_valid():
#             title = form.cleaned_data['title']
#             md_file = util.get_entry(title)

#             if md_file:
#                 convert_md = markdowner.convert(md_file)

#                 page_content = {
#                     'title': title,
#                     'page': convert_md,
#                     'form': Search()
#                 }

#                 return render(request, "encyclopedia/index.html", page_content)

#             if title.lower():
#                 searching.append(title)
#                 page_content = {
#                     'searching': searching;
#                     'form': Search()
#                 }

#             return render(request, "encyclopedia/search.html", page_content)
#         else:

#             show_related_titles = util.related_titles(title)

#             page_content = {
#                 'title': title,
#                 'show_related_titles': show_related_titles ,
#                 'form': Search()
#             }
# 
#             return render(request, "encyclopedia/search_page.html", page_content)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": Search()
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

     searching = []

    result = request.GET.get('q','')
    if(util.get_entry(result) != None):
        return HttpResponseRedirect(Reversible("page", kwargs={"page": result}))
    else:
        related_titles = util.related_titles(title)

        return render(request, "encyclopedia/search.html", {
            "title": title,
            "related_titles": related_titles,
            "search_form": SearchForm()
        })

    # return HttpResponseRedirect(Reversible('index'))

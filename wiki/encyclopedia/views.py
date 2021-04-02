from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse

from . import util

from markdown2 import Markdown
markdowner = Markdown()


# class searchForm (forms.Form):
#     # Search Form
#     title = forms.CharField(label="", widget=forms.TextInput(attrs={
#       "class": "search",
#       "placeholder": "Search Encyclopedia"}))

class createForm(forms.Form):
    # Create Form
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "The Page Title"}))
    textarea = forms.CharField(label='', widget=forms.Textarea(attrs={
        "placeholder": "Type in the content (Do follow the markdown format when creating it)"
    }))


def index(request):

    # Home
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
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
    title = request.POST.get("q")

    if request.method == "POST":

        # If the title search exist it show the content
        if util.get_entry(title) != None:

            return render(request, "encyclopedia/entry_page.html", {
                'title': title,
                'page': markdowner.convert(util.get_entry(title)),
            })

        # Else it will show an error message and
        # it will show a list of the exist file that relate with the query insert in. 
        else:
            if title in entries:
                return redirect(reverse('page', title))

            results = [page for page in entries if title.lower() in page.lower()]
            return render(request, "encyclopedia/search_page.html", {
                "title": title,
                "entries": results
            })
    else:
        # if it does not exist diplay the error message
        return render(request, "encyclopedia/error_page.html", {
            "title": title,
            "message": f"Error: '{title}' page was not found.",
            "entries": util.get_entries
        })
           


def create(request):

    if request.method == "POST":
         
        createForm = createForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            textarea = form.cleaned_data["textarea"]
            

            return HttpResponseRedirect(reverse("enc:create"))

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Item


class Home(generic.ListView):
    template_name = "stock/home.html"
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.order_by('name')

def go_home(request):
    return HttpResponse("<script>location.href = 'stock';</script>")

def get_items():
    try:
        items = Item.objects.order_by('name')
    except:
        raise Http404("Error: 404.")
    else:
        return items

def add_item(request):
    try:
        item_to_add = Item(name=request.POST["name"],
                           price=request.POST["price"],
                           number_available=request.POST["number_available"])
    except:
        messages.error(request, "Error. Please retry")
        return HttpResponseRedirect(reverse("stock:home"))
    else:
        if len(Item.objects.filter(name=item_to_add.name)) == 0:
            item_to_add.save()
        return HttpResponseRedirect(reverse("stock:home"))
    
def delete_items(request):
    try:
        items_to_remove = []
        for item_name in request.POST.getlist("delete[]"):
            items_to_remove.append(Item.objects.get(name=item_name))
    except:
        messages.error(request, "Error. Please retry")
        return HttpResponseRedirect(reverse("stock:home"))
    else:
        for item in items_to_remove:
            item.delete()
        return HttpResponseRedirect(reverse("stock:home"))
    
def edit_items(request):
    try:
        item_name = request.POST["name"]
        item = Item.objects.get(name=item_name)
    except:
        messages.error(request, "Error. Please retry")
        return HttpResponseRedirect(reverse("stock:home"))
    else:
        item.price = request.POST["price_" + item.name]
        item.number_available = request.POST["number_available_" + item.name]
        item.save()
        return HttpResponseRedirect(reverse("stock:home"))

def search_to_view(request):
    html_text = """<tr>
            <th></th>
            <th>Item name</th>
            <th>Price</th>
            <th>Number Available</th>
            </tr>"""
    items = Item.objects.filter(
                            name__startswith=request.GET["q"]).order_by("name")
    if len(items) == 0:
        html_text += """<tr>
                        <td></td>
                        <td>Item not found </td>
                        <td>0.0</td>
                        <td>0</td>
                        </tr>"""
        return HttpResponse(html_text)
    else:
        counter = 1
        for item in items:
            if counter % 2 == 0:
                html_text += "<tr class = 'dark'>"
            else:
                html_text += "<tr>"
            html_text += """<td>
                <input type="checkbox" name="delete[]" value=
                '""" + item.name + """'></td>
                <td>""" + str(item.name) + """</td>
                <td>""" + str(item.price) + """</td>
                <td>""" + str(item.number_available) + """</td>
                </tr>"""
            counter += 1
        return HttpResponse(html_text)


def search_to_edit(request):
    html_text = """<tr>
            <th>Item name</th>
            <th>Price</th>
            <th>Number Available</th>
            <th></th>
            </tr>"""
    items = Item.objects.filter(
                            name__startswith=request.GET["q"]).order_by("name")
    if len(items) == 0:
        html_text += """<tr>
                        <td>Item not found </td>
                        <td>0.0</td>
                        <td>0</td>
                        <td></td>
                        </tr>"""
        return HttpResponse(html_text)
    else:
        counter = 1
        for item in items:
            if counter % 2 == 0:
                html_text += "<tr class = 'dark'>"
            else:
                html_text += "<tr>"
            html_text += """
                        <td>""" + str(item.name) + """</td>
                        <td><input type='text' name='price_""" + str(
                                                            item.name) + """'
                            value='""" + str(item.price) + """'></td>
                        <td><input type='text'
                            name='number_available_""" + str(item.name) + """'
                            value='""" + str(item.number_available) + """'></td>
                        <td>
                        <a style='width:90%' class='btn'
                            onclick="document.getElementById('name').value=
                            '""" + str(item.name) + """';
                            submit_form('edit_items_form')">Edit</a>
                        </td>
                        </tr>"""
            counter += 1
        return HttpResponse(html_text)

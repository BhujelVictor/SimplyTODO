from typing import Any # for using context variable to hold hold object data
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDoList, ToDoItem

class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    # overriding get_queryset() to return only the items relative to list_id
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self):
        # used super() to override method from parent class to merge context data instead of creating a new one
        context = super().get_context_data()
        # adding the associated 'ToDolist' object to the context which allows the template to access the object itself
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


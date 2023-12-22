from django.test import TestCase
from django.urls import reverse
from django.test import TestCase

from .models import ToDoList, ToDoItem



class ToDoListTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        ToDoList.objects.all().delete()
    
    def test_create_todo_list(self):
        new_todo_list = ToDoList.objects.create(title="New Todo List")

        self.assertEqual(new_todo_list.title, "New Todo List")
        new_todo_list.delete()


    def test_get_all_todo_lists(self):
        ToDoList.objects.create(title="My First Todo List")
        ToDoList.objects.create(title="My Second Todo List")

        todo_lists = ToDoList.objects.all()
        self.assertEqual(len(todo_lists), 2)

    def test_update_todo_list(self):
        new_todo_list = ToDoList.objects.create(title="My New Todo List")
        new_todo_list.title = "My Updated Todo List"
        new_todo_list.save()

        updated_todo_list = ToDoList.objects.get(id=new_todo_list.id)

        self.assertEqual(updated_todo_list.title, "My Updated Todo List")

    def test_delete_todo_item(self):
        new_todo_item = ToDoItem.objects.create(
            title="My New Todo Item",
            todo_list=ToDoList.objects.create(title="My New Todo List"),
            created_date="2023-12-22",
            due_date="2023-12-29",
            is_done=False,
        )

        todo_item_to_delete = ToDoItem.objects.get(pk=new_todo_item.pk)
        todo_item_to_delete.delete()

        todo_items = ToDoItem.objects.all()
        self.assertEqual(len(todo_items), 0)


    def test_todo_item_delete_response(self):
        self.todo_list = ToDoList.objects.create(title="Test List")
        self.todo_item = ToDoItem.objects.create(
            title="Test Item",
            todo_list=self.todo_list,
            created_date="2023-01-01",
            due_date="2023-01-07",
            is_done=False,
        )
        url = reverse("item-delete", args=[str(self.todo_list.id), str(self.todo_item.id)])
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, reverse("list", args=[str(self.todo_list.id)]))
        todo_items = ToDoItem.objects.all()
        self.assertEqual(len(todo_items), 0)
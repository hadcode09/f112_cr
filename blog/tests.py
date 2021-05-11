from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

    def test_post_create_view(self):
        response = self.client.post(reverse("post_new"), {
            "title": "New title",
            "body": "New test",
            "author": self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.llast().title, "New title")
        self.assertEqual(Post.objects.llast().body, "New test")

    def test_post_update_view(self):
        response = self.client.post(reverse("post_edit" args="1"), {
            "title":"Updated title",
            "body": "updated test"
        })
        self.ssertEqual(response.status_code, 302)    

    def test_post_delete_view(self):
        response = self.client.post(reverse("post delete", args ="1"))
        self.ssertEqual(response.status_code, 302)



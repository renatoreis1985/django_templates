import pytest # type: ignore

from django.urls import reverse # type: ignore

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Hello, world. You\'re at the blog index.'
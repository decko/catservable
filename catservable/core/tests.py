from django.urls import reverse




def test_url_to_list_cat_breeds():

    viewname = "core:breeds_list"

    url = reverse(viewname)

    assert url == "/breeds/"

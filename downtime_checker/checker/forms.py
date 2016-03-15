from django.forms import Form, URLField

class URLForm(Form):

    url = URLField()

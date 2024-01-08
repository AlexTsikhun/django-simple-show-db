from django.shortcuts import render

from .models import Elements


# Create your views here.
def show_elem(request):
    elements = Elements.objects.all()
    # show data from dict
    context = {"elements": elements}
    # without `templates` becouse in settings.py described logic
    return render(request, "show/show_elements.html", context)

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *

from .models import *


def index(request):
    search_query = request.GET.get("search", "")
    if search_query:
        all_films = Film.objects.filter(title__icontains=search_query)
    else:
        all_films = Film.objects.all()

    paginator = Paginator(all_films, 1)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)
    return render(request, "main/index.html", {"page_object": page, "first_page": 1})


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    print(film.__dict__)
    return render(request, "main/film_detail.html", context={"film": film})


class FilmCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = FilmForm()
        return render(request, "main/create_film.html", context={"form": form})

    def post(self, request):
        bound_form = FilmForm(data=request.POST, files=request.FILES)
        if bound_form.is_valid():
            new_film = bound_form.save()
            return redirect(new_film)
        return render(request, "main/create_film.html", context={"form": bound_form})


class FilmUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        bound_form = FilmForm(instance=film)
        return render(request, "main/update_film.html", context={"film": film, "form": bound_form})

    def post(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        bound_form = FilmForm(request.POST, request.FILES, instance=film)

        if bound_form.is_valid():
            updated_film = bound_form.save()
            return redirect (updated_film)
        return render(request, "main/update_film.html", context={"film": film, "form": bound_form})


class FilmDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        return render(request, "main/delete_film.html", context={"film": film})

    def post(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        film.delete()
        return redirect(reverse("index"))
    # model = Film
    # template_name = "main/delete_film.html"
    # success_url = reverse_lazy("index")

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     messages.add_message(request, messages.SUCCESS, "Successfully deleted!")
    #     return HttpResponseRedirect(success_url)




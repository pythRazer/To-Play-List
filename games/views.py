from django.shortcuts import render, redirect
from .models import Game
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
# Create your views here.

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields=('title', 'platform', 'status')

class GameListView(GameForm, ListView):

    model = Game
    template_name = 'games/game_list.html'
    form_class = GameForm
    
    def post(self, request):
        form = self.form_class(request.POST)
        print("KK")
      
        if(form.is_valid()):
            form.save()
            model.save()
            print("YY")
            return HttpResponseRedirect(self.request.path_info)
        return render(request, "games/game_list.html", {'form':form})

   
class GameDelete(DeleteView):
    
    model = Game
    success_url = reverse_lazy('home')

class GameAdd(CreateView):
    model = Game
    template_name = "games/game_form.html"
    fields = ('title', 'platform', 'status')
    success_url = reverse_lazy('home')
class GameEdit(UpdateView):
    model = Game
    fields = ('title', 'platform', 'status')
    template_name = 'games/game_edit.html'
    success_url = reverse_lazy('home')






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
        fields=('title', 'platform')

class GameListView(GameForm, ListView):

    model = Game
    template_name = 'games/game_list.html'
    form_class = GameForm
    
    def post(self, request):
        form = self.form_class(request.POST)
        print("KK")
      
        if(form.is_valid()):
            form.save()
            print("YY")
            return HttpResponseRedirect(self.request.path_info)
        return render(request, self.template_name, {'form':form})

   
class GameDelete(DeleteView):
    
    model = Game
    success_url = reverse_lazy('home')






from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator

import os
from django.conf import settings
from django.http import HttpResponse

import calendar
from calendar import HTMLCalendar
from DimosoApp.models import *
from DimosoApp.forms import *



# Create your views here.
def user_login(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        messages.success(request,"username or password is incorrect")
        return redirect('user_login')
        
   
        
    
        
    return render(request,'DimosoApp/user_login.html')
def base(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='simba').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}
	return render(request, 'DimosoApp/base.html', context)

def readmore(request):
	
	return render(request, 'DimosoApp/readmore.html')
def sampo(request):
	
	return render(request, 'basic/sample.html')
def home(request):
	teams = Teams.objects.all().order_by('id')

	context = {
	    "teams":teams

	}


	
	return render(request, 'DimosoApp/home.html', context)

    
def SimbaHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='simba').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'simba/home.html', context)


def SimbaAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'simba/SimbaAssistsDetail.html', context)
def SimbaGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'simba/SimbaGoalsDetail.html', context)
def SimbaYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'simba/SimbaYellowDetail.html', context)
def SimbaRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'simba/SimbaRedDetail.html', context)
def SimbaSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'simba/SimbaSummaryDetail.html', context)

class add_simba_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('SimbaHomePage')
    success_message = "Player Added Successfully"

class update_simba_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('SimbaHomePage')
    success_message = "Player Updated Successfully" 
def delete_simba_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('SimbaHomePage')

def msimamo_wa_league(request):
	msimamo = Msimamo.objects.all().order_by('-id')

	context = {
	    "msimamo":msimamo

	}
	return render(request, 'basic/msimamo_wa_league.html', context)
def ratiba_ya_league(request):
	ratiba = Ratiba.objects.all().order_by('-id')

	context = {
	    "ratiba":ratiba

	}
	return render(request, 'basic/ratiba_ya_league.html', context)
def matokeo_ya_league_leo(request):
	form = ResultsForm(request.POST or None)
	matokeo = Results.objects.filter(name="leo")
	siku = Results.objects.all()


	context = {
	    "matokeo":matokeo,
	    "siku":siku

	}
	return render(request, 'basic/matokeo_ya_league_leo.html', context)
def matokeo_ya_league_jana(request):
	form = ResultsForm(request.POST or None)
	matokeo = Results.objects.filter(name="jana")
	siku = Results.objects.all()


	context = {
	    "matokeo":matokeo,
	    "siku":siku

	}
	return render(request, 'basic/matokeo_ya_league_jana.html', context)
def matokeo_ya_league_juzi(request):
	form = ResultsForm(request.POST or None)
	matokeo = Results.objects.filter(name="juzi")
	siku = Results.objects.all()


	context = {
	    "matokeo":matokeo,
	    "siku":siku

	}
	return render(request, 'basic/matokeo_ya_league_juzi.html', context)



class add_matokeo_ya_mechi(SuccessMessageMixin, CreateView):
    model = Results
    template_name = 'basic/add_matokeo_ya_mechi.html'
    form_class = ResultsForm
    success_url = reverse_lazy('home')
    success_message = "Results Added Successfully"

class update_matokeo_ya_mechi(SuccessMessageMixin, UpdateView):
    model = Results
    template_name = 'basic/add_matokeo_ya_mechi.html'
    form_class = ResultsForm
    success_url = reverse_lazy('home')
    success_message = "Results Updated Successfully" 
def delete_matokeo_ya_mechi(request, pk):
    player = get_object_or_404(Results, id=pk)
    player.delete()
    messages.success(request, "Results deleted Successfully")
    return redirect('home')

class add_ratiba_ya_mechi(SuccessMessageMixin, CreateView):
    model = Ratiba
    template_name = 'basic/add_ratiba_ya_mechi.html'
    form_class = RatibaForm
    success_url = reverse_lazy('ratiba_ya_league')
    success_message = "Ratiba Added Successfully"

class update_ratiba_ya_mechi(SuccessMessageMixin, UpdateView):
    model = Ratiba
    template_name = 'basic/add_ratiba_ya_mechi.html'
    form_class = RatibaForm
    success_url = reverse_lazy('ratiba_ya_league')
    success_message = "Ratiba Updated Successfully" 
def delete_ratiba_ya_mechi(request, pk):
    player = get_object_or_404(Ratiba, id=pk)
    player.delete()
    messages.success(request, "Ratiba deleted Successfully")
    return redirect('ratiba_ya_league')


 #kwa ajili ya msimamo wa league
class add_msimamo_wa_league(SuccessMessageMixin, CreateView):
    model = Msimamo
    template_name = 'basic/add_msimamo_wa_league.html'
    form_class = MsimamoForm
    success_url = reverse_lazy('msimamo_wa_league')
    success_message = "Data Added Successfully"

class update_msimamo_wa_league(SuccessMessageMixin, UpdateView):
    model = Msimamo
    template_name = 'basic/add_msimamo_wa_league.html'
    form_class = MsimamoForm
    success_url = reverse_lazy('msimamo_wa_league')
    success_message = "Data Updated Successfully" 
def delete_msimamo_wa_league(request, pk):
    player = get_object_or_404(Msimamo, id=pk)
    player.delete()
    messages.success(request, "Data deleted Successfully")
    return redirect('msimamo_wa_league')




#VIEWS KWA AJILI YA YANGA
def YangaHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='yanga').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'yanga/YangaHomePage.html', context)


def YangaAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'yanga/YangaAssistsDetail.html', context)
def YangaGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'yanga/YangaGoalsDetail.html', context)
def YangaYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'yanga/YangaYellowDetail.html', context)
def YangaRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'yanga/YangaRedDetail.html', context)

def YangaSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'yanga/YangaSummaryDetail.html', context)

class add_yanga_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('YangaHomePage')
    success_message = "Player Added Successfully"

class update_yanga_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('YangaHomePage')
    success_message = "Player Updated Successfully" 
def delete_yanga_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('YangaHomePage')


#VIEWS KWA AJILI YA AZAM
def AzamHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='azam').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'azam/AzamHomePage.html', context)


def AzamAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'azam/AzamAssistsDetail.html', context)
def AzamGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'azam/AzamGoalsDetail.html', context)
def AzamYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'azam/AzamYellowDetail.html', context)
def AzamRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'azam/AzamRedDetail.html', context)

def AzamSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'azam/AzamSummaryDetail.html', context)

class add_azam_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('AzamHomePage')
    success_message = "Player Added Successfully"

class update_azam_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('AzamHomePage')
    success_message = "Player Updated Successfully" 
def delete_azam_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('AzamHomePage')


#VIEWS KWA AJILI YA NAMUNGO
def NamungoHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='namungo').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'namungo/NamungoHomePage.html', context)

def NamungoAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'namungo/NamungoAssistsDetail.html', context)
def NamungoGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'namungo/NamungoGoalsDetail.html', context)
def NamungoYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'namungo/NamungoYellowDetail.html', context)
def NamungoRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'namungo/NamungoRedDetail.html', context)

def NamungoSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'namungo/NamungoSummaryDetail.html', context)

class add_namungo_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('NamungoHomePage')
    success_message = "Player Added Successfully"

class update_namungo_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('NamungoHomePage')
    success_message = "Player Updated Successfully" 
def delete_namungo_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('NamungoHomePage')

#VIEWS KWA AJILI YA MTIBWA
def MtibwaHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='mtibwa').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'mtibwa/MtibwaHomePage.html', context)

def MtibwaAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mtibwa/MtibwaAssistsDetail.html', context)
def MtibwaGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mtibwa/MtibwaGoalsDetail.html', context)
def MtibwaYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mtibwa/MtibwaYellowDetail.html', context)
def MtibwaRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mtibwa/MtibwaRedDetail.html', context)

def MtibwaSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mtibwa/MtibwaSummaryDetail.html', context)

class add_mtibwa_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('MtibwaHomePage')
    success_message = "Player Added Successfully"

class update_mtibwa_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('MtibwaHomePage')
    success_message = "Player Updated Successfully" 
def delete_mtibwa_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('MtibwaHomePage')

#VIEWS KWA AJILI YA KMC
def KMCHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='kmc').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'kmc/KMCHomePage.html', context)
def KMCAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kmc/KMCAssistsDetail.html', context)
def KMCGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kmc/KMCGoalsDetail.html', context)
def KMCYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kmc/KMCYellowDetail.html', context)
def KMCRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kmc/KMCRedDetail.html', context)

def KMCSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kmc/KMCSummaryDetail.html', context)

class add_kmc_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('KMCHomePage')
    success_message = "Player Added Successfully"

class update_kmc_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('KMCHomePage')
    success_message = "Player Updated Successfully" 
def delete_kmc_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('KMCHomePage')

#VIEWS KWA AJILI YA MBEYA CITY
def MbeyaCityHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='mbeyacity').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'mbeyacity/MbeyaCityHomePage.html', context)

def MbeyaCityAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mbeyacity/MbeyaCityAssistsDetail.html', context)
def MbeyaCityGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mbeyacity/MbeyaCityGoalsDetail.html', context)
def MbeyaCityYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mbeyacity/MbeyaCityYellowDetail.html', context)
def MbeyaCityRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mbeyacity/MbeyaCityRedDetail.html', context)

def MbeyaCitySummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'mbeyacity/MbeyaCitySummaryDetail.html', context)

class add_mbeyacity_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('MbeyaCityHomePage')
    success_message = "Player Added Successfully"

class update_mbeyacity_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('MbeyaCityHomePage')
    success_message = "Player Updated Successfully" 
def delete_mbeyacity_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('MbeyaCityHomePage')

#VIEWS KWA AJILI YA COASTAL UNION
def CoastalUnionHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='coastalunion').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'coastalunion/CoastalUnionHomePage.html', context)

def CoastalUnionAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'coastalunion/CoastalUnionAssistsDetail.html', context)
def CoastalUnionGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'coastalunion/CoastalUnionGoalsDetail.html', context)
def CoastalUnionYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'coastalunion/CoastalUnionYellowDetail.html', context)
def CoastalUnionRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'coastalunion/CoastalUnionRedDetail.html', context)

def CoastalUnionSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'coastalunion/CoastalUnionSummaryDetail.html', context)

class add_coastalunion_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('CoastalUnionHomePage')
    success_message = "Player Added Successfully"

class update_coastalunion_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('CoastalUnionHomePage')
    success_message = "Player Updated Successfully" 
def delete_coastalunion_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('CoastalUnionHomePage')

#VIEWS KWA AJILI YA PRISON
def PrisonHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='prison').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'prison/PrisonHomePage.html', context)

def PrisonAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'prison/PrisonAssistsDetail.html', context)
def PrisonGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'prison/PrisonGoalsDetail.html', context)
def PrisonYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'prison/PrisonYellowDetail.html', context)
def PrisonRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'prison/PrisonRedDetail.html', context)

def PrisonSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'prison/PrisonSummaryDetail.html', context)

class add_prison_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('PrisonHomePage')
    success_message = "Player Added Successfully"

class update_prison_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('PrisonHomePage')
    success_message = "Player Updated Successfully" 
def delete_prison_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('PrisonHomePage')
#VIEWS KWA AJILI YA POLICE TZ
def PoliceTzHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='policetz').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'policetz/PoliceTzHomePage.html', context)

def PoliceTzAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'policetz/PoliceTzAssistsDetail.html', context)
def PoliceTzGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'policetz/PoliceTzGoalsDetail.html', context)
def PoliceTzYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'policetz/PoliceTzYellowDetail.html', context)
def PoliceTzRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'policetz/PoliceTzRedDetail.html', context)

def PoliceTzSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'policetz/PoliceTzSummaryDetail.html', context)

class add_policetz_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('PoliceTzHomePage')
    success_message = "Player Added Successfully"

class update_policetz_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('PoliceTzHomePage')
    success_message = "Player Updated Successfully" 
def delete_policetz_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('PoliceTzHomePage')
#VIEWS KWA AJILI YA GEITA GOLD
def GeitaGoldHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='geitagold').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'geitagold/GeitaGoldHomePage.html', context)

def GeitaGoldAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'geitagold/GeitaGoldAssistsDetail.html', context)
def GeitaGoldGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'geitagold/GeitaGoldGoalsDetail.html', context)
def GeitaGoldYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'geitagold/GeitaGoldYellowDetail.html', context)
def GeitaGoldRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'geitagold/GeitaGoldRedDetail.html', context)

def GeitaGoldSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'geitagold/GeitaGoldSummaryDetail.html', context)

class add_geitagold_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('GeitaGoldHomePage')
    success_message = "Player Added Successfully"

class update_geitagold_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('GeitaGoldHomePage')
    success_message = "Player Updated Successfully" 
def delete_geitagold_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('GeitaGoldHomePage')
#VIEWS KWA AJILI YA BIASHARA
def BiasharaHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='biashara').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'biashara/BiasharaHomePage.html', context)

def BiasharaAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'biashara/BiasharaAssistsDetail.html', context)
def BiasharaGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'biashara/BiasharaGoalsDetail.html', context)
def BiasharaYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'biashara/BiasharaYellowDetail.html', context)
def BiasharaRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'biashara/BiasharaRedDetail.html', context)

def BiasharaSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'biashara/BiasharaSummaryDetail.html', context)

class add_biashara_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('BiasharaHomePage')
    success_message = "Player Added Successfully"

class update_biashara_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('BiasharaHomePage')
    success_message = "Player Updated Successfully" 
def delete_biashara_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('BiasharaHomePage')
#VIEWS KWA AJILI YA DODOMAJIJI
def DodomaJijiHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='dodomajiji').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'dodomajiji/DodomaJijiHomePage.html', context)

def DodomaJijiAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'dodomajiji/DodomaJijiAssistsDetail.html', context)
def DodomaJijiGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'dodomajiji/DodomaJijiGoalsDetail.html', context)
def DodomaJijiYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'dodomajiji/DodomaJijiYellowDetail.html', context)
def DodomaJijiRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'dodomajiji/DodomaJijiRedDetail.html', context)

def DodomaJijiSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'dodomajiji/DodomaJijiSummaryDetail.html', context)

class add_dodomajiji_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('DodomaJijiHomePage')
    success_message = "Player Added Successfully"

class update_dodomajiji_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('DodomaJijiHomePage')
    success_message = "Player Updated Successfully" 
def delete_dodomajiji_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('DodomaJijiHomePage')
#VIEWS KWA AJILI YA KAGERA
def KageraHomePage(request):
	form = TeamForm(request.POST or None)
	players = TeamInformations.objects.filter(team_name='kagera').order_by('id')
	#searching button codes
	if request.method == 'POST':
		players = TeamInformations.objects.filter( prayer_name__icontains=form['prayer_name'].value())
	context = {
		"players":players,
		"form":form

	}


	return render(request, 'kagera/KageraHomePage.html', context)
def KageraAssistsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kagera/KageraAssistsDetail.html', context)
def KageraGoalsDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kagera/KageraGoalsDetail.html', context)
def KageraYellowDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kagera/KageraYellowDetail.html', context)
def KageraRedDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kagera/KageraRedDetail.html', context)

def KageraSummaryDetail(request, pk):
	players = TeamInformations.objects.get(id=pk)
	context = {
		"players":players

	}


	return render(request, 'kagera/KageraSummaryDetail.html', context)

class add_kagera_player(SuccessMessageMixin, CreateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('KageraHomePage')
    success_message = "Player Added Successfully"

class update_kagera_player(SuccessMessageMixin, UpdateView):
    model = TeamInformations
    template_name = 'DimosoApp/add_team_player.html'
    form_class = TeamForm
    success_url = reverse_lazy('KageraHomePage')
    success_message = "Player Updated Successfully" 
def delete_kagera_player(request, pk):
    player = get_object_or_404(TeamInformations, id=pk)
    player.delete()
    messages.success(request, "player deleted Successfully")
    return redirect('KageraHomePage')

def search_prayer(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=TeamInformations.objects.filter(Q(prayer_name__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'DimosoApp/search_prayer.html',context)

def search_player_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(prayer_name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    players = TeamInformations.objects.filter(search)
    mylist= []
    mylist += [x.prayer_name for x in players]
    return JsonResponse(mylist, safe=False)
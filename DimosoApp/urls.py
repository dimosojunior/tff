from django.urls import path
from .import views



urlpatterns = [

   
    path('', views.home, name="home"),
    
    path('base/', views.base, name="base"),
    path('search_prayer/', views.search_prayer, name="search_prayer"),
    path('readmore/', views.readmore, name="readmore"),
    path('user_login/', views.user_login, name="user_login"),
    path('sampo/', views.sampo, name="sampo"),
    path('SimbaHomePage/', views.SimbaHomePage, name="SimbaHomePage"),
    path('SimbaAssistsDetail/<int:pk>/', views.SimbaAssistsDetail, name="SimbaAssistsDetail"),
    path('SimbaGoalsDetail/<int:pk>/', views.SimbaGoalsDetail, name="SimbaGoalsDetail"),
    path('SimbaYellowDetail/<int:pk>/', views.SimbaYellowDetail, name="SimbaYellowDetail"),
    path('SimbaRedDetail/<int:pk>/', views.SimbaRedDetail, name="SimbaRedDetail"),
    path('SimbaSummaryDetail/<int:pk>/', views.SimbaSummaryDetail, name="SimbaSummaryDetail"),
    
    path('add_simba_player/', views.add_simba_player.as_view(), name="add_simba_player"),

    path('update_simba_player/<int:pk>/', views.update_simba_player.as_view(), name="update_simba_player"),
    path('delete_simba_player/<int:pk>/', views.delete_simba_player, name="delete_simba_player"),
   	path('search_player_autocomplete', views.search_player_autocomplete, name="search_player_autocomplete"),
  
  	path('msimamo_wa_league/', views.msimamo_wa_league, name="msimamo_wa_league"),
   	path('ratiba_ya_league/', views.ratiba_ya_league, name="ratiba_ya_league"),
   	path('matokeo_ya_league_leo/', views.matokeo_ya_league_leo, name="matokeo_ya_league_leo"),
    path('matokeo_ya_league_jana/', views.matokeo_ya_league_jana, name="matokeo_ya_league_jana"),
    path('matokeo_ya_league_juzi/', views.matokeo_ya_league_juzi, name="matokeo_ya_league_juzi"),
   

   #URLS ZA YANGA
   	path('YangaHomePage/', views.YangaHomePage, name="YangaHomePage"),
   	path('YangaAssistsDetail/<int:pk>/', views.YangaAssistsDetail, name="YangaAssistsDetail"),
    path('YangaGoalsDetail/<int:pk>/', views.YangaGoalsDetail, name="YangaGoalsDetail"),
    path('YangaYellowDetail/<int:pk>/', views.YangaYellowDetail, name="YangaYellowDetail"),
    path('YangaRedDetail/<int:pk>/', views.YangaRedDetail, name="YangaRedDetail"),
    path('YangaSummaryDetail/<int:pk>/', views.YangaSummaryDetail, name="YangaSummaryDetail"),
    path('add_yanga_player/', views.add_yanga_player.as_view(), name="add_yanga_player"),

    path('update_yanga_player/<int:pk>/', views.update_yanga_player.as_view(), name="update_yanga_player"),
    path('delete_yanga_player/<int:pk>/', views.delete_yanga_player, name="delete_yanga_player"),

 	#URLS ZA AZAM
   	path('AzamHomePage/', views.AzamHomePage, name="AzamHomePage"),
   	path('AzamAssistsDetail/<int:pk>/', views.AzamAssistsDetail, name="AzamAssistsDetail"),
    path('AzamGoalsDetail/<int:pk>/', views.AzamGoalsDetail, name="AzamGoalsDetail"),
    path('AzamYellowDetail/<int:pk>/', views.AzamYellowDetail, name="AzamYellowDetail"),
    path('AzamRedDetail/<int:pk>/', views.AzamRedDetail, name="AzamRedDetail"),
    path('AzamSummaryDetail/<int:pk>/', views.AzamSummaryDetail, name="AzamSummaryDetail"),
    path('add_azam_player/', views.add_azam_player.as_view(), name="add_azam_player"),

    path('update_azam_player/<int:pk>/', views.update_azam_player.as_view(), name="update_azam_player"),
    path('delete_azam_player/<int:pk>/', views.delete_azam_player, name="delete_azam_player"),

  	#URLS ZA NAMUNGO
   	path('NamungoHomePage/', views.NamungoHomePage, name="NamungoHomePage"),
   	path('NamungoAssistsDetail/<int:pk>/', views.NamungoAssistsDetail, name="NamungoAssistsDetail"),
    path('NamungoGoalsDetail/<int:pk>/', views.NamungoGoalsDetail, name="NamungoGoalsDetail"),
    path('NamungoYellowDetail/<int:pk>/', views.NamungoYellowDetail, name="NamungoYellowDetail"),
    path('NamungoRedDetail/<int:pk>/', views.NamungoRedDetail, name="NamungoRedDetail"),
    path('NamungoSummaryDetail/<int:pk>/', views.NamungoSummaryDetail, name="NamungoSummaryDetail"),
    path('add_namungo_player/', views.add_namungo_player.as_view(), name="add_namungo_player"),

    path('update_namungo_player/<int:pk>/', views.update_namungo_player.as_view(), name="update_namungo_player"),
    path('delete_namungo_player/<int:pk>/', views.delete_namungo_player, name="delete_namungo_player"),  
    
    #URLS ZA MTIBWA
   	path('MtibwaHomePage/', views.MtibwaHomePage, name="MtibwaHomePage"),
   	path('MtibwaAssistsDetail/<int:pk>/', views.MtibwaAssistsDetail, name="MtibwaAssistsDetail"),
    path('MtibwaGoalsDetail/<int:pk>/', views.MtibwaGoalsDetail, name="MtibwaGoalsDetail"),
    path('MtibwaYellowDetail/<int:pk>/', views.MtibwaYellowDetail, name="MtibwaYellowDetail"),
    path('MtibwaRedDetail/<int:pk>/', views.MtibwaRedDetail, name="MtibwaRedDetail"),
    path('MtibwaSummaryDetail/<int:pk>/', views.MtibwaSummaryDetail, name="MtibwaSummaryDetail"),
    path('add_mtibwa_player/', views.add_mtibwa_player.as_view(), name="add_mtibwa_player"),

    path('update_mtibwa_player/<int:pk>/', views.update_mtibwa_player.as_view(), name="update_mtibwa_player"),
    path('delete_mtibwa_player/<int:pk>/', views.delete_mtibwa_player, name="delete_mtibwa_player"),
 
    
 	#URLS ZA KMC
   	path('KMCHomePage/', views.KMCHomePage, name="KMCHomePage"),
   	path('KMCAssistsDetail/<int:pk>/', views.KMCAssistsDetail, name="KMCAssistsDetail"),
    path('KMCGoalsDetail/<int:pk>/', views.KMCGoalsDetail, name="KMCGoalsDetail"),
    path('KMCYellowDetail/<int:pk>/', views.KMCYellowDetail, name="KMCYellowDetail"),
    path('KMCRedDetail/<int:pk>/', views.KMCRedDetail, name="KMCRedDetail"),
    path('KMCSummaryDetail/<int:pk>/', views.KMCSummaryDetail, name="KMCSummaryDetail"),
    path('add_kmc_player/', views.add_kmc_player.as_view(), name="add_kmc_player"),

    path('update_kmc_player/<int:pk>/', views.update_kmc_player.as_view(), name="update_kmc_player"),
    path('delete_kmc_player/<int:pk>/', views.delete_kmc_player, name="delete_kmc_player"),

    #URLS ZA MBEYA CITY
   	path('MbeyaCityHomePage/', views.MbeyaCityHomePage, name="MbeyaCityHomePage"),
   	path('MbeyaCityAssistsDetail/<int:pk>/', views.MbeyaCityAssistsDetail, name="MbeyaCityAssistsDetail"),
    path('MbeyaCityGoalsDetail/<int:pk>/', views.MbeyaCityGoalsDetail, name="MbeyaCityGoalsDetail"),
    path('MbeyaCityYellowDetail/<int:pk>/', views.MbeyaCityYellowDetail, name="MbeyaCityYellowDetail"),
    path('MbeyaCityRedDetail/<int:pk>/', views.MbeyaCityRedDetail, name="MbeyaCityRedDetail"),
    path('MbeyaCitySummaryDetail/<int:pk>/', views.MbeyaCitySummaryDetail, name="MbeyaCitySummaryDetail"),
    path('add_mbeyacity_player/', views.add_mbeyacity_player.as_view(), name="add_mbeyacity_player"),

    path('update_mbeyacity_player/<int:pk>/', views.update_mbeyacity_player.as_view(), name="update_mbeyacity_player"),
    path('delete_mbeyacity_player/<int:pk>/', views.delete_mbeyacity_player, name="delete_mbeyacity_player"),


    #URLS ZA COASTAL UNION
   	path('CoastalUnionHomePage/', views.CoastalUnionHomePage, name="CoastalUnionHomePage"),
   	path('CoastalUnionAssistsDetail/<int:pk>/', views.CoastalUnionAssistsDetail, name="CoastalUnionAssistsDetail"),
    path('CoastalUnionGoalsDetail/<int:pk>/', views.CoastalUnionGoalsDetail, name="CoastalUnionGoalsDetail"),
    path('CoastalUnionYellowDetail/<int:pk>/', views.CoastalUnionYellowDetail, name="CoastalUnionYellowDetail"),
    path('CoastalUnionRedDetail/<int:pk>/', views.CoastalUnionRedDetail, name="CoastalUnionRedDetail"),
    path('CoastalUnionSummaryDetail/<int:pk>/', views.CoastalUnionSummaryDetail, name="CoastalUnionSummaryDetail"),
    path('add_coastalunion_player/', views.add_coastalunion_player.as_view(), name="add_coastalunion_player"),

    path('update_coastalunion_player/<int:pk>/', views.update_coastalunion_player.as_view(), name="update_coastalunion_player"),
    path('delete_coastalunion_player/<int:pk>/', views.delete_coastalunion_player, name="delete_coastalunion_player"),

    #URLS ZA PRISON
   	path('PrisonHomePage/', views.PrisonHomePage, name="PrisonHomePage"),
   	path('PrisonAssistsDetail/<int:pk>/', views.PrisonAssistsDetail, name="PrisonAssistsDetail"),
    path('PrisonGoalsDetail/<int:pk>/', views.PrisonGoalsDetail, name="PrisonGoalsDetail"),
    path('PrisonYellowDetail/<int:pk>/', views.PrisonYellowDetail, name="PrisonYellowDetail"),
    path('PrisonRedDetail/<int:pk>/', views.PrisonRedDetail, name="PrisonRedDetail"),
    path('PrisonSummaryDetail/<int:pk>/', views.PrisonSummaryDetail, name="PrisonSummaryDetail"),
    path('add_prison_player/', views.add_prison_player.as_view(), name="add_prison_player"),

    path('update_prison_player/<int:pk>/', views.update_prison_player.as_view(), name="update_prison_player"),
    path('delete_prison_player/<int:pk>/', views.delete_prison_player, name="delete_prison_player"),

    #URLS ZA AZAM
   	path('PoliceTzHomePage/', views.PoliceTzHomePage, name="PoliceTzHomePage"),
   	path('PoliceTzAssistsDetail/<int:pk>/', views.PoliceTzAssistsDetail, name="PoliceTzAssistsDetail"),
    path('PoliceTzGoalsDetail/<int:pk>/', views.PoliceTzGoalsDetail, name="PoliceTzGoalsDetail"),
    path('PoliceTzYellowDetail/<int:pk>/', views.PoliceTzYellowDetail, name="PoliceTzYellowDetail"),
    path('PoliceTzRedDetail/<int:pk>/', views.PoliceTzRedDetail, name="PoliceTzRedDetail"),
    path('PoliceTzSummaryDetail/<int:pk>/', views.PoliceTzSummaryDetail, name="PoliceTzSummaryDetail"),
    path('add_policetz_player/', views.add_policetz_player.as_view(), name="add_policetz_player"),

    path('update_policetz_player/<int:pk>/', views.update_policetz_player.as_view(), name="update_policetz_player"),
    path('delete_policetz_player/<int:pk>/', views.delete_policetz_player, name="delete_policetz_player"),

    #URLS ZA AZAM
   	path('GeitaGoldHomePage/', views.GeitaGoldHomePage, name="GeitaGoldHomePage"),
   	path('GeitaGoldAssistsDetail/<int:pk>/', views.GeitaGoldAssistsDetail, name="GeitaGoldAssistsDetail"),
    path('GeitaGoldGoalsDetail/<int:pk>/', views.GeitaGoldGoalsDetail, name="GeitaGoldGoalsDetail"),
    path('GeitaGoldYellowDetail/<int:pk>/', views.GeitaGoldYellowDetail, name="GeitaGoldYellowDetail"),
    path('GeitaGoldRedDetail/<int:pk>/', views.GeitaGoldRedDetail, name="GeitaGoldRedDetail"),
    path('GeitaGoldSummaryDetail/<int:pk>/', views.GeitaGoldSummaryDetail, name="GeitaGoldSummaryDetail"),
    path('add_geitagold_player/', views.add_geitagold_player.as_view(), name="add_geitagold_player"),

    path('update_geitagold_player/<int:pk>/', views.update_geitagold_player.as_view(), name="update_geitagold_player"),
    path('delete_geitagold_player/<int:pk>/', views.delete_geitagold_player, name="delete_geitagold_player"),

    #URLS ZA AZAM
   	path('BiasharaHomePage/', views.BiasharaHomePage, name="BiasharaHomePage"),
   	path('BiasharaAssistsDetail/<int:pk>/', views.BiasharaAssistsDetail, name="BiasharaAssistsDetail"),
    path('BiasharaGoalsDetail/<int:pk>/', views.BiasharaGoalsDetail, name="BiasharaGoalsDetail"),
    path('BiasharaYellowDetail/<int:pk>/', views.BiasharaYellowDetail, name="BiasharaYellowDetail"),
    path('BiasharaRedDetail/<int:pk>/', views.BiasharaRedDetail, name="BiasharaRedDetail"),
    path('BiasharaSummaryDetail/<int:pk>/', views.BiasharaSummaryDetail, name="BiasharaSummaryDetail"),
    path('add_biashara_player/', views.add_biashara_player.as_view(), name="add_biashara_player"),

    path('update_biashara_player/<int:pk>/', views.update_biashara_player.as_view(), name="update_biashara_player"),
    path('delete_biashara_player/<int:pk>/', views.delete_biashara_player, name="delete_biashara_player"),

    #URLS ZA DODOMA JIJI
   	path('DodomaJijiHomePage/', views.DodomaJijiHomePage, name="DodomaJijiHomePage"),
   	path('DodomaJijiAssistsDetail/<int:pk>/', views.DodomaJijiAssistsDetail, name="DodomaJijiAssistsDetail"),
    path('DodomaJijiGoalsDetail/<int:pk>/', views.DodomaJijiGoalsDetail, name="DodomaJijiGoalsDetail"),
    path('DodomaJijiYellowDetail/<int:pk>/', views.DodomaJijiYellowDetail, name="DodomaJijiYellowDetail"),
    path('DodomaJijiRedDetail/<int:pk>/', views.DodomaJijiRedDetail, name="DodomaJijiRedDetail"),
    path('DodomaJijiSummaryDetail/<int:pk>/', views.DodomaJijiSummaryDetail, name="DodomaJijiSummaryDetail"),
    path('add_dodomajiji_player/', views.add_dodomajiji_player.as_view(), name="add_dodomajiji_player"),

    path('update_dodomajiji_player/<int:pk>/', views.update_dodomajiji_player.as_view(), name="update_dodomajiji_player"),
    path('delete_dodomajiji_player/<int:pk>/', views.delete_dodomajiji_player, name="delete_dodomajiji_player"),

    #URLS ZA KAGERA
   	path('KageraHomePage/', views.KageraHomePage, name="KageraHomePage"),
   	path('KageraAssistsDetail/<int:pk>/', views.KageraAssistsDetail, name="KageraAssistsDetail"),
    path('KageraGoalsDetail/<int:pk>/', views.KageraGoalsDetail, name="KageraGoalsDetail"),
    path('KageraYellowDetail/<int:pk>/', views.KageraYellowDetail, name="KageraYellowDetail"),
    path('KageraRedDetail/<int:pk>/', views.KageraRedDetail, name="KageraRedDetail"),
    path('KageraSummaryDetail/<int:pk>/', views.KageraSummaryDetail, name="KageraSummaryDetail"),
    path('add_kagera_player/', views.add_kagera_player.as_view(), name="add_kagera_player"),

    path('update_kagera_player/<int:pk>/', views.update_kagera_player.as_view(), name="update_kagera_player"),
    path('delete_kagera_player/<int:pk>/', views.delete_kagera_player, name="delete_kagera_player"),



    path('add_matokeo_ya_mechi/', views.add_matokeo_ya_mechi.as_view(), name="add_matokeo_ya_mechi"),

    path('update_matokeo_ya_mechi/<int:pk>/', views.update_matokeo_ya_mechi.as_view(), name="update_matokeo_ya_mechi"),
    path('delete_matokeo_ya_mechi/<int:pk>/', views.delete_matokeo_ya_mechi, name="delete_matokeo_ya_mechi"),
  

#ratiba
    path('add_ratiba_ya_mechi/', views.add_ratiba_ya_mechi.as_view(), name="add_ratiba_ya_mechi"),

    path('update_ratiba_ya_mechi/<int:pk>/', views.update_ratiba_ya_mechi.as_view(), name="update_ratiba_ya_mechi"),
    path('delete_ratiba_ya_mechi/<int:pk>/', views.delete_ratiba_ya_mechi, name="delete_ratiba_ya_mechi"),
  
#msimamo
    path('add_msimamo_wa_league/', views.add_msimamo_wa_league.as_view(), name="add_msimamo_wa_league"),

    path('update_msimamo_wa_league/<int:pk>/', views.update_msimamo_wa_league.as_view(), name="update_msimamo_wa_league"),
    path('delete_msimamo_wa_league/<int:pk>/', views.delete_msimamo_wa_league, name="delete_msimamo_wa_league"),
  







]
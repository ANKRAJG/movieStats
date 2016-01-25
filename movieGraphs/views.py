import numpy as np

from matplotlib.font_manager import FontProperties
from matplotlib import pyplot as plt
from django.shortcuts import render
from django.views import generic
from .forms import FilmForm

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from django.core import serializers    
from django.http import HttpResponse

#from movieStats.settings import MEDIA_ROOT, MEDIA_URL
from movieStats.settings import MEDIA_URL
from movieGraphs.models import Hollywood,Profession, Artist, Xaxis, Yaxis, MovieImage, ArtistImage

import sqlite3
import os
import PIL
import PIL.Image
import io 



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




def film_graph(request):
    
    if request.method == 'POST':
        form = FilmForm(request.POST)
        
        if form.is_valid():

            profession = str(form.cleaned_data['profession'])
            artist = str(form.cleaned_data['artist'])
            xaxis = str(form.cleaned_data['x_axis'])
            yaxis = str(form.cleaned_data['y_axis'])
            
            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()
            c.execute("SELECT * FROM movieGraphs_hollywood WHERE " + profession + " LIKE '%" + artist + "%'")
            result = c.fetchall()
            
            
            if not result:
                form = FilmForm()
                alert = "Artist Name might have spelled wrong OR there is a mismatch of Profession and Artist Name OR Artist does not exist."
                return render(request, 'film.html', {'form': form, 'alert': alert})
            
            else: 
                xAxis = [idx for idx,r in enumerate(result)]           #getting count in a loop through idx
                labels = [r[1] for r in result]
                actrs = [r[2] for r in result]
                directrs = [r[3] for r in result]
                relez = [r[4] for r in result]
                ratin = [r[5] for r in result]
                budzt = [r[6] for r in result]
                boxoff = [r[7] for r in result]
                
                #if-else condition
                if '' + yaxis + '' == 'Rating':
                    yAxis = [r[5] for r in result]
                    
                elif '' + yaxis + '' == 'Release':
                    yAxis = [r[4] for r in result]
                    
                elif '' + yaxis + '' == 'Budget':
                    yAxis = [r[6] for r in result]
                    
                else:
                    yAxis =[r[7] for r in result]
            
                max_y = max(yAxis)                          #Getting maximum value of Y-axis       
                max_yIndex = yAxis.index(max_y)             #Getting index of maximum value
            
                muvie = labels[max_yIndex]
                actor = actrs[max_yIndex]
                director = directrs[max_yIndex]
                ry = relez[max_yIndex]
                rat = ratin[max_yIndex]
                
                ratings = float(rat/2)                  #Dividing rating by 2
                
                bujet = budzt[max_yIndex]
                boxOffice = boxoff[max_yIndex]
                
            
                movie_image = MovieImage.objects.get(movie_name = '' + muvie + '')
                mi = movie_image.movie_img
            
            
            #try-catch block
                try:
                    artist_image = ArtistImage.objects.get(artst_name__startswith = '' + artist + '')
                except (MultipleObjectsReturned, ObjectDoesNotExist):                                           #Handling Errors 
                    form = FilmForm()
                    alert = "Please enter Full Artist Name!! There might be other Artists with the same name."
                    return render(request, 'film.html', {'form': form, 'alert': alert})
                
                ai = artist_image.artist_img
                an = artist_image.artst_name
                ap = artist_image.artist_prof
                ag = artist_image.artist_gender
            
            
            
                fig = plt.figure()
                fig.set_size_inches(12, 9)
                rect = fig.patch
                rect.set_facecolor('#eeeeee')

                ax1 = fig.add_subplot(1,1,1, axisbg='#ffff96')
                ax1.bar(xAxis, yAxis, color='palevioletred', align='center')
                for i,j in zip(xAxis,yAxis):
                    ax1.annotate(j,xy=(i,j), ha='center', va = 'bottom')

                ax1.set_xticks(xAxis)

                ax1.grid(True)

                count = 0
                for xa in xAxis:
                    count+=1

                ax1.set_xlabel('<-------------- Movies -------------->')
                ax1.set_xlim(-1, count)

                #if-else
                if '' + yaxis + '' == 'Rating':
                    ax1.set_ylabel('Rating out of 10 ----->')
                    ax1.set_ylim(0.0, 11)
    
                elif '' + yaxis + '' == 'Budget':
                    ax1.set_ylabel('' + yaxis + ' (in $million) ----->')
                    ax1.set_ylim(0, 260)

                elif '' + yaxis + '' == 'Box_Office':
                    ax1.set_ylabel('' + yaxis + ' (in $million) ----->')
                    ax1.set_ylim(0, 3000)
    
                else:
                    ax1.set_ylabel('Releasing-Year')
                    ax1.set_ylim(1920, 2030)
    
        
                ax1.set_title("" + an + "'s  " +xaxis + "s-" + yaxis + " Chart")
    
                fig.savefig(BASE_DIR + '/movieGraphs/static/img/plot.png', dpi = 60, facecolor=fig.get_facecolor())
                plt.close(fig)
                
            
                list = zip(xAxis, labels)
                context = {'list': list, 'an': an, 'yaxis': yaxis, 'mi': mi, 'ai': ai, 'ap': ap, 'ag': ag, 'muvie': muvie, 'actor': actor, \
                           'director': director, 'ry': ry, 'rat': rat, 'ratings': ratings, 'bujet': bujet, 'boxOffice': boxOffice}
            
                return render(request, 'graph.html', context)        
    
    
    else:
        form = FilmForm()

    return render(request, 'film.html', {'form': form})
    
    

    
    
            

def sample_graph(request):
    
    profession = 'Actor'
    artist = 'Matthew McConaughey'
    xaxis = 'Movie'
    yaxis = 'Box_Office'
            
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT id," + xaxis + "," + yaxis + " FROM movieGraphs_hollywood WHERE " + profession + " LIKE '%" + artist + "%'")

    result = c.fetchall()
    
    xAxis = [idx for idx,r in enumerate(result)]           #getting count in a loop through idx
    labels = [r[1] for r in result]
    yAxis = [(r[2]) for r in result]
            
    fig = plt.figure()
    rect = fig.patch
    rect.set_facecolor('#bbbbbb')

    ax1 = fig.add_subplot(1,1,1, axisbg='w')
    ax1.bar(xAxis, yAxis, color='darkseagreen', align='center')
    for i,j in zip(xAxis,yAxis):
        ax1.annotate(j,xy=(i,j), ha='center', va = 'bottom')

    ax1.set_xticks(xAxis)
    ax1.set_xticklabels(labels)

    ax1.grid(True)

    count = 0
    for xa in xAxis:
        count+=1

    ax1.set_xlabel('<-------------- Movies -------------->')
    ax1.set_xlim(-1, count)

    #if-else
    if '' + yaxis + '' == 'Rating':
        ax1.set_ylabel('Rating out of 5')
        ax1.set_ylim(0.0, 5.5)
    
    elif '' + yaxis + '' == 'Budget':
        ax1.set_ylabel('' + yaxis + ' (in $million) ---->')
        ax1.set_ylim(0, 260)

    elif '' + yaxis + '' == 'Box_Office':
        ax1.set_ylabel('' + yaxis + ' (in $million) ---->')
        ax1.set_ylim(0, 1000)
    
    else:
        ax1.set_ylabel('Releasing-Year')
        ax1.set_ylim(1920, 2030)
    
        
    ax1.set_title("" + artist + "'s  " +xaxis + "s-" + yaxis + " Chart")
    
    
    buffer = io.BytesIO()
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    plt.close()
    
    return HttpResponse(buffer.getvalue(), content_type = "image/png")





def detail(request):
    return render(request, 'sample_graph.html', None)




def film(request):
    form    = FilmForm()
    context = {'form' : form}
    
    return render(request, 'film.html', context)





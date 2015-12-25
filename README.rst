=====
MovieGraphs
=====

Do not get confused with movieStats and MovieGraphs. Here movieStats is a full Project and our main point of focus is movieGraphs App.

MovieGraphs is a Web application to see movie-related statistics in a graphical way.
You put your queries related to movies and the data will be shown to you in a Graphical form. This app is built using Django, Python, Sqlite3, Matplotlib, JQuery, Javascript, Ajax, HTML5, CSS3.

There are four fields in the main home Film page to fill, Profession, Artist Name, X-axis and Y-axis. You have to select 
options from the dropdown apart from Artist Name where you have to type the appropriate artist name.
After submitting button, the data will be shown to you in a graphical form with X-axis and Y-axis
values given by you.
Right now the data in the database of this app is small, but to make this app do wonders there must be large dataset in it.
     

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "movieGraphs" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        
        'movieGraphs',
    ]

2. Include the film URLconf in your project urls.py like this::

    url(r'^film/', include('film.urls')),

3. Run `python manage.py migrate` to create the movieGraphs models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a tables for movieGraphs (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/film/ to get started.


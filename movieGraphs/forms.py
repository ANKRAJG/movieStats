from django import forms
from movieGraphs import models



class FilmForm(forms.ModelForm):
    profession = forms.ModelChoiceField(label = 'Profession', empty_label='Select Profession for Artist', queryset=models.Profession.objects.all())
    artist = forms.CharField(max_length = 150, label = 'Artist Name', help_text = 'e.g. Leonardo Dicaprio')
    x_axis = forms.ModelChoiceField(label = 'X-axis', empty_label='Select Value for X-axis', queryset=models.Xaxis.objects.all())
    y_axis = forms.ModelChoiceField(label = 'Y-axis', empty_label='Select Value for Y-axis', queryset=models.Yaxis.objects.all())
    
    class Meta:
        model = models.Profession

        fields = ('profession', 'artist')
from django import forms

class GazouForm(forms.Form):
    name = forms.CharField(label='ユーザーID', \
        widget=forms.TextInput(attrs={'class':'form-control'}),initial='rikichannel1203',max_length=16)#'pelicaNCancAn')
    word = forms.CharField(label='界隈名', \
        widget=forms.TextInput(attrs={'class':'form-control'}),initial='宇宙',max_length=160)#'ポケモン')
    fl = forms.IntegerField(label='フォロワー数', \
        widget=forms.NumberInput(attrs={'class':'form-control'}),initial=1000,max_value=1000000000)

from django import forms


class PostForm(forms.Form):
	titulo = forms.CharField(label='titulo', widget=forms.Textarea(),required=False, max_length=150)
	descricao = forms.CharField(label='titulo', widget=forms.Textarea(),required=False ,max_length=800)
	anexo = forms.FileField(label="anexo", required=True)


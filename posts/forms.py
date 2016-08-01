from django import forms

from .models import Hidrometros

import datetime

from .apps import SelectTimeWidget


class HidrometrosForm(forms.ModelForm):

	LOCAL_CHOICES = (
    ('Geral', 'Geral'),
    ('Corte_H1', 'Corte H1'),
    ('Corte_H2', 'Corte H2'),
    ('Bloco_ADM', 'Bloco ADM.'),
    ('Bloco_Varas', 'Bloco Varas'),
    ('Jardim', 'Jardim'),
)

	class Meta:
		model = Hidrometros
		fields = [
			"local",
			"medicao_inicial",
			"medicao_final",
			"horario_ligamento",
			"horario_desligamento",
			"data",
		]

	data = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today())

	#horario_ligamento = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
	horario_ligamento = forms.TimeField(widget=SelectTimeWidget())
	horario_desligamento = forms.TimeField(widget=SelectTimeWidget())

	local = forms.ChoiceField(label="Local", choices=(LOCAL_CHOICES),
                                       widget=forms.Select(attrs={'class':'selector'}))
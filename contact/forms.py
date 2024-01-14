from django import forms
from django.core.exceptions import ValidationError 
from . import models

class ContactForm(forms.ModelForm):
    # mudar campos do form declarado em models.py
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva aqui',       
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )    

    # Podemos criar novos campos no form
    # qualquer = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'classe-a classe-b',
    #             'placeholder': 'Escreva aqui',       
    #         }
    #     ),
    #     help_text='Texto de ajuda para seu usuário',
    # ) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # outra maneira de atualizar um cmapo já existente no form
        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',             
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        # outra maneira de atualizar um cmapo já existente no form
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',       
        #         }
        #     )
        # }

    def clean(self):
        #cleaned_data = self.cleaned_data
        #print(cleaned_data)

        self.add_error(
            #'first_name',
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            #'first_name',
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )


        return super().clean()

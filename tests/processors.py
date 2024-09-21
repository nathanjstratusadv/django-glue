from tests import forms


def get_complex_form_processor(form_data):
    if form_data.get('location') == 'NYC':
        return forms.NewYorkForm(data=form_data)

    if form_data.get('location') == 'CHI':
        return forms.ChicagoForm(data=form_data)


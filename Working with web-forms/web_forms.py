from requests_html import HTMLSession
from bs4 import BeautifulSoup

# сохраняем печеньки
session = HTMLSession()

def forms(url):
	request = session.get(url)
	#request.html.render() # если сайт использует динамическую подгрузку на js
	a = BeautifulSoup(request.html.html , "html.parser")
	form_1 = a.find_all('form')
	return form_1


def all_forms_from_the_page(form):
	ins= {}
	form_action = form.attrs.get('action').lower()
	form_method = form.attrs.get('method', 'get').lower()
	spisok_inputs = []
	
	s = form.find_all('input')
	for tag_i in s:
		type_i = tag_i.attrs.get("type", "text")
		name_i = tag_i.attrs.get('name')
		value_i = tag_i.attrs.get("value", "")
		spisok_inputs.append({'type:' : type_i , 'name' : name_i , 'value': value_i})
		print(type_i)
	ins['action'] = form_action
	ins['method'] = form_method
	ins['inputs'] = spisok_inputs
	return ins
	
url = 'https://wikipedia.org'

#fforms = forms(url)
#for i, form in enumerate(fforms, start=1):
#	f_det = all_forms_from_the_page(form)
#	print("="*50, f"form #{i}", "="*50)
#	print(f_det)
	
	
fforms = forms(url)
# iteratte over forms
for i, form in enumerate(fforms, start=1):
    form_details =all_forms_from_the_page(form)
    print("="*50, f"form #{i}", "="*50)
    print(form_details)


















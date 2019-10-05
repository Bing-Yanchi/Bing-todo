# import
import time,yaml,json
# language
language_choice = 'cn'
def lang():
	global language
	if language_choice == 'cn':
		file = open('language_cn.yml', encoding='UTF-8')
		language = yaml.load(file, Loader = yaml.FullLoader)
	else:
		file = open('language_en.yml')
		language = yaml.load(file, Loader = yaml.FullLoader)
lang()
# def
def create():
	# create todo
	add_name = input(language.get('msg#11'))
	if add_name != '':
		add_description = input(language.get('msg#12'))
		if add_description != '':
			add_mode = input(language.get('msg#13'))
			if add_mode == 'back' or add_mode == 'go' or add_mode == 'no':
				return add_name,add_description,add_mode
def data_add(name,description,mode):
	# add data
	with open('data.json','r',encoding='UTF-8') as f:
		# read
		data = {}
		data['name'] = name
		data['description'] = description
		data['mode'] = mode
		data['time'] = int(time.time())
		load_data = []
		load_data = json.load(f)
		load_data.append(data)
	with open('data.json','w',encoding='UTF-8') as file:
		# write
		json.dump(load_data,file,ensure_ascii=False)
# welcome
print(language.get('msg#0'))
print()
# get version
version = '1.0'
latest = '1.0'
# check update
print(language.get('Info') + " » " + language.get('msg#1'))
if latest == version:
	print(language.get('Info') + " » " + language.get('msg#2'))
elif latest == "":
	print(language.get('Error') + " » " + language.get('msg#3'))
else:
	print(language.get('Warn') + " » " + language.get('msg#4')+ " " + str(latest))
	print(language.get('Warn') + " » " + language.get('msg#5'))
print()
# main
while True:
	# input
	command = input(language.get('Input') + " » ")
	# run
	if command == 'help':
		# help
		help = language.get('help')[0]
		for a in help.keys():
			print(language.get('Help') + " » " + a + " -- " + help.get(a))
	elif command == 'exit':
		# exit
		print(language.get('msg#6'))
		break
	elif command == 'time':
		# time
		time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print(language.get('Time') + ' » '+ time)
	elif command == 'language' or command == 'lang':
		# language
		print(language.get('Info') + ' » '+ language.get('msg#7') + ':' + language.get('Language'))
		print(language.get('Info') + ' » '+ language.get('msg#8') + ' (en,cn):')
		language_choice = input(language.get('Input') + ' » ')
		if language_choice == 'en' or language_choice == 'cn':
			lang()
			print(language.get('msg#9') + ' » '+ language.get('Language'))
		else:
			print(language.get('Error') + " » " + language.get('Unknown') + ' ' + language.get('msg#7'))
	elif command == 'about':
		# about
		print(language.get('msg#10'))
	elif command == 'create':
		# create
		name,description,mode = create()
		data_add(name,description,mode)
		print(language.get('msg#14'))
	else:
		# unknown
		print(language.get('Error') + " » " + language.get('Unknown'))
	print()
with open('schema.sql') as f:
	with open('api/hydration_info.py', 'w') as o:
		line = f.readline()
		while line != '':
			pieces = line.split(' ')
			if pieces[0] == 'CREATE' and pieces[1] == 'TABLE':
				table_name = pieces[2][1:-1]
				fields = []
				while True:
					line = f.readline()
					pieces = line.strip().split(' ')
					if pieces[0][0] == '`':
						fields += [pieces[0].replace('`', '\'')]
					else:
						break
				o.write(table_name.upper() + '_SCHEMA = [\n')
				for field in fields:
					o.write('\t' + field + (',' if fields[-1] != field else '') + '\n')
				o.write(']\n')
			line = f.readline()
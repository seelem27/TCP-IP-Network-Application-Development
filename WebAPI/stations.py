import sqlite3
db = sqlite3.connect('stations.sqlite')

db.execute('DROP TABLE IF EXISTS stations')

db.execute('''CREATE TABLE stations(
    id integer PRIMARY KEY AUTOINCREMENT,
    code text UNIQUE NOT NULL,
    name text NOT NULL,
    type text NOT NULL    
)''')

cursor = db.cursor()

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK07','Surian','Elevated')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK08','Mutiara Damansara','Elevated')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK09','Bandar Utama','Elevated')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK10','TTDI','Elevated')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK12','Phileo Damansara','Elevated')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK13','Pusat Bandar Damansara','Elevated')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK14','Semantan','Elevated')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK15','Muzium Negara','Underground')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK16','Pasar Seni','Underground')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK17','Merdeka','Underground')
''')

cursor.execute('''
    INSERT INTO stations(code,name,type)
    VALUES('SBK18A','Bukit Bintang','Elevated')
''')

db.commit()
db.close()
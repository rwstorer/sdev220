import sqlalchemy as sa

engine = sa.create_engine('sqlite:///books.db')
conn = engine.connect()
sql = sa.text('SELECT title from book')
rows = conn.execute(sql)

for row in rows:
    print('title:', row[0])

conn.close()
engine.dispose()
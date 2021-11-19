from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:example@localhost:3306/mysql')

result = engine.execute("select 1, 'hello' from dual")

for row in result:
    print(row)

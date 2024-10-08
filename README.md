# clone project
```
atul@atul-Lenovo-G570:~$ git clone https://github.com/atulkrishnathakur/fasterp.git

```

# generate requirements.txt
```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 freeze > requirements.txt
```
# pip version

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 --version

# Or

(env) atul@atul-Lenovo-G570:~/fasterp$ pip --version

# you can see version is same.
# It means you can use pip3 or pip both command in virtual environment

```

# install fastapi

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip install "fastapi[standard]"

```

# run the server
The command uvicorn main:app refers to:

1. main: the file main.py (the Python "module").
2. app: the object created inside of main.py with the line app = FastAPI().
3. --reload: make the server restart after code changes. Only use for development.

```
(env) atul@atul-Lenovo-G570:~/fasterp$ uvicorn main:app --reload

```


# install sqlalchemy
```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install sqlalchemy

```

# install psycopg2-binary

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install psycopg2-binary

```

# install alembic

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install alembic

```

Below command will create an alembic directory with necessary configuration files.

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic init alembic

```

# alembic.ini file

You can see alembic.ini file outside of alembic directory. The alembic.ini file path is fasterp/alembic.ini. 

```
sqlalchemy.url = sqlalchemy.url = postgresql://postgres:123456789@localhost:5432/fasterp_db

```

# Database connection

1. create fasterp/database directory
2. create the fasterp/database/dbconnection.py file

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/fasterp_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```

# database models __init__.py file
1. create the database/model directory
2. create the database/model/__init__.py file
3. import the created model in database/model/__init__.py file

```
from .country import Country

```


# env.py of alembic
Open the alembic/env.py and add below line of code


```
*******************

from database.dbconnection import Base # by atul

from database.model import * # by atul
target_metadata = Base.metadata

***********************
```

# Auto Migration

If you want alembic handles migrations follow this method: In the alembic folder edit env.py and find target_metadata line and edit like the following

import the "from main import Base" in alembic/env.py file and set the "target_metadata = Base.metadata" in alembic/env.py file

Reference url https://fastapi.blog/blog/posts/2023-07-20-fastapi-sqlalchemy-migrations-guide

# Generating a Migration

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic revision --autogenerate -m "Initial Migration"

```

# create contries table in database
1. create table by help of https://docs.sqlalchemy.org/en/20/core/metadata.html

```
from database.dbconnection import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column('id',Integer, primary_key=True, index=True)
    country_name = Column('country_name',String(255),nullable=False)
    status = Column('status',Integer,default=1,nullable=True)
    created_at = Column('created_at',DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column('updated_at',DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=True)
    
```


# rollback(downgrade) last migration of alembic
reference of help: https://python-code.dev/articles/270017224 
1. downgrade the last migration command: alembic downgrade -1

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic downgrade -1

``` 

# rollback(downgrade) specific migration of alembic
reference of help: https://python-code.dev/articles/270017224 

1. (method-1): get the latest revision ID. command: alembic current
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic current

```

2.(method-2): You can also get the revision ID from alembic migration file. Go to alembic/versions directory and open the any one migration file. For example 1eaa2206f60f_add_nullable_in_states_table.py here 1eaa2206f60f is the revision ID.

2.(method-3) You can also get the revision ID from alembic migration file. Go to alembic/versions directory and open the any one migration file. For example opent the 1eaa2206f60f_add_nullable_in_states_table.py in this file revision: str = '1eaa2206f60f' you will get.
Note: down_revision: Union[str, None] = '4b268ddeef0d' is the just previous migration file revision ID. If you see down_revision: Union[str, None] = None . Here you will see None instead of previous file revision ID. It means this is the first migration file.


3. rollback(downgrade) the specific migration command: alembic downgrade <revision_id>

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic downgrade 1eaa2206f60f

```
# rollback(downgrade) the all migrated files
Reference: https://alembic.sqlalchemy.org/en/latest/tutorial.html#downgrading

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic downgrade base

```
# upgrade the all migrations
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic upgrade head

```

# relationship and back_populates

1. country.py file module
```
from database.dbconnection import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column('id',Integer, primary_key=True, index=True)
    country_name = Column('country_name',String(255),nullable=False)
    status = Column('status',Integer,default=1,nullable=True)
    created_at = Column('created_at',DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column('updated_at',DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=True)
    country = relationship('Country', back_populates='state')

```

2. state.py file module

```
from database.dbconnection import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
from datetime import datetime

class State(Base):
    __tablename__ = 'states'
    
    id = Column('id',Integer, primary_key=True, index=True)
    state_name = Column('state_name',String(255),nullable=False)
    countries_id = Column('countries_id',Integer,ForeignKey('countries.id'),nullable=True)
    status = Column('status',Integer,default=1,nullable=True)
    created_at = Column('created_at',DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column('updated_at',DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=True)
    state = relationship('Country', back_populates='country')
```

3. country = relationship('Country', back_populates='state') of country.py file country variable used in back_populates='country' in state.py file.
4. state = relationship('Country', back_populates='country') of state.py file state variable used in back_populates='state' in country.py file.


# How see sql query before migration
reference: https://alembic.sqlalchemy.org/en/latest/offline.html

1. method-1: run the command to show sql in console. command: alembic upgrade head --sql

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic upgrade head --sql

```

2. method-2: run the command to write sql queries in a file before migration. command: alembic upgrade head --sql > state.sql

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic upgrade head --sql > state.sql

```

# How to see hostory of all migrated migrations

Reference: https://alembic.sqlalchemy.org/en/latest/tutorial.html

1. run the command to see history of all migrated files
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic history --verbose

```


# How to use already created database in sqlalchemy
1. install the sqlacodegen. reference: https://pypi.org/project/sqlacodegen/

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip install sqlacodegen

```
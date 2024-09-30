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
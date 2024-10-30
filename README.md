
## how to clone project from github?
```
atul@atul-Lenovo-G570:~$ git clone https://github.com/atulkrishnathakur/fasterp.git
```

## How to generate requirements.txt in python?
```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 freeze > requirements.txt
```
## how to get pip version?

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 --version

# Or

(env) atul@atul-Lenovo-G570:~/fasterp$ pip --version

# you can see version is same.
# It means you can use pip3 or pip both command in virtual environment
```

## How to install fastapi using pip?

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip install "fastapi[standard]"
```

## How to run the uvicorn server?
The command uvicorn main:app refers to:

1. main: the file main.py (the Python "module").
2. app: the object created inside of main.py with the line app = FastAPI().
3. --reload: make the server restart after code changes. Only use for development.

```
(env) atul@atul-Lenovo-G570:~/fasterp$ uvicorn main:app --reload
```


## How to install sqlalchemy ORM in fastapi?
```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install sqlalchemy
```

## how to install psycopg2-binary?

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install psycopg2-binary
```

## How to install alembic to create migrations in fastapi?

```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install alembic
```

Below command will create an alembic directory with necessary configuration files.

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic init alembic
```

## How to configure alembic.ini file?

You can see alembic.ini file outside of alembic directory. The alembic.ini file path is fasterp/alembic.ini. 

```
sqlalchemy.url = sqlalchemy.url = postgresql://postgres:123456789@localhost:5432/fasterp_db
```

## How to create database connection with sqlalchemy ORM?

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

## create the database/models/__init__.py file
1. create the database/model directory
2. create the database/model/__init__.py file
3. import the created model in database/model/__init__.py file

```
from .country import Country
```
## How to configure env.py of alembic?
Open the alembic/env.py and add below line of code
```
*******************

from database.dbconnection import Base # by atul

from database.model import * # by atul
target_metadata = Base.metadata

***********************
```

## Auto Migration in alembic

If you want alembic handles migrations follow this method: In the alembic folder edit env.py and find target_metadata line and edit like the following

import the "from main import Base" in alembic/env.py file and set the "target_metadata = Base.metadata" in alembic/env.py file

Reference url https://fastapi.blog/blog/posts/2023-07-20-fastapi-sqlalchemy-migrations-guide

## Generating a Migration by alembic

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic revision --autogenerate -m "Initial Migration"
```

## create contries table in database
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


## rollback(downgrade) last migration of alembic
reference of help: https://python-code.dev/articles/270017224 
1. downgrade the last migration command: alembic downgrade -1

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic downgrade -1
``` 

## rollback(downgrade) specific migration of alembic
reference of help: https://python-code.dev/articles/270017224 

1. (method-1): get the latest revision ID. command: alembic current
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic current
```

2.(method-2): You can also get the revision ID from alembic migration file. Go to alembic/versions directory and open the any one migration file. For example 1eaa2206f60f_add_nullable_in_states_table.py here 1eaa2206f60f is the revision ID.

3.(method-3) You can also get the revision ID from alembic migration file. Go to alembic/versions directory and open the any one migration file. For example opent the 1eaa2206f60f_add_nullable_in_states_table.py in this file revision: str = '1eaa2206f60f' you will get.
Note: down_revision: Union[str, None] = '4b268ddeef0d' is the just previous migration file revision ID. If you see down_revision: Union[str, None] = None . Here you will see None instead of previous file revision ID. It means this is the first migration file.


3. rollback(downgrade) the specific migration command: alembic downgrade <revision_id>

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic downgrade 1eaa2206f60f
```
## rollback(downgrade) the all migrated files of alembic
Reference: https://alembic.sqlalchemy.org/en/latest/tutorial.html#downgrading

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic downgrade base
```
## upgrade the all migrations file
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic upgrade head
```

## relationship and back_populates

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


## How see sql query before migration?
reference: https://alembic.sqlalchemy.org/en/latest/offline.html

1. method-1: run the command to show sql in console. command: alembic upgrade head --sql

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic upgrade head --sql
```

2. method-2: run the command to write sql queries in a file before migration. command: alembic upgrade head --sql > state.sql

```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic upgrade head --sql > state.sql
```

## How to see hostory of all migrated migrations

Reference: https://alembic.sqlalchemy.org/en/latest/tutorial.html

1. run the command to see history of all migrated files
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic history --verbose
```


## How to use already created database in sqlalchemy
1. install the sqlacodegen-v2. reference: https://pypi.org/project/sqlacodegen-v2/
```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install sqlacodegen_v2[citext]
```

2. create a model in models.py for full database
```
(env) atul@atul-Lenovo-G570:~/fasterp/database/model$ sqlacodegen_v2 postgresql://postgres:123456789@localhost:5432/fasterp_db > models.py
```

3. create a model file for every table
```
(env) atul@atul-Lenovo-G570:~/fasterp/database/model$ sqlacodegen_v2 postgresql://postgres:123456789@localhost:5432/fasterp_db --tables countries > country.py

# Or

(env) atul@atul-Lenovo-G570:~/fasterp/database/model$ sqlacodegen_v2 postgresql://postgres:123456789@localhost:5432/fasterp_db --tables countries states > location.py
```

Note: currently sqlcodegen does not support python3.12 therefore I used sqlacodegen_v2. If sqlacodegen support your python version then use it.

4. create the migration 
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic revision --autogenerate -m "initial migration"
```

5. Comment the all code of upgrade() and downgrade() funciton and use the pass keyword
```
def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('country')
    # ### end Alembic commands ###
    pass


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('country',
    # sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
    # sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.PrimaryKeyConstraint('id', name='country_pkey')
    # )
    # ### end Alembic commands ###
    pass
```

5. migrate the this file
6. create a new migration file to add new column
Note: do not use --autogenerate in command to create migration
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic revision -m "initial add new column"
```
Change migration file to add column like below:
```
"""initial add new column

Revision ID: 84af06e88411
Revises: 4f6d19b3053b
Create Date: 2024-10-14 11:06:55.899661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84af06e88411'
down_revision: Union[str, None] = '4f6d19b3053b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('country', sa.Column('code', sa.BigInteger))

def downgrade() -> None:
    op.drop_column('country', 'code')

```
7. update new column in the model 
```
from sqlalchemy import BigInteger, Column, PrimaryKeyConstraint, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='country_pkey'),
    )

    id = mapped_column(BigInteger)
    name = mapped_column(Text)
    code = mapped_column(Text, nullable=True)  # Add the new column here
```

8. create new migration to creatte new table 
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic revision -m "create account table"
```

change the migration file to crate table
```
"""create account table

Revision ID: 33f75298723e
Revises: 84af06e88411
Create Date: 2024-10-14 11:26:56.240932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33f75298723e'
down_revision: Union[str, None] = '84af06e88411'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade() -> None:
    op.drop_table('account')

```
9. create the model file for account table 

## SQL Datatype Objects for sqlalchemy
Reference: https://docs.sqlalchemy.org/en/20/core/types.html

## Cascades for sqlalchemy
Reference: https://docs.sqlalchemy.org/en/20/orm/cascades.html


## timezone setting
1. install the pytz for timezone
```
(env) atul@atul-Lenovo-G570:~/fasterp$ pip3 install pytz
```

## Table Configuration with Declarative for mapped_column
Reference: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html

## How to configure alembic for multiple schema of postgresql
1. create alembic directory in your project
2. create hr and sales directory in alembic directory
3. Initialize Alembic within each schema-specific directory:
```
alembic -c alembic/hr/alembic.ini init alembic/hr
alembic -c alembic/sales/alembic.ini init alembic/sales
```

4. Configure alembic/hr/alembic.ini and alembic/sales/alembic.ini. Set the same database for both. If database name is different then you write diffent database name.

```
script_location = alembic/hr
sqlalchemy.url = postgresql://postgres:123456789@localhost:5432/fasterp_db
```

```
script_location = alembic/sales
sqlalchemy.url = postgresql://postgres:123456789@localhost:5432/fasterp_db
```

5. create include_object() function in alembic/hr/env.py and sales/env.py file
6. set version_table_schema= 'hr'
7. create the model/hr/__init__.py and model/sales/__init__.py 
8. change in alembic/hr/.env file
```
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from database.dbconnection import Base # by atul
from database.dbconfig import SCHEMA_HR

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from database.model.hr import * # by atul
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    schema_name = SCHEMA_HR
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema=schema_name
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    def include_object(object, name, type_, reflected, compare_to):
        if type_ == "table" and object.schema == SCHEMA_HR:
            return True
        return False

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        schema_name = SCHEMA_HR
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema=schema_name,
            include_object=include_object,
            include_schemas=True
        )

        with context.begin_transaction():
            context.execute(f"SET search_path TO {schema_name}")
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

9. change in alembic/sales/.env

```
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from database.dbconnection import Base # by atul

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from database.model.sales import * # by atul
target_metadata = Base.metadata
from database.dbconfig import SCHEMA_SALES

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    schema_name = SCHEMA_SALES
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema=schema_name
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    def include_object(object, name, type_, reflected, compare_to):
        if type_ == "table" and object.schema == SCHEMA_SALES:
            return True
        return False

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        schema_name = SCHEMA_SALES
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema=schema_name,
            include_object=include_object,
            include_schemas=True
        )

        with context.begin_transaction():
            context.execute(f"SET search_path TO {schema_name}")
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

10. create migration file by alembic for schema like hr
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic -c alembic/hr/alembic.ini revision --autogenerate -m "Initial user migration"
``` 
11. migrate the generated migration file for schema like hr
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic -c alembic/hr/alembic.ini upgrade head
```

12. downgrade migrated migration for a schema like hr
```
(env) atul@atul-Lenovo-G570:~/fasterp$ alembic -c alembic/hr/alembic.ini downgrade -1
```

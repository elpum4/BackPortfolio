### Install alembic if not yet installed

```
$ pip install alembic
```

```
$ cd <module path>
```

## Running the autogenerating script*

```
$ alembic revision --autogenerate -m "Commit message"
```


## Applying (*upgrading*) the changes to the database schema*

* To its most recent state

```
$ alembic upgrade head
```

* To a particular db version

```
$ alembic upgrade <version_number>
```

## Working with branches.
### For merging two branches use

```
$  alembic heads
$  alembic merge -m "merge <head_1_id> and <head_2_id>" head_1_id head_2_id
$  alembic upgrade head
```

## Downgrading (*undoing*) the changes to the database schema

```
$ alembic downgrade base
```

### \* If you not have an environment yet:

## Creating a new environment


```
$ cd yourproject
$ alembic init alembic
```

### For further details, visit the [Alembic documentation](http://alembic.zzzcomputing.com/en/latest/index.html)

"""Module for testing the User model in the todolist application."""

import pytest
from models.db import connect, execute_query


@pytest.fixture(scope='module')
def test_db():
    """Create a test database and return a connection object."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO test_table (name) VALUES ("test")')
    conn.commit()
    yield conn
    cursor.execute('DROP TABLE test_table')
    conn.commit()
    cursor.close()
    conn.close()


def test_connect():
    """Test that the connect() function returns a connection object."""
    conn = connect()
    assert conn is not None
    conn.close()


def test_execute_query():
    """Test that the execute_query() function executes a query and returns the results."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO test_table (name) VALUES ("test")')
    conn.commit()
    query = 'SELECT * FROM test_table where name = ?'
    params = ('test',)
    results = execute_query(query, params=params)
    cursor.execute('DROP TABLE test_table')
    conn.commit()
    cursor.close()
    conn.close()
    assert len(results) == 1
    assert results[0][1] == 'test'

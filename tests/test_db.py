import sqlite3

import pytest
from flask import Flask

from flaskr.db import get_db


def test_get_close_db(app: Flask):
    with app.app_context():
        db = get_db()
        assert db is get_db()
    with pytest.raises(sqlite3.ProgrammingError) as error:
        db.execute('SELECT 1')
    assert 'closed' in str(error.value)


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False
    
    def fake_init_db():
        Recorder.called = True
    
    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Создана' in result.output
    assert Recorder.called

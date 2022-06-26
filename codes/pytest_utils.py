from typing import Optional
from db.redis import RedisDB


db = RedisDB()


def reset_db():
    db.reset()


def add_admin_account(name = 'admin', password = 'password'):
    """add one admin account"""
    resp, info = db.create_user(name, password, '0', 'admin')
    assert resp, info


def add_student_account(name, password, stuNum):
    """add one admin account"""
    resp, info = db.create_user(name, password, stuNum, 'user')
    assert resp, info


def get_token(client, name: str = 'admin', password: str = 'password'):
    # get token, default admin token
    resp = client.post('/login', json = { 
        'name': name, 
        'password': password,
    })
    assert resp.status_code == 200, resp.json()
    token = resp.json()['auth']
    return token


def token2header(token: str):
    return { 'Content-Type': 'application/json', 'Auth-Token': token }
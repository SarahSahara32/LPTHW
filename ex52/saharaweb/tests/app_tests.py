from nose.tools import *
from saharaweb.app import app
from tools import assert_response

client = app.test_client() # create a testing client (like a fake browser)
client.testing = True # enable this so that exceptions in your code bubble up to the testing client

def test_index():
    global client
    resp = client.get('/')
    assert_response(resp, status=302) #root url should give back a redirect

    resp = client.get('/game')
    assert_response(resp) #just make sure we got a valid response

    resp = client.post('/game')
    assert_response(resp, contains="You Died!")

    # Go to another scene in the game
    testdata = {'userinput': 'south'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Oasis")

    # From there, go to yet another scene in the game
    testdata = {'userinput': 'yes'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Tribe of Cajun")

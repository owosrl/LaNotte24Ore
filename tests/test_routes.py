from web import create_app

def test_index():
    app = create_app('lanotte24ore.test')
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_signup():
    app = create_app('lanotte24ore.test')
    client = app.test_client()
    response = client.get('/signup')
    assert response.status_code == 200
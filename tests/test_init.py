
def test_app_created(app):
	assert app.name == 'delivery.app'


def test_config_is_loaded(config):
	assert config['DEBUG'] is False


def test_app_index(client):
	assert client.get('/').status_code == 200

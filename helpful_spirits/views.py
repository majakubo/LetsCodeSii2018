from helpful_spirits import app

@app.route('/')
def index():
	return 'Hello, world!'

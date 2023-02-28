from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

# Importing routes
from routes.info_routes import info_bp
from routes.validate_routes import validate_bp
from routes.count_routes import count_bp
from routes.find_routes import find_bp

# Creating the app and configuring it
app = Flask(__name__)
app.config['API_BASE_URL'] = '/api/v1'

# Swagger UI
SWAGGER_URL = '/api/v1/docs'
API_URL = '/static/swagger.yml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "FLAMAPY API - V1"
    }
)

# Adding blueprints
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(info_bp)
app.register_blueprint(validate_bp)
app.register_blueprint(count_bp)
app.register_blueprint(find_bp)


@app.route(app.config['API_BASE_URL'], methods=['GET'])
def hello_world():
    return 'FLAMAPY API - V1 - Running and ready to use!'


if __name__ == '__main__':
    app.run()

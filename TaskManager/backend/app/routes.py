from flask import Blueprint

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/api/health')
def health():
    return {"status": "ok"}
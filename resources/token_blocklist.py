from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import TokenSchema
from models import TokenModel


blp = Blueprint("token_blocklists", __name__, description="Operations on token blocklist")

@blp.route("/token")
class TokenList(MethodView):
    @blp.response(200, TokenSchema(many=True))
    def get(self):
        return TokenModel.query.all()

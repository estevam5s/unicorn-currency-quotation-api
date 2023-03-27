from flask import Flask, render_template_string, request
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin


app = Flask(__name__)

# Configuração do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_app.db"
app.config["SECRET_KEY"] = "my_secret_key"
app.config["CSRF_ENABLED"] = True
app.config["USER_ENABLE_EMAIL"] = False

db = SQLAlchemy(app)

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

user_roles = db.Table("user_roles",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id", ondelete="CASCADE")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id", ondelete="CASCADE"))
)

# Definição do modelo de usuário
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default="")
    active = db.Column(db.Boolean(), nullable=False, server_default="0")
    # ...
    roles = db.relationship("Role", secondary=user_roles, backref=db.backref("users", lazy="dynamic"))

# Criação das tabelas do banco de dados
db.create_all()

# Configuração do Flask-User
user_manager = UserManager(app, db, User)

@app.route("/")
@login_required
def home():
    return render_template_string("<h1>Bem-vindo, {{ current_user.username }}!</h1><p><a href={{ url_for('user.logout') }}>Logout</a></p>")

@app.route("/admin")
@roles_required("Admin")
def admin_dashboard():
    return render_template_string("<h1>Painel de Administração</h1><p><a href={{ url_for('user.logout') }}>Logout</a></p>")

if __name__ == "__main__":
    app.run(debug=True)

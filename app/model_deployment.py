import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post
import os


@app.shell_context_processor
def make_shell_context():
    return {"sa": sa, "so": so, "db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

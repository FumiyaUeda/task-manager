from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    note = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Item {self.id} {self.title!r}>"

# Flask 3対応: 起動時にDBを初期化（before_first_requestは廃止）
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    items = Item.query
    if q:
        items = items.filter(Item.title.contains(q) | Item.note.contains(q))
    items = items.order_by(Item.id.desc()).all()
    return render_template("index.html", items=items, q=q)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        note = request.form.get("note", "").strip()
        if not title:
            flash("タイトルは必須です。", "error")
            return redirect(url_for("create"))
        db.session.add(Item(title=title, note=note))
        db.session.commit()
        flash("作成しました。", "success")
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/<int:item_id>/edit", methods=["GET", "POST"])
def edit(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == "POST":
        item.title = request.form.get("title", "").strip()
        item.note = request.form.get("note", "").strip()
        if not item.title:
            flash("タイトルは必須です。", "error")
            return redirect(url_for("edit", item_id=item.id))
        db.session.commit()
        flash("更新しました。", "success")
        return redirect(url_for("index"))
    return render_template("edit.html", item=item)

@app.route("/<int:item_id>/delete", methods=["POST"])
def delete(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash("削除しました。", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    # ローカル実行: python app.py
    app.run(debug=True)

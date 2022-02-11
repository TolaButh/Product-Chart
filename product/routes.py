from turtle import title
from flask import redirect, render_template, request, url_for,flash
from product import db, app
from product.forms import ProductManagement
from product.models import Product
import json
@app.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    pro = Product.query.paginate(page=page, per_page=4)
    return render_template("index.html", title = "Home Page", products = pro)

@app.route("/add_product", methods=["POST", "GET"])
def add_product():
    form = ProductManagement()
    if form.validate_on_submit():
        pro = Product(product_id=form.product_id.data, product_name=form.product_name.data, product_type=form.product_type.data, category=form.category.data, price=form.price.data)
        db.session.add(pro)
        db.session.commit()
        flash("Add product Successfully", "success")
        return redirect(url_for("home"))
    return render_template("add_product.html", title="Add Product", form = form)

@app.route("/product/delete: <int:id>")
def delete(id):
    pro = Product.query.filter_by(id=id).first()
    db.session.delete(pro)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/product/dashboard")
def dashboard():
    income_vs_expense = db.session.query(db.func.sum(Product.price), Product.product_type).group_by(Product.product_type).order_by(Product.product_type).all()

    category_comparison = db.session.query(db.func.sum(Product.price), Product.category).group_by(Product.category).order_by(Product.category).all()

    dates = db.session.query(db.func.sum(Product.price), Product.date).group_by(Product.date).order_by(Product.date).all()

    income_category = []
    for price, _ in category_comparison:
        income_category.append(price)

    income_expense = []
    for total_price, _ in income_vs_expense:
        income_expense.append(total_price)

    over_time_expenditure = []
    dates_label = []
    for price, date in dates:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_expenditure.append(price)

    return render_template('dashboard.html',
                            income_vs_expense=json.dumps(income_expense),
                            income_category=json.dumps(income_category),
                            over_time_expenditure=json.dumps(over_time_expenditure),
                            dates_label =json.dumps(dates_label)
                        )
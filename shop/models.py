from shop import db

class Admin(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False,unique=True)
    password=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return "user {}".format(self.username)


class Seller(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False,unique=True)
    password=db.Column(db.Text(),nullable=False)
    type=db.Column(db.String(25),nullable=False)
    comm_type=db.Column(db.String(25),nullable=False)
    products=db.relationship("Product",backref="seller",lazy=True)

    def __repr__(self):
        return "seller {}".format(self.username)

class Product(db.Model):
    product_id=db.Column(db.Integer(),primary_key=True)
    prod_name=db.Column(db.String(255),nullable=False,unique=True)
    selling_price=db.Column(db.Integer(),nullable=False,unique=True)
    cost_price=db.Column(db.Integer(),nullable=False,unique=True)
    discount=db.Column(db.Integer(),nullable=False,unique=True)
    stock=db.Column(db.Integer(),nullable=False,unique=True)
    prod_type=db.Column(db.String(80),nullable=False,unique=True)
    seller_id=db.Column(db.Integer(),db.ForeignKey('seller.id'))

    def __repr__(self):
        return "product {}".format(self.prod_name)

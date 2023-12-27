class ProductNotes(db.Model):
    __tablename__ = 'product_notes'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String(255), db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_note = db.Column(db.String(255), db.ForeignKey('brand_opl.product_notes.product_id'), primary_key=True, nullable=False)


    product_notes = db.relationship('ProductNotes', backref='product', lazy='dynamic')


        # Add Product Notes
        selected_notes = form.product_notes.data
        for note in selected_notes:
            product_note = ProductNotes(product=new_product.product_id, product_note=note)
            db.session.add(product_note)


AttributeError: 'str' object has no attribute '_sa_instance_state'

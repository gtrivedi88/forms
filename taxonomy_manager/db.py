$(document).ready(function () {
        // Add more Product Reference and Reference Description pairs
        $(".add-notes").click(function () {
            var referencePair = $(".product-notes-pair:first").clone();
            referencePair.find("input, textarea").val('');
            referencePair.find(".add-notes").hide();
            referencePair.find(".remove-notes").show();
            $("#product-notes").append(referencePair);
        });

        // Remove the current Product Reference and Reference Description pair
        $(document).on("click", ".remove-notes", function () {
            $(this).closest(".product-notes-pair").remove();
        });
    });




    <fieldset class="product-notes-group">
        <legend>Product Notes Information</legend>
        <div id="product-notes">
            <div class="product-notes-pair">
                <div class="form-field">
                    <label for="{{ form.product_link.id }}">Product Notes</label>
                    {{ form.product_link(cols=40) }}
                </div>
                <div class="form-field buttons-row">
                    <button type="button" class="add-notes">Add more</button>
                    <button type="button" class="remove-notes" style="display: none;">Delete</button>
                </div>
            </div>
        </div>
    </fieldset>



        # Add Product Log
        product_log_data = []
        for i in range(len(request.form.getlist('edit_notes'))):
            edit_notes = request.form.getlist('edit_notes')[i]
            
            if edit_notes:
                product_log_data.append({
                    'edit_notes': edit_notes,
                })

        for notes_data in product_log_data:
            product_log = ProductLog(
                product_id=new_product.product_id,
                edit_notes=notes_data['edit_notes'],
                edit_date=date.today()
            )
            db.session.add(product_log)


class ProductLog(db.Model):
    """
    Represents a log of changes made to a product.

    Attributes:
    - log_id: Unique identifier for the log entry.
    - product_id: Foreign key to Product.
    - edit_date: Date when the edit was made.
    - edit_notes: Notes associated with the edit.
    - username: Username of the user who made the edit.
    """

    __tablename__ = 'product_log'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "edit_date"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    edit_date = db.Column(db.Date, nullable=False)
    edit_notes = db.Column(db.String(65535), nullable=True)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('ProductLog', lazy='dynamic'))

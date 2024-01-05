class ProductComponents(db.Model):
    """
    Represents a many-to-many relationship between Product and Components.

    Attributes:
    - product_id: Foreign key to Product.
    - component_id: Foreign key to Components.
    """

    __tablename__ = 'product_components'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "component_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    component_id = db.Column(db.String(255), nullable=False, primary_key=True)
    component_type = db.Column(db.String(255), nullable=False)

    # Define the relationship to the existing Product model
    product = db.relationship('Product', backref='components', foreign_keys=[product_id])


    # Add a new field for selecting a component
    component = SelectField('Parent', choices=[], coerce=str)
    component_type = SelectField('Component Type', choices=[('component', 'Component'), ('operator', 'Operator'), ('variant', 'Variant')], coerce=str)


    <fieldset class="product-component-group">
    <legend>Product Parent Information</legend>
        <div class="form-field">
            <label for="{{ form.component.id }}">{{ form.component.label }}</label>
            <select id="{{ form.component.id }}" name="{{ form.component.name }}">
                {% for value, label in form.component.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="form-field">
            <label for="{{ form.component_type.id }}">{{ form.component_type.label }}</label>
            <select id="{{ form.component_type.id }}" name="{{ form.component_type.name }}">
                {% for value, label in form.component_type.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
        <br>
        <button type="button" class="add-component-group" style="margin-top: 10px;">Add more components</button>
        <button type="button" class="remove-component-group" style="display: none;">Delete</button>
    </fieldset>

<fieldset class="product-partner-group">
    <legend>Product Partners Information</legend>
        <div class="form-field">
            <label for="{{ form.partner.id }}">{{ form.partner.label }}</label>
            <select id="{{ form.partner.id }}" name="{{ form.partner.name }}" multiple>
                {% for value, label in form.partner.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
    </fieldset>


    class Partner(db.Model):
    """
    Represents partners.

    Attributes:
    - partner_id: Unique identifier for the partner.
    - partner_name: Name of the partner.
    - persona_id: Persona ID for the partner.
    """

    __tablename__ = 'partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "partner_id"
    __term__ = "partner_name"

    partner_id = db.Column(db.String, primary_key=True)
    partner_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_partners = db.relationship('ProductPartners', backref='partner', lazy='dynamic')

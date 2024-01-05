class ProductAlias(db.Model):
    """
    Represents aliases associated with a product.

    Attributes:
    - alias_id: Unique identifier for the alias.
    - product_id: Foreign key to Product.
    - alias_name: Name associated with the alias.
    - alias_type: Type of the alias (Short, Acronym, Cli, Former).
    - alias_approved: Indicates if the alias is approved.
    - previous_name: Indicates if the alias is a previous name.
    - tech_docs: Indicates if the alias is approved for tech docs.
    - tech_docs_cli: Indicates if the alias is approved for tech docs code/CLI.
    - alias_notes: Notes associated with the alias.

    Relationships:
    - product: Relationship to Product for easy access to the associated product.
    """

    __tablename__ = 'product_alias'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "alias_id"
    __term__ = "alias_name"

    alias_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), nullable=False)
    alias_name = db.Column(db.String(255), nullable=False)
    alias_type = db.Column(db.String(255), nullable=False)
    alias_approved = db.Column(db.Boolean, nullable=True)
    previous_name = db.Column(db.Boolean, nullable=True)
    tech_docs = db.Column(db.Boolean, nullable=True)
    tech_docs_cli = db.Column(db.Boolean, nullable=True)
    alias_notes = db.Column(db.String(65535))

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('aliases', lazy='dynamic'))



class MyForm(FlaskForm):
    product_name = TextAreaField('Product Name *', validators=[DataRequired()])
    product_description = TextAreaField('Product Description')
    upcoming_change = BooleanField('Upcoming Change')
    deprecated = BooleanField('Deprecated')
    
    # SelectField for Product Status
    product_status = SelectField('Status', choices=[('Deprecated', 'Deprecated'), ('Upcoming', 'Upcoming'), ('Available', 'Available')])

    # SelectField for Product Status Details
    product_status_detail = SelectField('Status', choices=[('General Availability', 'General Availability'), ('Live', 'Live'), ('Developer Preview', 'Developer Preview'), ('Technology Preview', 'Technology Preview'), ('Limited Availability', 'Limited Availability'), ('Service Preview', 'Service Preview'), ('Null', 'NULL')])

    # SelectField for Product Type
    product_type = SelectMultipleField('Product Type', validators=[DataRequired()])

    # SelectField for Product Portfolio
    product_portfolio = SelectMultipleField('Portfolio')

    # Field for Product Notes
    product_notes = TextAreaField('Product Notes')

    # Field for Product References
    product_link = TextAreaField('Product Reference')
    link_description = TextAreaField('Reference Description')

    # Fields for Product Alias
    alias_name = StringField('Alias Name')
    alias_type = SelectField('Alias Type *', choices=[('Short', 'Short'), ('Acronym', 'Acronym'), ('Cli', 'Cli'), ('Former', 'Former')], validators=[DataRequired()])
    alias_approved = BooleanField('Alias Approved')
    previous_name = BooleanField('Previous Name')
    tech_docs = BooleanField('Approved For Tech Docs')
    tech_docs_cli = BooleanField('Approved For Tech Docs Code/CLI')
    alias_notes = TextAreaField('Alias Notes')

    submit = SubmitField('Add Product')



        # Print or log form data for debugging
        print("Alias names:", request.form.getlist('alias_name'))
        print("Alias types:", request.form.getlist('alias_type'))

        product_alias_data = []
        for i in range(len(request.form.getlist('alias_name'))):
            alias_name = request.form.getlist('alias_name')[i]
            alias_type = request.form.getlist('alias_type')[i]
            alias_approved = request.form.getlist('alias_approved')[i]
            previous_name = request.form.getlist('previous_name')[i]
            tech_docs = request.form.getlist('tech_docs')[i]
            tech_docs_cli = request.form.getlist('tech_docs_cli')[i]
            alias_notes = request.form.getlist('alias_notes')[i]

            if alias_name and alias_type:
                product_alias_data.append({
                    'alias_name': alias_name,
                    'alias_type': alias_type,
                    'alias_approved': alias_approved,
                    'previous_name': previous_name,
                    'tech_docs': tech_docs,
                    'tech_docs_cli': tech_docs_cli,
                    'alias_notes': alias_notes
                })

        # Print or log product_alias_data for debugging
        print("Product alias data:", product_alias_data)

        # Loop to save aliases
        for alias_data in product_alias_data:
            # Convert 'y' to True, and an empty string to False
            alias_approved = alias_data['alias_approved'].lower() == 'y'
            previous_name = alias_data['previous_name'].lower() == 'y'
            tech_docs = alias_data['tech_docs'].lower() == 'y'
            tech_docs_cli = alias_data['tech_docs_cli'].lower() == 'y'

            product_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=alias_data['alias_name'],
                alias_type=alias_data['alias_type'],
                alias_approved=alias_approved,
                previous_name=previous_name,
                tech_docs=tech_docs,
                tech_docs_cli=tech_docs_cli,
                alias_notes=alias_data['alias_notes']
            )
            db.session.add(product_alias)

        # Commit changes to the database session
        db.session.commit()






$(document).ready(function () {
    // Add more Product Alias Information groups
    $(document).on("click", ".add-alias-group", function () {
        var newAliasGroup = $(".product-alias-group:first").clone();
        newAliasGroup.find('input, select').val('');
        newAliasGroup.find('.remove-alias-group').show();
        newAliasGroup.find('.add-alias-group').remove(); // Remove the Add button in the cloned group
        $(".product-alias-group:last").after(newAliasGroup);
    });

    // Remove the current Product Alias Information group
    $(document).on("click", ".remove-alias-group", function () {
        if ($(".product-alias-group").length > 1) {
            $(this).closest(".product-alias-group").remove();
        }
    });
});





<fieldset class="product-alias-group">
        <legend>Product Alias Information</legend>
        <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
        {{ form.alias_name(cols=40) }}
        
        <br><br>
        
        <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
        {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
        
        <br><br>

        <div class="form-group">
            <div class="checkbox-field">
                {{ form.alias_approved() }}
                <label for="{{ form.alias_approved.id }}" data-toggle="tooltip"
                    title="Leaving it blank for unapproved aliases.">{{ form.alias_approved.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.previous_name() }}
                <label for="{{ form.previous_name.id }}">{{ form.previous_name.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.tech_docs() }}
                <label for="{{ form.tech_docs.id }}">{{ form.tech_docs.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.tech_docs_cli() }}
                <label for="{{ form.tech_docs_cli.id }}">{{ form.tech_docs_cli.label }}</label>
            </div>
        </div>
        
        <br><br>

        <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
        {{ form.alias_notes(cols=40) }}

        <br>
        <button type="button" class="add-alias-group" style="margin-top: 10px;">Add more aliases</button>
        <button type="button" class="remove-alias-group" style="display: none;">Delete</button>
    </fieldset>

    <br><br>
    
    {{ form.submit(style="background-color: #1a73e8; color: #ffffff;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/alias.js') }}"></script>

{% endif %}

{% if success_message %}
<p class="success">{{ success_message }}</p>
<br><br>
<a href="{{ url_for('add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}


label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input,
textarea,
select {
    padding: 5px;
    margin-bottom: 10px;
}

button {
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.checkbox-row {
    display: flex;
    align-items: center;
}

.checkbox-row input {
    margin-right: 10px;
}

.button-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: #1a73e8;
    color: white;
    text-decoration: none;
    border-radius: 12px;
}

.success {
    color: green;
    font-weight: bold;
}

.product-reference-pair {
    display: flex;
}

.form-group {
    display: flex;
}

.form-field {
    flex: 1;
    /* Adjust the width as needed */
}

.checkbox-field {
    display: flex;
    flex: auto;
}

.checkbox-field input {
    margin-right: 10px;
    /* Adjust the space between the checkbox and label */
}

.buttons-row {
    align-items: center;
    margin-top: 35px;
}

.buttons-row button {
    margin-left: 10px;
}

.remove-reference {
    background-color: #ff0000;
    color: white;
}

.remove-reference:hover {
    background-color: #cc0000;
}

/* Add this to your main.css file or include it in your HTML file */

.product-alias-group {
    border: 2px solid #0a63ca;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
    position: relative;
}

.product-alias-group legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}

.remove-alias-group {
    background-color: #ff0000;
    color: white;
    margin-top: 10px;
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.remove-alias-group:hover {
    background-color: #cc0000;
}

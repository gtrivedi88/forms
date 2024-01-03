    # SelectField for Product Status
    product_status = SelectField('Status', choices=[('deprecated', 'Deprecated'), ('upcoming', 'Upcoming'), ('available', 'Available')], validators=[DataRequired()])

    # SelectField for Product Status Details
    product_status_detail = SelectField('Status', choices=[('general availability', 'General Availability'), ('live', 'Live'), ('developer preview', 'Developer Preview'), ('technology preview', 'Technology Preview'), ('limited availability', 'Limited Availability'), ('service preview', 'Service Preview'), ('null', 'NULL')], validators=[DataRequired()])


    <div class="form-group">
        <div class="form-field">
            <label for="{{ form.product_status.id }}">Status</label>
            {{ form.product_status(id="status-dropdown", class="status-dropdown") }}
        </div>
    
        <div class="form-field">
            <label for="{{ form.product_status_detail.id }}">Status details</label>
            {{ form.product_status_detail(id="status-details-dropdown", class="status-details-dropdown") }}
        </div>
    </div>

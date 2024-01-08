        # Add Product Components
        product_components_data = []
        component_ids = request.form.getlist('component')
        component_types = request.form.getlist('component_type')

        save_to_database = any(component_id != 'Select' and component_type != 'Select' for component_id, component_type in zip(component_ids, component_types))

        if save_to_database:
            for component_id, component_type in zip(component_ids, component_types):
                product_components_data.append({
                    'component_id': component_id,
                    'component_type': component_type
                })

            # Loop to save components
            for component_data in product_components_data:
                component_id = component_data['component_id']
                component_type = component_data['component_type']

                # Assuming you have a ProductComponents model with appropriate fields
                product_component = ProductComponents(
                    product_id=new_product.product_id,
                    component_id=component_id,
                    component_type=component_type
                )
                db.session.add(product_component)




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



$(document).ready(function () {
    // Add more Product Component Information groups
    $(document).on("click", ".add-component-group", function () {
        var newComponentGroup = $(".product-component-group:first").clone();
        newComponentGroup.find('select').val('');
        newComponentGroup.find('.remove-component-group').show();
        newComponentGroup.find('.add-component-group').remove(); // Remove the Add button in the cloned group
        $(".product-component-group:last").after(newComponentGroup);

        // Update the event handler for the new remove button
        $(document).on("click", ".remove-component-group", function () {
            if ($(".product-component-group").length > 1) {
                $(this).closest(".product-component-group").remove();
            }
        });

        // Update the validation for the new select elements
        newComponentGroup.find('select').change(function () {
            validateComponentFields();
        });
    });

    // Initial validation for existing select elements
    $(".product-component-group select").change(function () {
        validateComponentFields();
    });

    function validateComponentFields() {
        var hasNonDefaultValues = false;

        $(".product-component-group select").each(function () {
            if ($(this).val() !== '' && $(this).val() !== 'Select') {
                hasNonDefaultValues = true;
                return false; // Break out of the loop early
            }
        });

        if (hasNonDefaultValues) {
            $(".product-component-group select").prop('required', true);
        } else {
            $(".product-component-group select").prop('required', false);
        }
    }
});

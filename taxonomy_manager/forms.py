$(document).ready(function () {
    // Initial choices for Status Details
    var initialStatusDetailsChoices = {
        'Select': 'Select',
        'General Availability': 'General Availability',
        'Live': 'Live',
        'Developer Preview': 'Developer Preview',
        'Technology Preview': 'Technology Preview',
        'Limited Availability': 'Limited Availability',
        'Service Preview': 'Service Preview',
        'Null': 'NULL'
    };

    // Update Status Details choices based on Product Status
    function updateStatusDetailsChoices() {
        var selectedStatus = $('#status-dropdown').val();
        var statusDetailsDropdown = $('#status-details-dropdown');

        // Reset choices to initial state
        statusDetailsDropdown.empty();

        if (selectedStatus === 'Deprecated') {
            // If Deprecated is selected, show only 'NULL' in Status Details
            statusDetailsDropdown.append($('<option>', { value: 'Null', text: 'NULL' }));
        } else {
            // If any other status is selected, show all choices
            $.each(initialStatusDetailsChoices, function (value, label) {
                statusDetailsDropdown.append($('<option>', { value: value, text: label }));
            });
        }
    }

    // Initial setup
    updateStatusDetailsChoices();

    // Attach event handler to Product Status dropdown change event
    $('#status-dropdown').change(function () {
        updateStatusDetailsChoices();
    });
});


        # Create a new product instance
        new_product = Product(
            product_name=form.product_name.data,
            product_description=form.product_description.data,
            upcoming_change=form.upcoming_change.data,
            deprecated=form.deprecated.data,
            product_status=form.product_status.data if form.product_status.data != 'Select' else '',
            last_updated=created_date,
            created=created_date,
            product_status_detail=form.product_status_detail.data if form.product_status.data == 'Deprecated' and form.product_status_detail.data == 'NULL' else ''
        )

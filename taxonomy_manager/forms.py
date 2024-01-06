function updateStatusDetailsChoices() {
    var selectedStatus = $('#status-dropdown').val();
    var statusDetailsDropdown = $('#status-details-dropdown');

    // Reset choices to initial state
    statusDetailsDropdown.empty();

    if (selectedStatus === 'Select') {
        // If 'Select' is selected, disable validation for the status field
        $('#status-dropdown').removeAttr('required');
    } else {
        // If any other status is selected, show all choices
        $('#status-dropdown').attr('required', 'required');

        // Show the appropriate choices based on the selected status
        $.each(initialStatusDetailsChoices, function (value, label) {
            if (selectedStatus === 'Deprecated' && value === 'Null') {
                // If 'Deprecated' is selected, mark 'NULL' as selected
                statusDetailsDropdown.append($('<option>', { value: value, text: label, selected: 'selected' }));
            } else {
                // For other statuses or non-'Deprecated' status, show all choices
                statusDetailsDropdown.append($('<option>', { value: value, text: label }));
            }
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

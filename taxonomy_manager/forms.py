document.addEventListener("DOMContentLoaded", function() {
        var statusDropdown = document.getElementById("status-dropdown");
        var statusDetailsDropdown = document.getElementById("status-details-dropdown");
        var form = document.getElementById("your-form-id");  // Replace 'your-form-id' with the actual ID of your form

        // Function to update Status Details dropdown based on selected Status
        function updateStatusDetailsOptions() {
            var selectedStatus = statusDropdown.value;

            // If 'Deprecated' is selected, set Status Details to 'NULL' and disable other options
            if (selectedStatus === "Deprecated") {
                statusDetailsDropdown.value = "NULL";
                statusDetailsDropdown.disabled = true;
            } else {
                // Enable Status Details dropdown and reset its value
                statusDetailsDropdown.disabled = false;
                statusDetailsDropdown.value = "Select";
            }
        }

        // Attach an event listener to the Status dropdown
        statusDropdown.addEventListener("change", updateStatusDetailsOptions);

        // Attach an event listener to the form submission
        form.addEventListener("submit", function(event) {
            // Check if 'Deprecated' is selected before submitting the form
            if (statusDropdown.value === "Deprecated") {
                // Set 'NULL' as the value of Status Details
                statusDetailsDropdown.value = "NULL";
            }
            // You can also disable the Status Details dropdown here if needed

            // Convert 'NULL' to an empty string before submission
            if (statusDetailsDropdown.value === "NULL") {
                statusDetailsDropdown.value = "";
            }
        });

        // Trigger initial update
        updateStatusDetailsOptions();
    });

$(document).ready(function () {
    // Add more Product Component Information groups
    $(document).on("click", ".add-component-group", function () {
        var newComponentGroup = $(".product-component-group:first").clone();
        newComponentGroup.find('select').val('');
        newComponentGroup.find('.remove-component-group').show();
        newComponentGroup.find('.add-component-group').remove(); // Remove the Add button in the cloned group
        $(".product-component-group:last").after(newComponentGroup);
    });

    // Remove the current Product Component Information group
    $(document).on("click", ".remove-component-group", function () {
        if ($(".product-component-group").length > 1) {
            $(this).closest(".product-component-group").remove();
        }
    });
});

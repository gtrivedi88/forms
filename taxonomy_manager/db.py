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

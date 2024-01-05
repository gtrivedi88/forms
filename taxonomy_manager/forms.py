$(document).ready(function () {
        // Add more Product Reference and Reference Description pairs
        $(".add-reference").click(function () {
            var referencePair = $(".product-reference-pair:first").clone();
            referencePair.find("input, textarea").val('');
            referencePair.find(".add-reference").hide();
            referencePair.find(".remove-reference").show();
            $("#product-references").append(referencePair);
        });

        // Remove the current Product Reference and Reference Description pair
        $(document).on("click", ".remove-reference", function () {
            $(this).closest(".product-reference-pair").remove();
        });
    });

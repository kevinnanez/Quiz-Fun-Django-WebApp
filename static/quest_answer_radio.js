(function($) {

    // < start of closure

    $ = django.jQuery

    $(document).ready(function() {
    $("input[id$='is_correct']").click(function() {
       $("input[id$='is_correct']").not($(this)).prop('checked', false);

    });


    $("[name='_save']").click(function(event) {
        if ($("input[id$='is_correct']:checked").length == 0) {
            event.preventDefault();
            alert("You must select at least one correct answer!!");
        }
    });

    });
})(django.jQuery);

(function($) {

    // < start of closure

    $ = django.jQuery

    $(document).ready(function() {
    $("input[id$='is_correct']").click(function() {
       $("input[id$='is_correct']").not($(this)).prop('checked', false);

    });


    });
})(django.jQuery);

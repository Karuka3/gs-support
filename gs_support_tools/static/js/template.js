$(document).ready(function () {
    $('#add_text').keydown(function (e) {
        if (e.keyCode == 13 && e.shiftKey) {
            $('form[name="f"]').attr('action', 'add')
            $('form[name="f"]').submit();
        }
    });

    $('.txt').longpress(function () {
        var id = $(this).attr("template_id");
        $('#id').val(id);
        $('form[name="f"]').attr('action', 'delete');
        $('form[name="f"]').submit();
    },
        2000
    );

    $('.txt').dblclick(function () {
        var id = $(this).attr("template_id");
        if ($('#edit_txt_' + id).is(':visible')) {
            $('#edit_txt_' + id).hide();
            $('#template_' + id).show();
        } else {
            $('#edit_txt_' + id).show();
            $('#template_' + id).hide();
        }
    });

    $('textarea[name="edit_txt"]').keydown(function (e) {
        if (e.keyCode == 13 && e.shiftKey) {
            var id = $(this).attr("template_id");
            $('#id').val(id);
            var text = $(this).val();
            $('#text').val(text)
            $('form[name="f"]').attr('action', 'edit');
            $('form[name="f"]').submit();
        }
    });

    $('.txt').on('click', function () {
        var text = $(this).text();
        $(this).append('<textarea class="clipbtextarea">' + text + '</textarea>');
        $('.clipbtextarea').select();
        document.execCommand('Copy');
        $('.clipbtextarea').remove();
    })
})
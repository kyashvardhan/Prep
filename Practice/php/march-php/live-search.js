jQuery(document).ready(function($) {
    $('#live-search-input').on('keyup', function() {
        var query = $(this).val();
        $.ajax({
            url: liveSearch.ajax_url,
            type: 'POST',
            data: {
                action: 'live_search',
                query: query
            },
            success: function(data) {
                var output = '<ul>';
                $.each(data, function(index, post) {
                    output += '<li><a href="'+ post.link +'">'+ post.title +'</a></li>';
                });
                output += '</ul>';
                $('#live-search-results').html(output);
            }
        });
    });
});

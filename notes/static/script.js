function elect_note(elect, pre_class){
            elect.attr('class', null);
            elect.addClass(pre_class == 'elected' ? 'unelected' : 'elected');
            elect.text(pre_class == 'elected' ? 'Unelected' : 'Elected');
        }
        function truncate_words(str, qtywords) {
            if (str.split(' ').length < qtywords)
                return str;
            return str.split(' ', qtywords).join(' ') + ' ...';
        }
        function render_notes(data) {
            if (data['status'] == 'ok') {
                $('.note, #content_message').detach();
                if (data['data'].length > 0){
                    for (i=0; i < data['data'].length; i++){
                        title = data['data'][i]['title'];
                        id = data['data'][i]['id'];
                        category = data['data'][i]['category'];
                        description = data['data'][i]['description'];
                        is_elected = data['data'][i]['elect'];
                        created = data['data'][i]['created'];
                        note = get_note(title, id, category, description, created, is_elected);
                        note.appendTo('#content');
                    }
                }
                else{
                    $('<span/>', {id:'content_message', text: "No search results found"}).appendTo('#content');
                }
            }
        }
        function get_note(title, id, category, description, created, is_elected) {
            elect = is_elected == true ? 'Elected' : 'Unelected';
            note = $('<div/>', {class: 'note'});
            $('<h2/>').append($('<a/>', {href: '/notes/detail/'+id, text: title})).appendTo(note);
            $('<span/>', {text: category['title']}).appendTo(note);
            $('<p/>', {text: truncate_words(description, 49)}).appendTo(note);
            $('<span/>', {text: created}).appendTo(note);
            $('<div/>', {'data-id': id, class: 'score'}).append($('<span/>', {class: elect.toLowerCase(), text: elect})).appendTo(note);
            $('<span/>', {'data-id': id, class: 'delete', text: ' Delete'}).appendTo(note);
            return note
        }
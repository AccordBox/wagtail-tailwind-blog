/*
 * vim:sw=4 ts=4 et:
 * Copyright (c) 2015 Torchbox Ltd.
 * felicity@torchbox.com 2015-09-14
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely. This software is provided 'as-is', without any express or implied
 * warranty.
 */

/*
 * Used to initialize Simple MDE when Markdown blocks are used in StreamFields
 */

/*
 * Used to initialize Simple MDE when MarkdownFields are used on a page.
 */


$(document).ready(function() {

    $(".markdown .field-content textarea").each(function(index, elem) {
        var mde = new SimpleMDE({
            element: elem,
            autofocus: false
        });
        mde.render();
    });

});

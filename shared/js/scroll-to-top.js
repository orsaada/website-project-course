/* Unoriginal JS - START
 Taken from: https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
 */

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scrollToTopButton").style.display = "block";
    } else {
        document.getElementById("scrollToTopButton").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

/* Unoriginal JS - START
 Taken from: https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
 */
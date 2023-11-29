const menu = document.querySelector('.side');

menu.addEventListener('click', function (event) {
    const button = document.querySelector('#menu_button');
    if (event.target == button) {
        if (button.className == "fa fa-plus-circle") {
            menu.style = 'position:fixed; left:0;';
            button.className = "fa fa-minus-circle"
        } else if (button.className == "fa fa-minus-circle") {
            menu.style = 'position:fixed; left:-150px;';
            button.className = "fa fa-plus-circle"
        }
    }
})

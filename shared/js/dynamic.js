
//from
function readURL(input) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();

        reader.onload = function (e) {
            let ul = document.getElementById("userupload");
            let li = document.createElement("li");
            // li.style = "width:33.333333%; float:left;";
            let img = document.createElement("img");
            li.appendChild(document.createTextNode(input.files[0].name.substring(0, input.files[0].name.indexOf('.'))));
            ul.appendChild(li);
            li.appendChild(img);
            $(img)
                .attr('src', e.target.result)
                .width(200)
                .height(150);
        };
        reader.readAsDataURL(input.files[0]);
        alert('your photo: "'+input.files[0].name.substring(0, input.files[0].name.indexOf('.'))+'" was uploaded');
    }
}

//from
function openCity(cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("nav-item tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(cityName).style.display = "block";
    //currentTarget.className += " active";
}

// <!--<script>-->
// <!--    $("#search button").ready(function () {-->
// <!--        $("#search button").on("sea", function () {-->
// <!--            let words = $("#search input").val().toLowerCase();-->
// <!--            alert("words");-->
// <!--            pathname = os.path.dirname(sys.argv[0]);-->
// <!--            // console.log(pathname);-->
// <!--            // console.log(words);-->
// <!--            $("#myList li").filter(function () {-->
// <!--                $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)-->
// <!--            });-->
// <!--        });-->
// <!--    });-->
// <!--</script>-->
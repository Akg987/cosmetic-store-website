$(document).ready(function() {
    $("#AddReview").click(function() {
       $("#myModal").show()
        $("#btnclose").click(function() {
            $("#myModal").hide()
        })

    })
    onclicksave()
    $("#searchbackground").hide()
    $("#searchbutton").click(function() {
        $("#searchbackground").show();
        GetData()
    })
    $("#reviews-tab").click(function() {
        getCsrfToken()
        Getcomment()
    })

});
function Getcomment() {
    $.ajax({
        type: "POST",
        url: "http://" + window.location.host + "/homepage/readallAsk/" + productId,
        data: $(".frm").serialize(),
        dataType: 'json',
        beforeSend: function(){
            $(".errorcomment").html("Prossesing...");
        },
        success: function(result){
            $(".errorcomment").html("");
            try {
                if (Array.isArray(result) && result.length > 0) {
                    let trstr = "";
                    result.forEach(item => {
                        let createdDate = new Date(item.Created).toLocaleString(); // Format date
                        trstr += "<tr>" +
                            "<td>" + item.title + "</td>" +
                            "<td>" + item.caption + "</td>" +
                            "<td>" + createdDate + "</td>" +
                        "</tr>";
                    });
                    $(".body-table").html(trstr);
                } else {
                    $(".errorcomment").html("There is no information to display");
                }
            } catch (e) {
                console.log("Error parsing JSON:", e);
                $(".errorcomment").html("A problem has occurred in processing the data");
            }
        },
        error: function(e){
            $(".errorcomment").html("There was a problem receiving the information");
        }
    });
}

function getCsrfToken() {
    let cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        let [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return null;
}


function GetData() {
    $.ajax({
        type: "POST",
        url: "http://" + window.location.host + "/homepage/readallcosmetics/",
        data: $(".frm-getdata").serialize(),
        beforeSend: function() {
            $(".wite").html("Prossesing...");
        },
        success: function(result) {
            $(".wite").html("");

            let obj;
            if (typeof result === "object") {
                obj = result;
            } else {
                try {
                    obj = JSON.parse(result);
                } catch (e) {
                    console.error("Error parsing JSON:", e);
                    return;
                }
            }

            if (obj.length > 0) {
                let content = "";
                for (let item of obj) {
                    content += `
                        <div class="item" style="background-color:#fff;position:relative;border-radius:25px;text-align:center;margin-bottom:40px;">
                            <div class="thumb" style="position: relative;border-radius: 25px;overflow: hidden;">
                                <a href="product-details.html"><img src="/media/${item.fields.image}" alt="${item.fields.title}"></a>
                            </div>
                            <div class="down-content">
                                <span class="category">${item.fields.category}</span>
                                <h4>${item.fields.title}</h4>
                                <a href="product-details.html">view</a>
                        </div>
                        </div>
                `;
                }
                $(".searchresult").html(content);

            } else {
                console.error()
                $(".wite").html("There is no information to display");
            }
        },
        error: function(e) {
            $(".wite").html("There was a problem receiving the information");
            console.error("AJAX error:", e);
        }
    });
}

function onclicksave() {
$(".imggif").on("click", function(){
        var cosmeticId = $(this).data("cosmetic-id");
        $.ajax({
            type: "POST",
            url: "/bookmark/" + cosmeticId + "/",
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.status === 'success') {
                    alert("Cosmetic bookmarked!");
                } else {
                    alert("Failed to bookmark cosmetic.");
                }
            },
            error: function() {
                alert("An error occurred.");
            }
        });
    });
}
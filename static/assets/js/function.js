console.log("working fine");

const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

$("#review-res").hide();

$("#commentForm").submit(function(e){
    e.preventDefault(); // prevent refreshing

    let dt = new Date();
    let time = dt.getDay() + " " + monthNames[dt.getUTCMonth] + ", " + dt.getFullYear();

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(res){
            console.log("Comment saved");

            if(res.bool == true){
                $("#review-res").html("Review added successfully").show()
                $(".high-comment-form").hide()
                $(".add-review").hide()

                let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
                    _html += '<div class="user justify-content-between d-flex">'
                    _html += '<div class="thumb text-center">'
                    _html += '<img src="https://www.shutterstock.com/image-vector/default-avatar-profile-icon-social-600nw-2180848911.jpg" alt=""/>'
                    _html += '<a href="#" class="font-heading text-brand">'+ res.context.user +'</a>'
                    _html += '</div>'

                    _html += '<div class="desc">'
                    _html += '<div class="d-flex justify-content-between mb-10">'
                    _html += '<div class="d-flex align-items-center">'
                    _html += '<span class="font-xs text-muted">'+ time +'</span>'
                    _html += '</div>'

                    for(let i = 1; i <= res.context.rating; i++){
                        _html += '<i class="fa fa-star text-warning"></i>'
                    }

                    _html += '</div>'
                    _html += '<p class="mb-10">'+ res.context.review +'</p>'

                    _html += '</div>'
                    _html += '</div>'
                    _html += '</div>'
                    $(".comment-list").prepend(_html)
            }

            

        }

    })
})
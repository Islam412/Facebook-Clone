$(document).ready(function(){
    $("#post-form").submit(function(e){
        e.preventDefault();  // stop page refresh

        let post_caption = $("#post-caption").val();
        let post_visibility = $("#visibility").val();

        let fileInput = $("#post-thumbnail")[0];
        let file = fileInput.files[0];
        let fileName = file.name;

        // Use FileReader to read the file and create a URL for display
        let reader = new FileReader();
        reader.onload = function(event) {
            // Display the image in the img element
            $("#image-preview").attr("src", event.target.result);
        };
        reader.readAsDataURL(file); // Read the file as a Data URL

        console.log(post_caption);
        console.log(post_visibility);
        console.log(fileName);
        console.log(file);

        let formData = new FormData();
        formData.append("post-caption", post_caption);
        formData.append("post-thumbnail", file, fileName);
        formData.append("visibility", post_visibility);

        $.ajax({
            url: "/create_post/",
            type: "POST",
            dataType: "json",
            data: formData,
            processData: false,
            contentType: false,
        });
    });
});

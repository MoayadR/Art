const form = document.getElementById("editCommentForm");
const textArea = document.getElementsByName("commentText")[0];
form.addEventListener("submit" , (e)=>{
    e.preventDefault();

    if(textArea.value.length)
    {
        form.submit();
    }
    else
    {
        alert("Comment Can't be changed to empty comment!");
    }
})
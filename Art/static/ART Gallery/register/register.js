const form = document.getElementById("userForm");
const emailField = document.getElementById("id_email");


form.addEventListener("submit" , (e)=>{
    e.preventDefault();
    if (emailField.value.length)
    {
        form.submit();
    }
    else
    {
        alert("Please Fill the Email Field!");
    }
})
const form = document.getElementById("form");

form.addEventListener("submit",(e)=>{
    e.preventDefault()
    let reason = document.getElementsByName("reason")[0]
    if(reason.value.length)
    {
        alert("The Report was successfully submitted");
        form.submit()
    }
    else
    {
        alert("Please fill the report");
    }
})
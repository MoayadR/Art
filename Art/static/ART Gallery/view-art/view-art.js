// commentInput;
// commentButton;

// commentDiv;  a.img  span br


var userData
var userProfile

getUserData = async function(){
    return fetch("http://127.0.0.1:8000/api/user/my-id").then(res => res.json()).then((data) => {
        return data
    });
}

getUserProfile = async function(id){
    return fetch("http://127.0.0.1:8000/api/profile-data/"+id).then(res => res.json()).then((data) => {
        return data
    });
}


addComment = async function(){
    if(userData === undefined)
    {
        userData = await getUserData()
        userData = userData[0]
    }

    if(userProfile === undefined)
    {
        userProfile = await getUserProfile(userData["pk"])
        userProfile = userProfile[0]
    }


    console.log(userData);
    console.log(userProfile);


    commentText = commentInput.value
    a = document.createElement("a")


    a.href = "http://127.0.0.1:8000/auth/profile/"
    img = document.createElement("img")
    img.src = "http://127.0.0.1:8000/mediafiles/"+userProfile["fields"]["profile_pic"]
    img.classList.add("me-3" , "mb-3")
    img.classList.add("astyle")
    img.alt = "comment author"

    a.append(img)
   
    commentDiv.append(a)

    span = document.createElement("span")
    span.innerText = commentText
    span.classList.add("mb-3")

    br = document.createElement("br")
    commentDiv.append(span)
    commentDiv.append(br)
}
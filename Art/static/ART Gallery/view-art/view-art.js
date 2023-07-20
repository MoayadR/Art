// commentInput;
// commentButton;

// commentDiv;  a.img  span br

var userData;
var userProfile;

getUserData = async function () {
  return fetch("http://127.0.0.1:8000/api/user/my-id")
    .then((res) => res.json())
    .then((data) => {
      return data;
    });
};

getUserProfile = async function (id) {
  return fetch("http://127.0.0.1:8000/api/profile-data/" + id)
    .then((res) => res.json())
    .then((data) => {
      return data;
    });
};

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

addComment = async function () {
  // getting userData and userProfile to make the comment
  if (userData === undefined) {
    userData = await getUserData();
    userData = userData[0];
  }

  if (userProfile === undefined) {
    userProfile = await getUserProfile(userData["pk"]);
    userProfile = userProfile[0];
  }


  commentText = commentInput.value;
  // Comment Validation

  if(commentText.length == 0)
  {
    return undefined
  }

  // save the comment in the database
  let splitted = location.pathname.split("/");

  data = {
    text: commentText,
    postID: Number(splitted[splitted.length - 1]),
  };

  fetch("http://127.0.0.1:8000/api/comment/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify(data),
  }).then((res) => res);



  // make the comment and make it appear

  a = document.createElement("a");

  a.href = "http://127.0.0.1:8000/auth/profile/";
  img = document.createElement("img");
  img.src =
    "http://127.0.0.1:8000/mediafiles/" + userProfile["fields"]["profile_pic"];
  img.classList.add("me-3", "mb-3");
  img.classList.add("astyle");
  img.alt = "comment author";

  a.append(img);

  commentDiv.append(a);

  span = document.createElement("span");
  span.innerText = commentText;
  span.classList.add("mb-3");

  br = document.createElement("br");
  commentDiv.append(span);
  commentDiv.append(br);

  commentInput.value = ""
};

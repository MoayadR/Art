const bar = document.getElementById("search-bar");
const box = document.getElementById("recommend");
const btn = document.getElementById("search-button");

var values;

getFromDB = function () {
  fetch("http://127.0.0.1:8000/api/tags/")
    .then((response) => response.json())
    .then((data) => setValues(data));
};

setValues = function (data) {
  values = data;
};

getFromDB()

function displayRecommendation(result) {
  var newResult = "";
  for (var i = 0; i < result.length; i++) {
    result[i] = "<li onclick =selectInput(this) >" + result[i] + "</li>";
    newResult += result[i];
  }

  box.innerHTML = "<ul>" + newResult + "</ul>";
}

function selectInput(list){
    bar.value = list.innerHTML
    btn.click()
}

bar.onkeyup = function () {
  var result = [];
  var input = bar.value;
  if (input.length) {
    for (var i = 0; i < values.length; i++) {
      if (values[i].title.includes(input)) {
        result.push(values[i].title);
      }
    }

    displayRecommendation(result);
  } else {
    box.innerHTML = "";
  }
};


const checkBoxSelectors = [
  ...document.querySelectorAll("input[name = 'tags']"),
];
const checkBoxSelectorsNames = [... document.querySelectorAll(".form-check-label")]

// value = id
const recommendationBox = document.querySelector("#recommendTag");
const search = document.querySelector("#searchForTags");
var Tags ;
var selectedTags = [];
const selectedTagsBox = document.querySelector("#SelectedTags")

function getFromDB () {
    return fetch("http://127.0.0.1:8000/api/tags/")
    .then((response) => response.json())
    .then((data) => {
        return data;
    });
};

async function setTags(){
    Tags = await getFromDB();
}

setTags();


search.onkeyup = debounce(()=>{
    let resultTitles = [];
    let searchValue = search.value;

    if(searchValue.length)
    {
        for(let i =0 ; i<Tags.length ; i++)
        {
            if(Tags[i].title.startsWith(searchValue))
            {
                resultTitles.push(Tags[i].title);
            }
        }
        displayRecommendation(resultTitles);
    }
    else
    {
        recommendationBox.innerHTML = ""
    }
   
});

function debounce(cb , delay = 250){
    let timeout;
  
    return () => {
      clearTimeout(timeout);
      timeout = setTimeout(()=>{
        cb()
      } , delay)
    }
  }

  function displayRecommendation(result) {
    var newResult = "";
    for (var i = 0; i < result.length; i++) {
      result[i] = "<li onclick =selectInput(this) >" + result[i] + "</li>";
      newResult += result[i];
    }
  
    recommendationBox.innerHTML = "<ul>" + newResult + "</ul>";
  }


  function findElementByIndex(value , arr){
    for(let i =0 ; i<arr.length ; i++)
    {
        if(value === arr[i])
        {
            return i;
        }
    }
    return -1;
  }

  function deleteFromSelectedInput(button){
    unCheckTheTag(button.currentTarget.innerHTML);
    let index = findElementByIndex(button.currentTarget.innerHTML , selectedTags);
    selectedTags = selectedTags.splice(index , index);
    selectedTagsBox.removeChild(button.currentTarget);
  }

  function unCheckTheTag(tagTitle){
    for(let i =0 ; i<checkBoxSelectors.length ; i++)
    {
        str = checkBoxSelectorsNames[i].innerHTML.trim();
        if(str === tagTitle)
        {
            checkBoxSelectors[i].checked = false;
            return;
        }
    }
  }

  function checkTheTag(tagTitle){
    for(let i =0 ; i<checkBoxSelectors.length ; i++)
    {
        str = checkBoxSelectorsNames[i].innerHTML.trim();
        if(str === tagTitle)
        {
            checkBoxSelectors[i].checked = true;
            return;
        }
    }
  }

  function isInSelectedTags(value){
    for(let i =0 ; i<selectedTags.length ; i++)
    {
        if(selectedTags[i] === value)
        {
            return true;
        }
    }
    return false;
  }

  function selectInput(listItem) // when selected add to buttons div with onclick delete
  {
    
    if(isInSelectedTags(listItem.innerHTML))
    {
        return;
    }

    selectedTags.push(listItem.innerHTML);
    let button = document.createElement("button" );
    button.type = "button";
    button.classList.add("btn");
    button.classList.add("btn-dark");
    button.classList.add("m-2");
    button.innerHTML = listItem.innerHTML;
    button.addEventListener("click" , deleteFromSelectedInput , false  )

    checkTheTag(listItem.innerHTML);

    selectedTagsBox.append(button);
  }
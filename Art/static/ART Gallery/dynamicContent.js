var throttleTimer;
const throttle = (callback, time) => {
  if (throttleTimer) return;
  throttleTimer = true;
  setTimeout(() => {
    callback();
    throttleTimer = false;
  }, time);
};


let currentItems = 0;
const containers = [...document.querySelectorAll("#posts-container")];

function dynamicfeed(){
  throttle(() =>{
    let endOfPage = window.innerHeight + window.pageYOffset >= document.body.offsetHeight;
  if(endOfPage )
  {
    for(let i = currentItems;i<currentItems+5 && i<containers.length ; i++)
  {
    containers[i].style.display = "inline";
  }
  currentItems += 5;
  }
  })
}

window.addEventListener("scroll" ,dynamicfeed )

dynamicfeed()
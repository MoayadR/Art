var throttleTimer;
const throttle = (callback, time = 250) => {
  if (throttleTimer) return;
  throttleTimer = true;
  setTimeout(() => {
    callback();
    throttleTimer = false;
  }, time);
};


let currentItems = 0;
const containers = [...document.querySelectorAll(".posts-container")];

function dynamicfeed(){
  throttle(() =>{
  if((window.innerHeight + window.pageYOffset) >= document.body.offsetHeight -2 )
  {
    for(let i = currentItems;i<currentItems+15 && i<containers.length ; i++)
  {
    containers[i].style.display = "block";
  }
  currentItems += 15;
  }
  })
}

window.addEventListener("scroll" ,dynamicfeed )

dynamicfeed()
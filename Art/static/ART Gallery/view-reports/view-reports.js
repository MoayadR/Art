function banUser(btn){
    let url = 'http://127.0.0.1:8000/api/ban/';
    let data = {'id' : btn.value};
    fetch(url, {method: 'PUT' , body: JSON.stringify(data)}); 
    alert("User Banned Sucessfully!")
}
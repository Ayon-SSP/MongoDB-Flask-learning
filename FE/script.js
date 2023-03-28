

// function retrieveName(e) {
//     e.preventDefault();
//     let id = document.getElementById('name').id;

//     fetch(`http://localhost:3000/${id}`)
//     .then(res => res.json())
//     .then((data) => {
//         // document.getElementById('result').innerHTML = `id : ${data.id} Name : ${data.name} Genre : ${data.email} Game : ${data.password}</li>`
//         document.getElementById('result').innerHTML = `id : ${data.id} Name : ${data.name} Genre : ${data.email} Game : ${data.password}</li>`
//     })
// }



// GET
document.getElementById('formData').addEventListener('submit', retrieveName);
function retrieveName(e) {
    e.preventDefault();
    let id = document.getElementById('id').value

    fetch(`http://127.0.0.1:5000/${id}`)
    .then(res => res.json())
    .then((data) => {
        console.log(data)
        document.getElementById('result').innerHTML = `<li class="list-group-item">id : ${data.id} Name : ${data.name} Genre : ${data.email} Game : ${data.password}</li>`
    })
}


// POST
document.getElementById('postData').addEventListener('submit', postData)

function postData (e) {
    e.preventDefault()

    let id = document.getElementById('postId').value
    let name = document.getElementById('postName').value
    let mail = document.getElementById('postEmail').value
    let password = document.getElementById('postPassword').value

    console.log(id, name, mail, password)

    fetch('http://127.0.0.1:5000/postData', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            'id' : id,
            'name' : name,
            'email' : mail,
            'password' : password
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}
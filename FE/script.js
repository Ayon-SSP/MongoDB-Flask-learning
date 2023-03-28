document.getElementById('formData').addEventListener('submit', retrieveName);

function retrieveName(e) {
    e.preventDefault();
    let id = document.getElementById('name').id;

    fetch(`http://localhost:3000/${id}`)
    .then(res => res.json())
    .then((data) => {
        document.getElementById('result').innerHTML = `id : ${data.id} Name : ${data.name} Genre : ${data.email} Game : ${data.password}</li>`
    })
}
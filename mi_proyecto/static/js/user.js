const button = document.querySelector("#create-user-button"); 

button.addEventListener("click", function(event) { 
    event.preventDefault();

    const form = document.querySelector("#create-user-form"); // Faltaban las comillas en el selector
    const formData = new FormData(form); // "FormData" debe empezar con mayúscula
    const data = {};
    const token = document.querySelector("#csrf_token").value; 

    formData.forEach((value, key) => { // Se corrigió la sintaxis de la arrow function
        data[key] = value; // Se corrigió la sintaxis para asignar valores al objeto
    });

    fetch(USER_CREATE_URL, {
        method: "POST",
        headers: {
            "X-CSRFToken": token,
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })
    .then((res) => res.json())
    .then((value) => {  
        console.log(value); 
    })
    .catch((error) => {
        console.error(error); 
    });
});

document.getElementById('formulario-producto').addEventListener('submit', async function(e) {
    e.preventDefault();

    const evento = document.getElementById('evento').value;
    const precio = document.getElementById('precio').value;
    const fecha = document.getElementById('fecha').value;
    
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch('/productos/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            evento: evento,
            precio: precio,
            fecha: fecha
        })
    });

    if (response.ok) {
        const data = await response.json();
        const newRow = document.createElement('tr');
        newRow.id = 'boleto-' + data.id;
        newRow.innerHTML = `
            <td>${data.evento_name}</td>
            <td>${data.precio}</td>
            <td>${data.fecha}</td>
            <td><button class="btn-eliminar" onclick="eliminarBoleto(${data.id})">Eliminar</button></td>
        `;
        document.querySelector('#tabla-boletos tbody').appendChild(newRow);
    } else {
        alert("Hubo un error al crear el boleto");
    }
});

async function eliminarBoleto(boletoId) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch(`/eliminar_boleto/${boletoId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        }
    });

    if (response.ok) {
        document.getElementById('boleto-' + boletoId).remove();
    } else {
        alert("Hubo un error al eliminar el boleto");
    }
}

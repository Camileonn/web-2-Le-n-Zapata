document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-boleto');
    const mensaje = document.getElementById('mensaje');
    const tablaBoletos = document.getElementById('tabla-boletos');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const formData = new FormData(form);

        try {
            const response = await fetch('/agregar_boleto/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                },
                body: formData,
            });

            const data = await response.json();

            if (response.ok) {
                const newRow = document.createElement('tr');
                newRow.innerHTML = `
                    <td>${data.evento_name}</td>
                    <td>${data.precio}</td>
                    <td>${data.fecha}</td>
                    <td>
                        <button class="btn-eliminar" data-id="${data.id}">Eliminar</button>
                    </td>
                `;
                tablaBoletos.appendChild(newRow);

                mensaje.textContent = 'Boleto agregado correctamente';
                mensaje.style.display = 'block';
                mensaje.style.color = 'green';

                form.reset();
            } else {
                mensaje.textContent = data.error || 'Error al agregar el boleto';
                mensaje.style.display = 'block';
                mensaje.style.color = 'red';
            }

        } catch (error) {
            console.error('Error de conexión:', error);
            mensaje.textContent = 'Error de conexión';
            mensaje.style.display = 'block';
            mensaje.style.color = 'red';
        }
    });

    tablaBoletos.addEventListener('click', async (e) => {
        if (e.target.classList.contains('btn-eliminar')) {
            const boletoId = e.target.getAttribute('data-id');

            try {
                const response = await fetch(`/eliminar_boleto/${boletoId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    },
                });

                const data = await response.json();

                if (response.ok) {
                    e.target.closest('tr').remove();
                    mensaje.textContent = 'Boleto eliminado correctamente';
                    mensaje.style.display = 'block';
                    mensaje.style.color = 'green';
                } else {
                    mensaje.textContent = data.error || 'Error al eliminar el boleto';
                    mensaje.style.display = 'block';
                    mensaje.style.color = 'red';
                }

            } catch (error) {
                console.error('Error de conexión:', error);
                mensaje.textContent = 'Error de conexión';
                mensaje.style.display = 'block';
                mensaje.style.color = 'red';
            }
        }
    });
});

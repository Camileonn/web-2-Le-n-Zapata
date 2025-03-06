document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-evento');
    const mensaje = document.getElementById('mensaje');
    const tablaEventos = document.getElementById('tabla-eventos');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const formData = new FormData(form);

        try {
            const response = await fetch('/agregar_evento/', {
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
                    <td>${data.name}</td>
                    <td>${data.fecha_inicio}</td>
                    <td>${data.fecha_fin}</td>
                    <td>${data.localidad_name}</td>
                    <td>
                        <button class="btn-eliminar" data-id="${data.id}">Eliminar</button>
                    </td>
                `;
                tablaEventos.appendChild(newRow);

                mensaje.textContent = 'Evento agregado correctamente';
                mensaje.style.display = 'block';
                mensaje.style.color = 'green';

                form.reset();
            } else {
                mensaje.textContent = data.error || 'Error al agregar el evento';
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

    tablaEventos.addEventListener('click', async (e) => {
        if (e.target.classList.contains('btn-eliminar')) {
            const eventoId = e.target.getAttribute('data-id');

            try {
                const response = await fetch(`/eliminar_evento/${eventoId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    },
                });

                const data = await response.json();

                if (response.ok) {
                    e.target.closest('tr').remove();
                    mensaje.textContent = 'Evento eliminado correctamente';
                    mensaje.style.display = 'block';
                    mensaje.style.color = 'green';
                } else {
                    mensaje.textContent = data.error || 'Error al eliminar el evento';
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

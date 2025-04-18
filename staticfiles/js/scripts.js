document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    const messagesDiv = document.getElementById('form-messages');

    if (!form || !messagesDiv) {
        console.error('Forma yoki messages div topilmadi!');
        return;
    }

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Sahifani qayta yuklashni oldini olish
        console.log('Forma yuborilmoqda...');

        const formData = new FormData(form);
        const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;
        console.log('CSRF Token:', csrfToken);

        fetch('/', {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken
            },
            body: formData
        })
        .then(response => {
            console.log('Server javobi statusi:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP xatosi! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Serverdan kelgan ma\'lumot:', data);
            messagesDiv.innerHTML = `<div class="alert alert-${data.status}">${data.message}</div>`;
            if (data.status === 'success') {
                form.reset(); // Formani tozalash
                console.log('Forma tozalandi');
            }
            // Xabarni 5 soniyadan so‘ng yo‘qotish
            setTimeout(() => {
                const alert = messagesDiv.querySelector('.alert');
                if (alert) {
                    alert.classList.add('fade-out');
                    setTimeout(() => alert.remove(), 500);
                    console.log('Xabar yo‘qotildi');
                }
            }, 5000);
        })
        .catch(error => {
            console.error('Xato:', error);
            messagesDiv.innerHTML = '<div class="alert alert-danger">Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.</div>';
            setTimeout(() => {
                const alert = messagesDiv.querySelector('.alert');
                if (alert) {
                    alert.classList.add('fade-out');
                    setTimeout(() => alert.remove(), 500);
                }
            }, 5000);
        });
    });
});
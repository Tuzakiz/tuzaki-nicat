const form = document.getElementById('Form-NewsLetter');
const emailInput = document.getElementById('Email-Input');
const mensagem = document.getElementById('mensagem');

form.addEventListener('submit', async(e) => {
    e.preventDefault()};

    const email = emailInput.value;

    try {
        const res = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({Email-Input}).value
        });
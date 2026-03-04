const API = "http://127.0.0.1:8000";

function register() {
    const data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
        role: document.querySelector('input[name="role"]:checked').value
    };

    fetch("http://127.0.0.1:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(async res => {
        const response = await res.json();
        if (!res.ok) throw new Error(response.detail);
        alert("Registered successfully!");
        window.location.href = "login.html";
    })
    .catch(err => alert(err.message));
}

function login() {
    const data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(async res => {
        const response = await res.json();
        if (!res.ok) throw new Error(response.detail);
        localStorage.setItem("token", response.access_token);
        window.location.href = "dashboard.html";
    })
    .catch(err => alert(err.message));
}
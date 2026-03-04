document.addEventListener("DOMContentLoaded", () => {

    const role = localStorage.getItem("role");
    const btn = document.getElementById("createEventBtn");

    if (role !== "organizer") {
        btn.style.display = "none";
    }

});
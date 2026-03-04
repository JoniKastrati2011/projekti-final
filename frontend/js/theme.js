
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {
        document.body.classList.add("light-mode");
    }
});


function setDark() {
    document.body.classList.remove("light-mode");
    localStorage.setItem("theme", "dark");
}


function setLight() {
    document.body.classList.add("light-mode");
    localStorage.setItem("theme", "light");
}
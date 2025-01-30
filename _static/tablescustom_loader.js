document.addEventListener("DOMContentLoaded", function () {
    // Ensure jQuery and DataTables are loaded before tablescustom.js
    console.log("Loading tablescustom.js dynamically...");
    const script = document.createElement("script");
    script.src = "_static/tablescustom.js";
    script.onload = function () {
        console.log("tablescustom.js loaded successfully!");
    };
    document.head.appendChild(script);
});
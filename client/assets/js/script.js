"use strict";

document.querySelector("#summarize").addEventListener("click", summarize);


async function summarize(e){
	e.preventDefault();
	let text = document.querySelector("#text").value;

	// Show the loading GIF
	const loading = document.querySelector("#loading");
	loading.style.display = "block";

	const fetched = await fetch("http://localhost:8000/summarize", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({text})
	});

	const data = await fetched.json();
	const summary = document.querySelector("#summary");
	summary.innerHTML = "";
	summary.innerHTML = data.summary;

	// Hide the loading GIF
	loading.style.display = "none";
}

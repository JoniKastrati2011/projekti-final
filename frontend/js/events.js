fetch("http://127.0.0.1:8000/events/")
  .then(res => res.json())
  .then(events => {
    const container = document.getElementById("eventList");

    events.forEach(e => {
      const card = document.createElement("div");
      card.className = "event-card";
      card.innerHTML = `
        <h3>${e.title}</h3>
        <p><strong>Location:</strong> ${e.location}</p>
        <p><strong>Date:</strong> ${e.date}</p>
        <button class="btn-outline small">Join Event</button>
      `;
      container.appendChild(card);
    });
  });
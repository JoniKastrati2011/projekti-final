document.addEventListener("DOMContentLoaded", () => {


  const statsData = {
    total_volunteers: 210,
    total_events: 12,
    total_hours: 1540,
    monthly_growth: [50, 80, 120, 150, 180, 210],
    categories: {
      labels: ['Environment', 'Education', 'Charity', 'Health'],
      values: [5, 3, 2, 2]
    }
  };


  document.getElementById("totalVolunteers").innerText = statsData.total_volunteers;
  document.getElementById("totalEvents").innerText = statsData.total_events;
  document.getElementById("totalHours").innerText = statsData.total_hours;


  const volunteerCtx = document.getElementById("volunteerChart");

  new Chart(volunteerCtx, {
    type: "line",
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        label: "Volunteers",
        data: statsData.monthly_growth,
        borderColor: "#3b82f6",
        backgroundColor: "rgba(59,130,246,0.2)",
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      responsive: true
    }
  });


  const eventCtx = document.getElementById("eventChart");

  new Chart(eventCtx, {
    type: "doughnut",
    data: {
      labels: statsData.categories.labels,
      datasets: [{
        data: statsData.categories.values,
        backgroundColor: [
          "#22c55e",
          "#3b82f6",
          "#f97316",
          "#ef4444"
        ]
      }]
    },
    options: {
      responsive: true
    }
  });

});
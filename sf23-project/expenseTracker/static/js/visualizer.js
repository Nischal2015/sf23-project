$(document).ready(function () {
  var z = document.getElementById("context_parse");
  var context = JSON.parse(z.innerText);
  z.remove();
  console.log(context);

  var ctx = document.getElementById("myChart1").getContext("2d");
  var barColors = ["red", "green", "blue", "orange", "brown"];

  new Chart(ctx, {
    type: "bar",
    data: {
      datasets: context.graph1.x_values.map((element, i) => {
        return {
          label: element,
          data: [context.graph1.y_values[i]],
          backgroundColor: barColors[i],
        };
      }),
    },
    options: {
      title: {
        display: true,
        text: "Mode of Payment",
      },
    },
  });

  var ctx2 = document.getElementById("myChart2").getContext("2d");
  new Chart(ctx2, {
    type: "doughnut",
    data: {
      labels: context.graph2.x_values,
      datasets: [
        {
          backgroundColor: barColors,
          data: context.graph2.y_values,
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Expense Type",
      },
    },
  });

  var ctx3 = document.getElementById("myChart3").getContext("2d");
  var barColors = [
    "red",
    "green",
    "blue",
    "orange",
    "brown",
    "yellow",
    "purple",
    "pink",
  ];

  new Chart(ctx3, {
    type: "bar",
    data: {
      datasets: context.graph3.x_values.map((element, i) => {
        return {
          label: element,
          data: [context.graph3.y_values[i]],
          backgroundColor: barColors[i],
        };
      }),
    },
    options: {
      title: {
        display: true,
        text: "Category of expenses",
      },
    },
  });

  var ctx4 = document.getElementById("myChart4").getContext("2d");

  new Chart(ctx4, {
    type: "line",
    data: {
      labels: context.graph4.x_values,
      datasets: [
        {
          label: "Amount Spent per day",
          backgroundColor: "rgba(153, 102, 255, 0.5)", //purple
          borderColor: "rgba(153, 102, 255, 1)",
          data: context.graph4.y_values,
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Time Series plot of expense",
      },
    },
  });
});

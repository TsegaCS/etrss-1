const intro = introJs();

intro.setOptions({
  steps: [
    {
      //   element: ".introduction",
      intro: "Welcome! Let's take a quick tour",
    },
    {
      element: ".introduction",
      intro: "This is where we begin",
    },
    {
      element: ".step-one",
      intro: "Start by giving us the coordinates",
    },
    {
      element: ".step-two",
      intro: "You can also use the Interactive Map here",
    },
    {
      element: ".step-three",
      intro: "You can change the map to Satellite View and scroll to zoom..",
    },
    {
      element: ".step-four",
      intro: "Right click on any place inside the map to get the coordinates..",
    },
  ],
});

document
  .querySelector(".take-tour-again")
  .addEventListener("click", function () {
    intro.start();
  });

intro.start();

$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

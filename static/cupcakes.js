const BASE_URL = "http://localhost:5000/api";

//makes a div for each cupcake instance
function makeHTML(cupcake) {
  return `
    <div class="container" data-cupcake-id=${cupcake.id}>
        <li>
            ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
            <button id="delete-btn">Remove</button>
        </li>
        <img class="cupcake-img" src="${cupcake.image}"
        alt="no Image provided">
    </div>`;
}

//lists all cupcakes available
async function showAllCupcakes() {
  const res = await axios.get(`${BASE_URL}/cupcakes`);

  for (let cupcake of res.data.cupcakes) {
    let availableCupcake = $(makeHTML(cupcake));
    $("#cupcake-list").append(availableCupcake);
  }
}

// the api works but i cannot implement it using JS
//returns searched cupcakes
// $(".search-form").on("submit", async function (evt) {
//   evt.preventDefault();

//   const res = await axios.get(`${BASE_URL}/cupcakes/search`);
//   console.log(res.data.cupcakes);
//   // listOfCupcakes = res.data.cupcakes;
//   // if (listOfCupcakes.length !== 0) {
//   //   for (let cupcake of listOfCupcakes) {
//   //     let searchCupcakes = $(makeHTML(cupcake));
//   //     $(".looked-up-list").append(searchCupcakes);
//   //   }
//   // }
// });

//makes a new cupcake
$("#new-cupcake-form").on("submit", async function (evt) {
  evt.preventDefault();

  let flavor = $("#flavor").val();
  let rating = $("#rating").val();
  let size = $("#size").val();
  let image = $("#image").val();

  let data = {
    flavor,
    rating,
    size,
    image,
  };

  const newCupcakeRes = await axios.post(`${BASE_URL}/cupcakes`, data);

  let newCupcake = $(makeHTML(newCupcakeRes.data.cupcake));
  $("#cupcake-list").append(newCupcake);
  $("#cupcake-form").trigger("reset");
});

//deletes cupcake
$("#cupcake-list").on("click", "#delete-btn", async function (evt) {
  evt.preventDefault();

  let $cupcake = $(evt.target).closest("div");
  let cupcakeid = $cupcake.attr("data-cupcake-id");

  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeid}`);
  $cupcake.remove();
});

$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
  let $cupcake = $(evt.target).closest("div");
  let cupcakeId = $cupcake.attr("data-cupcake-id");

  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
  $cupcake.remove();
});
showAllCupcakes();

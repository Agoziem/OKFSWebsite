// ---------------------------------------------------------
// UI for the Access Cards
// ---------------------------------------------------------
const download_btn = document.getElementById("download_btn");
const spinner = download_btn.querySelector(".spinner-border");
const student_card_container = document.getElementById(
  "student_card_container"
);
const download_back_btn = document.getElementById("download_back_btn");
const spinner2 = download_back_btn.querySelector(".spinner-border");
const student_card_back_container = document.getElementById(
  "student_card_back_container"
);
let element = student_card_container;
const regenerate_btn = document.getElementById("regenerate_btn");

// ---------------------------------------------------------
// event listener for the Front Card
// ---------------------------------------------------------
download_btn.addEventListener("click", () => {
  // Show spinner
  spinner.classList.remove("d-none");
  download_btn.disabled = true;
  // Call the function that generates the PDF
  element = student_card_container;
  myFunction()
    .then(() => {
      // PDF generation is finished, stop spinner
      spinner.classList.add("d-none");
      download_btn.disabled = false;
      // Add your code to start downloading the PDF here
    })
    .catch((error) => {
      // PDF generation encountered an error, display error message
      spinner.classList.add("d-none");
      download_btn.disabled = false;
      download_btn.innerHTML = "Error: " + error.message;
    });
});

// ---------------------------------------------------------
// event listener for the Back Card
// ---------------------------------------------------------
download_back_btn.addEventListener("click", () => {
  // Show spinner
  spinner2.classList.remove("d-none");
  download_back_btn.disabled = true;
  // Call the function that generates the PDF
  element = student_card_back_container;
  myFunction()
    .then(() => {
      // PDF generation is finished, stop spinner
      spinner2.classList.add("d-none");
      download_back_btn.disabled = false;
      // Add your code to start downloading the PDF here
    })
    .catch((error) => {
      // PDF generation encountered an error, display error message
      spinner2.classList.add("d-none");
      download_back_btn.disabled = false;
      download_back_btn.innerHTML = "Error: " + error.message;
    });
});

// ---------------------------------------------------------
// function to generate the PDF
// ---------------------------------------------------------
function myFunction(e) {
  if (!element) {
    console.error("Target element not found!");
    return;
}
  var opt = {
    margin: [0, 0],
    filename: "OKFS Access Cards" + ".pdf",
    image: { type: "jpeg", quality: 1 },
    html2canvas: {
      scale: 4,
      width: element.offsetWidth,
      height: element.offsetHeight,
      useCORS: true,
      allowTaint: true,
    },
    jsPDF: {
      unit: "px",
      format: [element.offsetWidth, element.offsetHeight],
      orientation: "Portrait",
      hotfixes: ["px_scaling"],
    },
  };
  // New Promise-based usage:
  return new Promise((resolve, reject) => {
    html2pdf()
      .set(opt)
      .from(element)
      .save()
      .then(() => {
        // PDF generation is complete, resolve the promise
        resolve();
      })
      .catch((error) => {
        // PDF generation encountered an error, reject the promise with the error
        reject(error);
      });
  });
}

// ---------------------------------------------------------
// event listener for the regenerate button
// ---------------------------------------------------------
regenerate_btn.addEventListener("click", regeneratePins);

// ---------------------------------------------------------
// regenerate the student Pins by clicking the regenerate button and calling an API
// ---------------------------------------------------------
async function regeneratePins() {
  const regenerate_btn = document.getElementById("regenerate_btn");
  const regenerate_spinner = regenerate_btn.querySelector(
    ".regenerate_spinner"
  );
  regenerate_spinner.classList.remove("d-none");
  regenerate_btn.disabled = true;
  try {
    const response = await fetch("/regeneratepins/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    });
    if (response.ok) {
      const data = await response.json();
      regenerate_spinner.classList.add("d-none");
      regenerate_btn.disabled = false;
      displayalert("success", data.message);
    } else {
      const error = await response.json();
      throw new Error(error.message);
    }
  } catch (error) {
    regenerate_spinner.classList.add("d-none");
    regenerate_btn.disabled = false;
    displayalert("danger", "Error Regenerating Pins " + error.message);
  }
}

// ---------------------------------------------------------
// display Alert when the regenerate button is clicked
// ---------------------------------------------------------
function displayalert(type, message) {
  const alertdiv = document.createElement("div");
  alertdiv.classList.add(
    "alert",
    type === "success" ? "alert-success" : "alert-danger",
    "d-flex",
    "align-items-center",
    "mt-3"
  );
  alertdiv.setAttribute("role", "alert");
  alertdiv.innerHTML = `
                        <i class="fa-solid fa-circle-check me-2"></i>
                        <div>
                           ${message}
                        </div>
                        `;
  // check for Screen Size and append alert message to the appropriate container
  const alertcontainer = document.getElementById("alertcontainer");
  alertcontainer.appendChild(alertdiv);
  setTimeout(() => {
    alertdiv.remove();
  }, 5000);
}

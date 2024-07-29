import { showSpinner, hideSpinner } from "../../utils/displayspinner.js";

// -----------------------------------------------------
// getting and updating from the server
// ------------------------------------------------------
async function getstudentdata(classdata) {
  showSpinner("updatesubjectspinner", "subjectbtnmessage", "Loading...");
  const response = await fetch(`/TMS/getstudentresults/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(classdata),
  });
  const data = await response.json();
  hideSpinner("updatesubjectspinner", "subjectbtnmessage", "load Results");
  return data;
}

// ---------------------------------------------------
// function to get Student Annual Result
// ---------------------------------------------------
async function getannualresultdata(classdata) {
  showSpinner("updatesubjectspinner", "subjectbtnmessage", "Loading...");
  console.log(classdata);
  const response = await fetch(`/TMS/annualresultcomputation/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(classdata),
  });
  const data = await response.json();
  hideSpinner("updatesubjectspinner", "subjectbtnmessage", "load Results");
  return data;
}

// -----------------------------------------------------
// Function to get Class Annual Result
// ------------------------------------------------------
async function getannualclassresult(classdata) {
  const response = await fetch(`/TMS/annualclassresultcomputation/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(classdata),
  });
  const data = await response.json();
  return data;
}

// -----------------------------------------------------
// Function to update student result
// ------------------------------------------------------
function updatestudentresult(
  formDataObject,
  classdata,
  readJsonFromFile,
  displayalert
) {
  const fullresultdata = {
    formDataObject,
    classdata,
  };
  showSpinner("updatespinner", "btnmessage", "Updating...");
  fetch(`/TMS/updatestudentresults/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(fullresultdata),
  })
    .then((response) => response.json())
    .then((data) => {
      hideSpinner("updatespinner", "btnmessage", "Update");
      readJsonFromFile();
      const type = "alert-success";
      const message = data;
      displayalert(type, message);
    })
    .catch((error) => console.error("Error:", error));
}

// -----------------------------------------------------
// Function to submit all student result
// ------------------------------------------------------
function submitallstudentresult(url, data, classdata, displayalert) {
  const resulttosubmit = {
    data,
    classdata,
  };
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(resulttosubmit),
  })
    .then((response) => response.json())
    .then((data) => {
      const type = "alert-success";
      const message = data;
      displayalert(type, message);
    })
    .catch((error) => console.error("Error:", error));
}

// ---------------------------------------------------
// function to get Student Result
// ---------------------------------------------------
async function getstudentresult(classdata) {
  const response = await fetch(`/TMS/getstudentsubjecttotals/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(classdata),
  });
  const data = await response.json();
  return data;
}

// ---------------------------------------------------
// function to publish Student Result
// ---------------------------------------------------
function publishstudentresult(url, data, classdata, displayalert) {
  const fulldata = {
    data,
    classdata,
  };

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(fulldata),
  })
    .then((response) => response.json())
    .then((data) => {
      const type = "alert-success";
      const message = data;
      displayalert(type, message);
    })
    .catch((error) => console.error("Error:", error));
}

export {
  getstudentdata,
  getannualresultdata,
  getannualclassresult,
  updatestudentresult,
  submitallstudentresult,
  getstudentresult,
  publishstudentresult,
};

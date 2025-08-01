import { showSpinner, hideSpinner } from "../../utils/displayspinner.js";

// -----------------------------------------------------
// function to get Subject Students Termly Results
// ------------------------------------------------------
async function getstudentdata(classdata) {
  if (
    classdata.selectedTerm === "" ||
    classdata.studentsubject === "" ||
    classdata.selectedAcademicSession === "" ||
    classdata.studentclass === ""
  ) {
    return;
  }
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
// function to get Subject Students Annual Results
// ---------------------------------------------------
async function getannualresultdata(classdata) {
  if (
    classdata.studentclass === "" ||
    classdata.studentsubject === "" ||
    classdata.selectedAcademicSession === ""
  ) {
    return;
  }
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
// Function to submit all Subject Student result
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
// function to get Class Students Result
// ---------------------------------------------------
async function getstudentresult(classdata) {
  if (
    classdata.studentclass === "" ||
    classdata.selectedTerm === "" ||
    classdata.selectedAcademicSession === ""
  ) {
    return;
  }
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
// function to publish Class Students Result
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


// -----------------------------------------------------
// Function to get Class Students Annual Result
// ------------------------------------------------------
async function getannualclassresult(classdata) {
  if (
    classdata.studentclass === "" ||
    classdata.selectedTerm === "" ||
    classdata.selectedAcademicSession === ""
  ) {
    return;
  }
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


export {
  getstudentdata,
  getannualresultdata,
  getannualclassresult,
  updatestudentresult,
  submitallstudentresult,
  getstudentresult,
  publishstudentresult,
};

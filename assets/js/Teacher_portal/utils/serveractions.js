import { showSpinner, hideSpinner } from "../../utils/displayspinner.js";

async function parseJsonResponse(response) {
  const contentType = response.headers.get("content-type") || "";
  if (!response.ok) {
    throw new Error(`Request failed (${response.status})`);
  }
  if (!contentType.includes("application/json")) {
    throw new Error("Server returned a non-JSON response");
  }
  return response.json();
}

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
  try {
    const response = await fetch(`/TMS/getstudentresults/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(classdata),
    });
    return await parseJsonResponse(response);
  } finally {
    hideSpinner("updatesubjectspinner", "subjectbtnmessage", "load Results");
  }
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
  try {
    const response = await fetch(`/TMS/annualresultcomputation/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(classdata),
    });
    return await parseJsonResponse(response);
  } finally {
    hideSpinner("updatesubjectspinner", "subjectbtnmessage", "load Results");
  }
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
    .then((response) => parseJsonResponse(response))
    .then((data) => {
      readJsonFromFile();
      displayalert("alert-success", data);
    })
    .catch((error) => {
      console.error("Error:", error);
      displayalert(
        "alert-danger",
        "Failed to update result. Please try again."
      );
    })
    .finally(() => {
      hideSpinner("updatespinner", "btnmessage", "Update");
    });
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
    .then((response) => parseJsonResponse(response))
    .then((data) => {
      displayalert("alert-success", data);
    })
    .catch((error) => {
      console.error("Error:", error);
      displayalert(
        "alert-danger",
        "Failed to publish/unpublish results. Please try again."
      );
    });
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
  return parseJsonResponse(response);
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
    .then((response) => parseJsonResponse(response))
    .then((data) => {
      displayalert("alert-success", data);
    })
    .catch((error) => {
      console.error("Error:", error);
      displayalert(
        "alert-danger",
        "Failed to publish/unpublish class results. Please try again."
      );
    });
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
  return parseJsonResponse(response);
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

// -----------------------------------------------------
// getting and updating from the server
// ------------------------------------------------------
async function getstudentdata(classdata) {
  const response = await fetch(`/TMS/getstudentresults/`, {
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
function submitallstudentresult(url,data, classdata, displayalert) {
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
function publishstudentresult(url,data, classdata,displayalert) {
  const fulldata = {
      data,
      classdata
  }
  fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
      },
      body: JSON.stringify(fulldata)
  })
      .then(response => response.json())
      .then(data => {
          const type = 'alert-success'
          const message = data
          displayalert(type, message)
      })
      .catch(error => console.error('Error:', error));
}

export {
  getstudentdata,
  updatestudentresult,
  submitallstudentresult,
  getstudentresult,
  publishstudentresult
};
import StudentDataHandler from "./utils/StudentResulthandler.js";
import StudentResultDatatable from "./datatable/StudentResultDatatable.js";
import {
  getstudentdata,
  updatestudentresult,
  submitallstudentresult,
} from "./utils/serveractions.js";
import * as XLSX from "https://cdn.sheetjs.com/xlsx-latest/package/xlsx.mjs";

// ---------------------------------------------------
// DOM elements
// ---------------------------------------------------
const inputStudentResultModal = document.querySelector(
  "#inputStudentResultModal"
);
const inputform = inputStudentResultModal.querySelector(
  "#inputStudentResultform"
);
const getstudentresultform = document.querySelector("#getstudentresultform");
const rowcheckboxes = document.querySelector(".rowgroup");
const subjectselect = getstudentresultform.querySelector("select");
const classinput = getstudentresultform.querySelector("input");
const termSelect = document.getElementById("termSelect");
const Examforminput = document.querySelector("#Examinput");
const academicSessionSelect = document.getElementById("academicSessionSelect");
const alertcontainer1 = document.querySelector(".alertcontainer1"); // for small screen
const alertcontainer2 = document.querySelector(".alertcontainer2"); // for large screen

document.querySelectorAll(".publishbtn").forEach((btn) => {
  btn.addEventListener("click", exportTableToJSON);
});

// Add Excel export button listeners
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".export-excel-btn").forEach((btn) => {
    if (btn.textContent.includes("Print to Excel")) {
      btn.addEventListener("click", exportToExcel);
    }
  });
});

// ---------------------------------------------------
// Global variables
// ---------------------------------------------------
let classdata = {
  studentclass: classinput.value,
};

let studentResult = [];
let state;

// ---------------------------------------------------
// Event listeners
// ---------------------------------------------------

// get student result
document.addEventListener("DOMContentLoaded", () => {
  getstudentresultform.addEventListener("submit", (e) => {
    e.preventDefault();
    saveformSelections();
  });
});

// update student result
document.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("inputStudentResultform")
    .addEventListener("submit", (e) => {
      e.preventDefault();
      const formData = new FormData(inputform);
      const formDataObject = {};
      formData.forEach((value, key) => {
        formDataObject[key] = value;
      });
      classdata.studentsubject =
        subjectselect.options[subjectselect.selectedIndex].value;
      (classdata.selectedTerm = termSelect.value),
        (classdata.selectedAcademicSession = academicSessionSelect.value),
        updatestudentresult(
          formDataObject,
          classdata,
          readJsonFromFile,
          displayalert
        );
      $(inputStudentResultModal).modal("hide");
    });
});

// load saved selection
document.addEventListener("DOMContentLoaded", () => {
  loadsavedSelection();
});

// ---------------------------------------------------
// Function to save selected values to localStorage
// ---------------------------------------------------
function saveformSelections() {
  localStorage.setItem("selectedresultTerm", termSelect.value);
  localStorage.setItem(
    "selectedresultAcademicSession",
    academicSessionSelect.value
  );
  localStorage.setItem("selectedresultsubject", subjectselect.value);
  classdata.selectedTerm = termSelect.value;
  classdata.selectedAcademicSession = academicSessionSelect.value;
  classdata.studentsubject =
    subjectselect.options[subjectselect.selectedIndex].value;

  // const examClasses = [
  //   "Jss3A",
  //   "Jss3B",
  //   "Jss3C",
  //   "Jss3D",
  //   "SS3 Art",
  //   "Ss3 Science",
  // ];

  // if (examClasses.includes(classinput.value)) {
  //   Examforminput.innerHTML = `
  //   <label for="Exam" class="form-label">Exam Score (100)</label>
  //   <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="100">
  // `;
  // } else {
  //   Examforminput.innerHTML = `
  //   <label for="Exam" class="form-label">Exam Score (60)</label>
  //   <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="60">
  // `;
  // }
  readJsonFromFile();
}

// -----------------------------------------------------
// Function to load saved values from localStorage
// ------------------------------------------------------
function loadsavedSelection() {
  const savedTerm = localStorage.getItem("selectedresultTerm");
  const savedAcademicSession = localStorage.getItem(
    "selectedresultAcademicSession"
  );
  const savedsubject = localStorage.getItem("selectedresultsubject");

  if (savedTerm !== null) {
    termSelect.value = savedTerm;
    classdata.selectedTerm = termSelect.value;
  } else {
    classdata.selectedTerm = termSelect.value;
  }

  if (savedAcademicSession !== null) {
    academicSessionSelect.value = savedAcademicSession;
    classdata.selectedAcademicSession = academicSessionSelect.value;
  } else {
    classdata.selectedAcademicSession = academicSessionSelect.value;
  }

  if (savedsubject !== null) {
    subjectselect.value = savedsubject;
    classdata.studentsubject = subjectselect.value;
  } else {
    classdata.studentsubject = subjectselect.value;
  }

  // const examClasses = [
  //   "Jss3A",
  //   "Jss3B",
  //   "Jss3C",
  //   "Jss3D",
  //   "SS3 Art",
  //   "Ss3 Science",
  // ];

  // if (examClasses.includes(classinput.value)) {
  //   Examforminput.innerHTML = `
  //   <label for="Exam" class="form-label">Exam Score (100)</label>
  //   <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="100">
  // `;
  // } else {
  //   Examforminput.innerHTML = `
  //   <label for="Exam" class="form-label">Exam Score (60)</label>
  //   <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="60">
  // `;
  // }

  readJsonFromFile();
}

// -----------------------------------------------------
// Function to read JSON file and populate the table
// ------------------------------------------------------
async function readJsonFromFile() {
  try {
    const jsonData = await getstudentdata(classdata);
    const studentHandler = new StudentDataHandler(jsonData);
    const studentsWithCalculatedFields = studentHandler.getStudents();
    studentResult = studentsWithCalculatedFields;
    updateResultBadge("update", studentsWithCalculatedFields[0]);
    populatetable(studentsWithCalculatedFields);
    const dataTable = new StudentResultDatatable(
      inputStudentResultModal,
      inputform
    );
  } catch (error) {
    console.error("Error reading JSON file:", error);
  }
}

// -----------------------------------------------------
// Function to populate the table with data
// ------------------------------------------------------
function populatetable(tabledata) {
  const tbody = document.querySelector("#dataTable").lastElementChild;
  tbody.innerHTML = tabledata.length
    ? tabledata
        .map(
          (data, index) => `
        <tr data-rowindex='${index + 1}'>
            <td>${index + 1}</td>
            <td class="text-primary text-uppercase"><a class="inputdetailsformmodelbtn text-decoration-none" style="cursor:pointer">${
              data.Name
            }</a></td>
            <td>${data["1sttest"]}</td>
            <td>${data["1stAss"]}</td>
            <td>${data["Project"]}</td>
            <td>${data["MidTermTest"]}</td>
            <td>${data["2ndTest"]}</td>
            <td>${data["2ndAss"]}</td>
            <td>${data["CA"] || "-"}</td>
            <td>${data["Exam"]}</td> 
            <td>${data["Total"] || "-"}</td>
            <td>${data["Grade"] || "-"}</td>
            <td>${data["Position"] || "-"}</td>
            <td>${data["Remarks"] || "-"}</td>
            <td>${data["studentID"]}</td>
        </tr>`
        )
        .join("")
    : `<tr data-rowindex="1">
           <td colspan="15" class="text-center">No Student Records Found</td>
       </tr>`;
}

// -----------------------------------------------------
// Function to export table data to JSON
// ------------------------------------------------------
function exportTableToJSON() {
  const url =
    state === "published"
      ? "/TMS/unpublishstudentresults/"
      : "/TMS/submitallstudentresult/";
  const datatosubmit = studentResult;
  classdata.studentsubject =
    subjectselect.options[subjectselect.selectedIndex].value;
  classdata.studentclass = classinput.value;
  (classdata.selectedTerm = termSelect.value),
    (classdata.selectedAcademicSession = academicSessionSelect.value),
    submitallstudentresult(url, datatosubmit, classdata, displayalert);
  updateResultBadge("setbadge", datatosubmit[0]);
}

// -----------------------------------------------------
// Function to display alert messages
// ------------------------------------------------------
function displayalert(type, message) {
  const alertdiv = document.createElement("div");
  alertdiv.classList.add(
    "alert",
    `${type}`,
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
  if (window.innerWidth < 768) {
    alertcontainer1.appendChild(alertdiv);
  } else {
    alertcontainer2.appendChild(alertdiv);
  }
  setTimeout(() => {
    alertdiv.remove();
  }, 5000);
}

// -----------------------------------------------------
// Export to Excel Handler
// -----------------------------------------------------
function exportToExcel() {
  if (!studentResult.length) {
    displayalert("alert-warning", "No data to export");
    return;
  }

  try {
    // Prepare data for Excel
    const exportData = studentResult.map((student, index) => {
      return {
        "S/N": index + 1,
        Name: student.Name,
        "1st Test": student["1sttest"] || "-",
        "1st Assignment": student["1stAss"] || "-",
        Project: student["Project"] || "-",
        "Mid Term Test": student["MidTermTest"] || "-",
        "2nd Test": student["2ndTest"] || "-",
        "2nd Assignment": student["2ndAss"] || "-",
        CA: student["CA"] || "-",
        Exam: student["Exam"] || "-",
        Total: student["Total"] || "-",
        Grade: student["Grade"] || "-",
        Position: student["Position"] || "-",
        Remarks: student["Remarks"] || "-",
      };
    });

    // Create worksheet
    const ws = XLSX.utils.json_to_sheet(exportData);

    // Set column widths
    ws["!cols"] = [
      { wch: 5 }, // S/N
      { wch: 25 }, // Name
      { wch: 10 }, // 1st Test
      { wch: 15 }, // 1st Assignment
      { wch: 10 }, // Project
      { wch: 15 }, // Mid Term Test
      { wch: 10 }, // 2nd Test
      { wch: 15 }, // 2nd Assignment
      { wch: 8 }, // CA
      { wch: 8 }, // Exam
      { wch: 8 }, // Total
      { wch: 8 }, // Grade
      { wch: 10 }, // Position
      { wch: 15 }, // Remarks
    ];

    // Create workbook
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Results");

    // Generate filename
    const subject =
      subjectselect.options[subjectselect.selectedIndex].text || "Subject";
    const filename =
      `${classinput.value}_${subject}_${termSelect.value}_${academicSessionSelect.value}_Results.xlsx`.replace(
        /\//g,
        "-"
      );

    // Save file
    XLSX.writeFile(wb, filename);

    displayalert("alert-success", "Results exported successfully!");
  } catch (error) {
    console.error("Export error:", error);
    displayalert("alert-danger", "Failed to export results");
  }
}

// ------------------------------------------------------------------------------------------------
// function to update the result badge
// ------------------------------------------------------------------------------------------------
function updateResultBadge(type, studentresult) {
  if (type === "setbadge") {
    studentresult.published = !studentresult.published;
  }
  state = studentresult.published ? "published" : "unpublished";
  const badge = document.querySelector("#resultbadge");
  studentresult.published
    ? badge.classList.replace("bg-secondary", "bg-success")
    : badge.classList.replace("bg-success", "bg-secondary");
  badge.innerHTML = studentresult.published
    ? `<i class="fa-solid fa-check-circle me-2"></i>
       Result Published`
    : `<i class="fa-solid fa-circle-plus me-2"></i>
       Result Not Published`;

  document.querySelectorAll(".publishbtn").forEach((btn) => {
    btn.innerHTML = studentresult.published
      ? `UnPublish Result <i class="fa-solid fa-right-from-bracket ms-2"></i>`
      : `Publish Result <i class='fa-solid fa-left-from-bracket ms-2'></i>`;
  });
}

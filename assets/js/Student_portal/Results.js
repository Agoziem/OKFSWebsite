const classSelect = document.getElementById("class");
const sessionSelect = document.getElementById("AcademicSession");
const StudentsSelect = document.getElementById("Students");
const userInput = document.querySelector("#studentId");

userInput.addEventListener("input", processinput);
function processinput() {
  // Get the input element
  const processedValue = userInput.value.toLowerCase().replace(/\s/g, "");
  userInput.value = processedValue;
}

sessionSelect?.addEventListener("input", populateClass);
classSelect?.addEventListener("input", populateClass);

function populateClass() {
  const classname = classSelect.value;
  const sessionid = sessionSelect.value;
  if (classname && sessionid) {
    fetch(`/SRMS/${classname}/${sessionid}`)
      .then((response) => response.json())
      .then((data) => {
        StudentsSelect.innerHTML = "";
        data.forEach((student) => {
          const option = document.createElement("option");
          option.value = student.student_name;
          option.textContent = student.student_name;
          StudentsSelect.appendChild(option);
        });
      })
      .catch((error) => console.error(error));
  } else {
    StudentsSelect.innerHTML = "";
  }
}

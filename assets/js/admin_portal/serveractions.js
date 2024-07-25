// --------------------------------------------
// function for admin get Class Published Results
// --------------------------------------------
const getClassPublishedResults = async (
  resultcredentials,
  displayResultPublishedbadge,
  displaypublishedResult
) => {
  try {
    const response = await fetch("/TMS/getclasspublishedResults/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(resultcredentials),
    });
    const data = await response.json();
    if (response.ok) {
      displayResultPublishedbadge(data);
      displaypublishedResult(data);
    } else {
      throw new Error(data.error);
    }
  } catch (error) {
    console.log(error);
  }
};

export { getClassPublishedResults };

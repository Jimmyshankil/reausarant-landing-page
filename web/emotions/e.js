// Array to store scent data
let scents = [];

// Function to add a scent
function addScent(scent, feeling) {
  // Create an object to store the scent and feeling
  let scentEntry = {
    scent: scent,
    feeling: feeling
  };

  // Add the object to the scents array
  scents.push(scentEntry);
}

// Function to assign a mood score based on the feeling
function assignMoodScore(feeling) {
  let score;

  // Simple scoring based on feelings
  if (feeling.toLowerCase() === "calm") {
    score = 8;
  } else if (feeling.toLowerCase() === "energized") {
    score = 9;
  } else if (feeling.toLowerCase() === "grossed out") {
    score = 2;
  } else {
    score = 5; // Neutral score for other feelings
  }

  return score;
}

// Function to analyze mood data
function analyzeMoods() {
  if (scents.length === 0) {
    return null; // No data to analyze
  }

  let totalScore = 0;
  let bestScent = "";
  let worstScent = "";
  let highestScore = -1; // Start with the lowest possible score
  let lowestScore = 11; // Start with the highest possible score

  // Loop through each scent to calculate scores
  for (let i = 0; i < scents.length; i++) {
    let entry = scents[i];
    let score = assignMoodScore(entry.feeling);
    totalScore += score;

    // Check if the current score is the best
    if (score > highestScore) {
      highestScore = score;
      bestScent = entry.scent;
    }

    // Check if the current score is the worst
    if (score < lowestScore) {
      lowestScore = score;
      worstScent = entry.scent;
    }
  }

  // Calculate the average mood score
  let averageScore = totalScore / scents.length;

  // Return the analysis result
  return {
    average: averageScore.toFixed(1), // Round to 1 decimal place
    bestScent: bestScent,
    worstScent: worstScent
  };
}

// Function to display results on the webpage
function displayResults(analysis) {
  // Get the results div
  let resultsDiv = document.getElementById("results");

  // If there is no data to show
  if (!analysis) {
    resultsDiv.style.display = "none";
    alert("No scent data available to analyze!");
    return;
  }

  // Show the results
  resultsDiv.style.display = "block";
  resultsDiv.innerHTML = `
    <p><strong>Average Mood Score:</strong> ${analysis.average}</p>
    <p><strong>Best Scent of the Day:</strong> ${analysis.bestScent}</p>
    <p><strong>Worst Scent of the Day:</strong> ${analysis.worstScent}</p>
  `;
}

// Function to handle adding a scent
function handleAddScent() {
  // Get the input values
  let scentInput = document.getElementById("scent");
  let feelingInput = document.getElementById("feeling");

  let scent = scentInput.value.trim();
  let feeling = feelingInput.value.trim();

  // Check if the user entered valid data
  if (scent === "" || feeling === "") {
    alert("Please enter both a scent and a feeling!");
    return;
  }

  // Add the scent to the array
  addScent(scent, feeling);

  // Clear the input fields
  scentInput.value = "";
  feelingInput.value = "";

  // Notify the user
  alert(`Added scent: "${scent}" with feeling: "${feeling}"`);
}

// Function to handle mood analysis
function handleAnalyzeMoods() {
  // Analyze the mood data
  let analysis = analyzeMoods();

  // Display the analysis results
  displayResults(analysis);
}

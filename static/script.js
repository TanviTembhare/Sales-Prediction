document.getElementById("prediction-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
  
    const response = await fetch("/predict", {
      method: "POST",
      body: formData
    });
  
    const result = await response.json();
    const resultDiv = document.getElementById("result");
  
    if (result.prediction) {
      resultDiv.innerHTML = `<p>💰 Predicted Sales: <b>${result.prediction}</b></p>`;
    } else if (result.error) {
      resultDiv.innerHTML = `<p style="color:red;">⚠️ Error: ${result.error}</p>`;
    }
  });
  
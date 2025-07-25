function searchNews() {
  const query = document.getElementById("searchBox").value;
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = `<p class="fade-in">Searching for: <strong>${query}</strong>... (AI backend coming soon)</p>`;
}

const display = document.createElement("p");
  display.style.position = "fixed";
  display.style.top = "0";
  display.style.left = "0";
  display.style.width = "100%";
  display.style.background = "white";
  display.style.zIndex = "10000";
  display.style.margin = "0";
  display.style.padding = "8px";
  display.style.fontWeight = "bold";
  display.textContent = "Click on something...";
  document.body.appendChild(display);

  // track last clicked element to reset its color
  let lastEl = null;

  document.addEventListener("click", e => {
    const el = e.target;

    // avoid triggering when clicking the display bar itself
    if (el === display) return;

    const text = (el.innerText || el.textContent || "").trim();
    display.textContent = text || "[no text]";

    // reset previous element color
    if (lastEl) lastEl.style.backgroundColor = "";
    el.style.backgroundColor = "#ff000059";
    lastEl = el;
  });
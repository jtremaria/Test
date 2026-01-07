const models = [
  {
    name: "GPT-4o",
    provider: "OpenAI",
    focus: "General + Multimodal",
    tag: "Líder en visión",
    updated: "Jun 2024",
    benchmarks: {
      mmlu: 86.5,
      gpqa: 53.2,
      humaneval: 90.2,
      mmmu: 68.7,
    },
    notes: "Muy sólido en tareas multimodales, mantiene buen desempeño en razonamiento general.",
  },
  {
    name: "GPT-5.2",
    provider: "OpenAI",
    focus: "General + Multimodal",
    tag: "Nueva generación",
    updated: "Sep 2024",
    benchmarks: {
      mmlu: 90.8,
      gpqa: 57.4,
      humaneval: 94.1,
      mmmu: 72.6,
    },
    notes: "Iteración más reciente con mejoras en razonamiento y precisión multimodal.",
  },
  {
    name: "Claude 3.5 Sonnet",
    provider: "Anthropic",
    focus: "General + Código",
    tag: "Consistencia",
    updated: "Jun 2024",
    benchmarks: {
      mmlu: 88.3,
      gpqa: 52.0,
      humaneval: 92.0,
      mmmu: 64.5,
    },
    notes: "Destaca en comprensión y generación de código, con fuerte coherencia textual.",
  },
  {
    name: "Claude Opus 4.5",
    provider: "Anthropic",
    focus: "General + Código",
    tag: "Razonamiento profundo",
    updated: "Sep 2024",
    benchmarks: {
      mmlu: 89.6,
      gpqa: 55.1,
      humaneval: 93.3,
      mmmu: 69.4,
    },
    notes: "Modelo premium orientado a tareas complejas y coherencia prolongada.",
  },
  {
    name: "Gemini 1.5 Pro",
    provider: "Google",
    focus: "Multimodal",
    tag: "Contexto largo",
    updated: "May 2024",
    benchmarks: {
      mmlu: 84.2,
      gpqa: 48.1,
      humaneval: 86.7,
      mmmu: 66.1,
    },
    notes: "Excelente para contexto extenso y análisis visual, equilibrado en lenguaje.",
  },
  {
    name: "Llama 3.1 70B",
    provider: "Meta",
    focus: "General + Código",
    tag: "Open-source",
    updated: "Jul 2024",
    benchmarks: {
      mmlu: 82.0,
      gpqa: 44.0,
      humaneval: 81.2,
      mmmu: 58.8,
    },
    notes: "Modelo abierto con gran adopción; requiere ajuste para resultados top en GPQA.",
  },
];

const modelGrid = document.getElementById("model-grid");
const modelCount = document.getElementById("model-count");
const lastUpdated = document.getElementById("last-updated");
const sourceCheck = document.getElementById("source-check");
const dataStatusText = document.getElementById("data-status-text");
const sortSelect = document.getElementById("sort-select");
const filterButtons = document.querySelectorAll(".filter");

const benchmarkMeta = [
  { key: "mmlu", label: "MMLU", category: "general" },
  { key: "gpqa", label: "GPQA", category: "general" },
  { key: "humaneval", label: "HumanEval", category: "coding" },
  { key: "mmmu", label: "MMMU", category: "multimodal" },
];

const formatScore = (value) => `${value.toFixed(1)}%`;

const scoreClass = (value) => {
  if (value >= 85) return "high";
  if (value >= 70) return "mid";
  return "low";
};

const getMetricsForFilter = (filter) => {
  if (filter === "all") return benchmarkMeta;
  return benchmarkMeta.filter((item) => item.category === filter);
};

const sortModels = (metricKey) => {
  return [...models].sort(
    (a, b) => b.benchmarks[metricKey] - a.benchmarks[metricKey]
  );
};

const renderModels = (filter = "general", sortKey = "mmlu") => {
  modelGrid.innerHTML = "";
  const metrics = getMetricsForFilter(filter);
  const sortedModels = sortModels(sortKey);

  sortedModels.forEach((model) => {
    const card = document.createElement("article");
    card.className = "model-card";

    const metricsMarkup = metrics
      .map((metric) => {
        const value = model.benchmarks[metric.key];
        return `
          <div class="metric">
            <span>${metric.label}</span>
            <span class="score ${scoreClass(value)}">${formatScore(value)}</span>
          </div>
        `;
      })
      .join("");

    card.innerHTML = `
      <div class="model-header">
        <div class="model-title">
          <h3>${model.name}</h3>
          <p class="badge">${model.provider}</p>
        </div>
        <span class="tag">${model.tag}</span>
      </div>
      <p class="note"><strong>Enfoque:</strong> ${model.focus}</p>
      <div>
        ${metricsMarkup}
      </div>
      <p class="note">${model.notes}</p>
      <p class="note"><strong>Actualizado:</strong> ${model.updated}</p>
    `;

    modelGrid.appendChild(card);
  });
};

const setActiveFilter = (selected) => {
  filterButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.filter === selected);
  });
};

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;
    setActiveFilter(filter);
    renderModels(filter, sortSelect.value);
  });
});

sortSelect.addEventListener("change", () => {
  const activeFilter = document.querySelector(".filter.active")?.dataset.filter ?? "general";
  renderModels(activeFilter, sortSelect.value);
});

modelCount.textContent = `${models.length} modelos líderes`;
lastUpdated.textContent = "Pendiente de actualización reciente";
sourceCheck.textContent = "Sin verificación automática";
dataStatusText.textContent =
  "Sin conexión a fuentes en vivo. Los benchmarks requieren una actualización para reflejar los últimos avances.";

setActiveFilter("all");
renderModels("all", sortSelect.value);

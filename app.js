let models = [
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
const dataStatusSource = document.getElementById("data-status-source");
const dataStatusAction = document.querySelector(".data-status-action");
const sortSelect = document.getElementById("sort-select");
const filterButtons = document.querySelectorAll(".filter");

const DEFAULT_LAST_UPDATED = "Pendiente de actualización reciente";
const DEFAULT_SOURCE_CHECK = "Sin verificación automática";
const DEFAULT_STATUS =
  "Sin conexión a fuentes en vivo. Los benchmarks requieren una actualización para reflejar los últimos avances.";
const STORAGE_KEY = "benchmarkSourceUrl";

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

const setStatus = ({ statusText, sourceText, lastUpdatedText, sourceCheckText }) => {
  dataStatusText.textContent = statusText;
  dataStatusSource.textContent = sourceText;
  lastUpdated.textContent = lastUpdatedText;
  sourceCheck.textContent = sourceCheckText;
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

const isValidModel = (model) => {
  if (!model || typeof model !== "object") return false;
  const requiredFields = ["name", "provider", "focus", "tag", "updated", "benchmarks"];
  const hasFields = requiredFields.every((field) => field in model);
  if (!hasFields) return false;
  const benchmarks = model.benchmarks;
  if (!benchmarks || typeof benchmarks !== "object") return false;
  return benchmarkMeta.every((metric) => typeof benchmarks[metric.key] === "number");
};

const applyRemoteData = (data, sourceUrl) => {
  if (!data || typeof data !== "object" || !Array.isArray(data.models)) {
    throw new Error("Formato inválido: se esperaba { models: [...] }.");
  }

  const validModels = data.models.filter(isValidModel);
  if (validModels.length === 0) {
    throw new Error("No hay modelos válidos en el dataset.");
  }

  models = validModels;
  modelCount.textContent = `${models.length} modelos líderes`;
  setStatus({
    statusText: "Datos en vivo conectados. Mostrando la última versión del origen.",
    sourceText: `Fuente: ${sourceUrl}`,
    lastUpdatedText: data.lastUpdated || new Date().toLocaleDateString("es-ES"),
    sourceCheckText: data.sourceCheck || "Verificación automática activa",
  });
  const activeFilter = document.querySelector(".filter.active")?.dataset.filter ?? "all";
  renderModels(activeFilter, sortSelect.value);
};

const fetchRemoteData = async (sourceUrl) => {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 8000);

  try {
    const response = await fetch(sourceUrl, { signal: controller.signal });
    if (!response.ok) {
      throw new Error(`No se pudo cargar (${response.status}).`);
    }
    const data = await response.json();
    applyRemoteData(data, sourceUrl);
    localStorage.setItem(STORAGE_KEY, sourceUrl);
  } finally {
    clearTimeout(timeoutId);
  }
};

const connectSource = async () => {
  const sourceUrl = window.prompt(
    "Pega la URL del JSON de benchmarks (formato: { models: [...], lastUpdated, sourceCheck }):"
  );
  if (!sourceUrl) return;

  setStatus({
    statusText: "Conectando a la fuente en vivo...",
    sourceText: `Fuente: ${sourceUrl}`,
    lastUpdatedText: DEFAULT_LAST_UPDATED,
    sourceCheckText: DEFAULT_SOURCE_CHECK,
  });

  try {
    await fetchRemoteData(sourceUrl);
  } catch (error) {
    setStatus({
      statusText: `No se pudo actualizar. ${error.message}`,
      sourceText: `Fuente: ${sourceUrl}`,
      lastUpdatedText: DEFAULT_LAST_UPDATED,
      sourceCheckText: DEFAULT_SOURCE_CHECK,
    });
  }
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
setStatus({
  statusText: DEFAULT_STATUS,
  sourceText: "Fuente: sin conexión",
  lastUpdatedText: DEFAULT_LAST_UPDATED,
  sourceCheckText: DEFAULT_SOURCE_CHECK,
});

setActiveFilter("all");
renderModels("all", sortSelect.value);

dataStatusAction.addEventListener("click", connectSource);

const storedSource = localStorage.getItem(STORAGE_KEY);
if (storedSource) {
  fetchRemoteData(storedSource).catch(() => {
    setStatus({
      statusText: DEFAULT_STATUS,
      sourceText: "Fuente: sin conexión",
      lastUpdatedText: DEFAULT_LAST_UPDATED,
      sourceCheckText: DEFAULT_SOURCE_CHECK,
    });
  });
}

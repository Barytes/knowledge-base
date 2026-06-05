(function () {
  const input = document.querySelector("[data-search-input]");
  const results = document.querySelector("[data-search-results]");
  const count = document.querySelector("[data-search-count]");
  if (!input || !results || !count) return;

  let pages = [];

  const escapeHtml = (value) => value.replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  }[char]));

  const normalize = (value) => value.toLowerCase().trim();

  const snippetFor = (page, query) => {
    const haystack = `${page.title} ${page.summary} ${page.body}`;
    const lowerHaystack = haystack.toLowerCase();
    const lowerQuery = query.toLowerCase();
    const index = lowerHaystack.indexOf(lowerQuery);
    if (index < 0) return escapeHtml(page.summary || page.body.slice(0, 160));
    const start = Math.max(0, index - 56);
    const end = Math.min(haystack.length, index + query.length + 96);
    const prefix = start > 0 ? "..." : "";
    const suffix = end < haystack.length ? "..." : "";
    const excerpt = haystack.slice(start, end);
    const escaped = escapeHtml(excerpt);
    const pattern = new RegExp(query.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi");
    return `${prefix}${escaped.replace(pattern, (match) => `<mark>${match}</mark>`)}${suffix}`;
  };

  const score = (page, query) => {
    const q = normalize(query);
    const title = normalize(page.title);
    const summary = normalize(page.summary);
    const body = normalize(page.body);
    let total = 0;
    if (title.includes(q)) total += 100;
    if (summary.includes(q)) total += 40;
    if (body.includes(q)) total += 10;
    return total;
  };

  const render = () => {
    const query = input.value.trim();
    if (!query) {
      count.textContent = `${pages.length} 个页面可搜索`;
      results.innerHTML = "";
      return;
    }
    const matches = pages
      .map((page) => ({ page, score: score(page, query) }))
      .filter((item) => item.score > 0)
      .sort((a, b) => b.score - a.score || a.page.title.localeCompare(b.page.title, "zh-CN"))
      .slice(0, 40);

    count.textContent = `${matches.length} 个结果`;
    results.innerHTML = matches.map(({ page }) => `
      <article class="result">
        <div class="meta">${escapeHtml(page.layer)} · ${escapeHtml(page.path)}</div>
        <h3><a href="${page.url}">${escapeHtml(page.title)}</a></h3>
        <p class="snippet">${snippetFor(page, query)}</p>
      </article>
    `).join("");
  };

  fetch("search-index.json")
    .then((response) => response.json())
    .then((data) => {
      pages = Array.isArray(data) ? data : [];
      render();
      input.addEventListener("input", render);
      const params = new URLSearchParams(window.location.search);
      const query = params.get("q");
      if (query) {
        input.value = query;
        render();
      }
    })
    .catch(() => {
      count.textContent = "搜索索引加载失败";
    });
}());

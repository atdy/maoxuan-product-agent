(() => {
  const copyText = async (text) => {
    if (navigator.clipboard?.writeText) {
      try {
        await navigator.clipboard.writeText(text);
        return;
      } catch {
        // Fall through for browsers that expose Clipboard API but deny writes.
      }
    }

    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    textarea.style.pointerEvents = "none";
    document.body.append(textarea);
    textarea.select();
    const copied = document.execCommand("copy");
    textarea.remove();

    if (!copied) throw new Error("Copy command was rejected");
  };

  const tool = document.querySelector("[data-install-tool]");

  if (tool) {
    const tabs = [...tool.querySelectorAll("[data-tab]")];
    const panels = [...tool.querySelectorAll("[data-panel]")];

    const selectTab = (selected) => {
      const name = selected.dataset.tab;

      tabs.forEach((tab) => {
        const active = tab === selected;
        tab.setAttribute("aria-selected", String(active));
        tab.tabIndex = active ? 0 : -1;
      });

      panels.forEach((panel) => {
        panel.hidden = panel.dataset.panel !== name;
      });
    };

    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => selectTab(tab));
      tab.addEventListener("keydown", (event) => {
        if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
        event.preventDefault();
        const direction = event.key === "ArrowRight" ? 1 : -1;
        const next = (index + direction + tabs.length) % tabs.length;
        tabs[next].focus();
        selectTab(tabs[next]);
      });
    });
  }

  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const code = button.closest(".code-line")?.querySelector("code")?.textContent?.trim();
      if (!code) return;

      try {
        await copyText(code);
        const icon = button.querySelector("img");
        const previousSrc = icon?.getAttribute("src");
        const previousTitle = button.title;
        const previousLabel = button.getAttribute("aria-label");
        button.title = "已复制";
        button.setAttribute("aria-label", "命令已复制");
        if (icon) icon.setAttribute("src", "assets/icons/check.svg");

        window.setTimeout(() => {
          button.title = previousTitle;
          if (previousLabel) button.setAttribute("aria-label", previousLabel);
          if (icon && previousSrc) icon.setAttribute("src", previousSrc);
        }, 1600);
      } catch {
        button.title = "请手动复制";
      }
    });
  });
})();

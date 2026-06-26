/* ============================================================
   MAIN — interactions
   nav drawer · drawer accordions · scroll reveal · quote modal
   · form validation · Web3Forms submission (no backend needed)
   ============================================================ */
(function () {
  var S = window.SITE || {};

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    /* ---- mobile drawer ---- */
    var body = document.body;
    function closeNav() { body.classList.remove("nav-open"); var b = document.querySelector(".burger"); if (b) b.setAttribute("aria-expanded", "false"); }
    document.addEventListener("click", function (e) {
      if (e.target.closest("[data-theme-toggle]")) {
        var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", next);
        try { localStorage.setItem("avk-theme", next); } catch (err) {}
      }
      if (e.target.closest(".burger")) {
        body.classList.toggle("nav-open");
        var b = document.querySelector(".burger");
        b.setAttribute("aria-expanded", body.classList.contains("nav-open"));
      }
      if (e.target.closest("[data-close-nav]")) closeNav();
      var grp = e.target.closest(".dgroup > button");
      if (grp) grp.parentElement.classList.toggle("open");
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeNav(); closeModal(); } });

    /* ---- scroll reveal (with failsafe so nothing stays hidden) ---- */
    var reveals = document.querySelectorAll(".reveal");
    function revealAll() { reveals.forEach(function (el) { el.classList.add("in"); }); }
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
      }, { threshold: 0.01, rootMargin: "0px 0px 12% 0px" });
      reveals.forEach(function (el) { io.observe(el); });
      setTimeout(revealAll, 1500); // safety net: never leave content invisible
    } else {
      revealAll();
    }

    /* ---- quote modal ---- */
    var modal = document.getElementById("quote-modal");
    function openModal() { if (modal) { modal.classList.add("open"); document.body.style.overflow = "hidden"; } }
    function closeModal() { if (modal) { modal.classList.remove("open"); document.body.style.overflow = ""; } }
    window.closeModal = closeModal;
    document.addEventListener("click", function (e) {
      if (e.target.closest("[data-open-quote]")) { e.preventDefault(); openModal(); }
      if (e.target.closest("[data-close-modal]") || e.target.classList.contains("modal__scrim")) closeModal();
    });

    /* ---- forms ---- */
    initForms(closeModal);
  });

  function initForms(closeModal) {
    var key = S.formAccessKey;
    var demo = !key || key.indexOf("REPLACE_WITH") === 0;

    document.querySelectorAll("form[data-form]").forEach(function (form) {
      var status = form.querySelector(".form-status");

      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!validate(form)) return;

        var btn = form.querySelector("[type=submit]");
        var label = btn ? btn.textContent : "";
        if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }

        if (demo) {
          // No key set yet — simulate success so the UI is testable.
          setTimeout(function () {
            done(true, "Demo mode: form is valid. Add a Web3Forms key in site.config.js to deliver emails.");
          }, 500);
          return;
        }

        var data = new FormData(form);
        data.append("access_key", key);
        data.append("subject", (form.getAttribute("data-subject") || "Website enquiry") + " — " + (S.brand && S.brand.name));
        fetch("https://api.web3forms.com/submit", { method: "POST", body: data })
          .then(function (r) { return r.json(); })
          .then(function (j) { done(j.success, j.success ? "Thanks — your message has been sent. We'll be in touch." : (j.message || "Something went wrong. Please try again.")); })
          .catch(function () { done(false, "Network error. Please try again or email us directly."); });

        function done(ok, msg) {
          if (btn) { btn.disabled = false; btn.textContent = label; }
          if (status) { status.className = "form-status " + (ok ? "ok" : "bad"); status.textContent = msg; }
          if (ok) {
            form.reset();
            if (form.closest(".modal")) setTimeout(closeModal, 2200);
          }
        }
      });

      // clear error state on input
      form.querySelectorAll("input,select,textarea").forEach(function (el) {
        el.addEventListener("input", function () {
          var f = el.closest(".field"); if (f) f.classList.remove("invalid");
        });
      });
    });
  }

  function validate(form) {
    var ok = true;
    form.querySelectorAll("[required]").forEach(function (el) {
      var field = el.closest(".field") || el.closest(".consent");
      var valid = el.type === "checkbox" ? el.checked : String(el.value).trim() !== "";
      if (el.type === "email" && valid) valid = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value);
      if (field) field.classList.toggle("invalid", !valid);
      if (!valid && ok) { ok = false; (field || el).scrollIntoView({ behavior: "smooth", block: "center" }); }
    });
    return ok;
  }
})();

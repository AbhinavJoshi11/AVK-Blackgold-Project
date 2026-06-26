/* ============================================================
   COMPONENTS — header + footer rendered from one place.
   Reads window.SITE (site.config.js). Edit nav/footer there.
   ============================================================ */
(function () {
  var S = window.SITE;
  if (!S) { console.error("site.config.js must load before components.js"); return; }

  var page = location.pathname.split("/").pop() || "index.html";
  function isCurrent(href) { return href ? href.split("#")[0] === page : false; }

  /* ---- inline icons (currentColor) ---- */
  var ICONS = {
    email: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg>',
    whatsapp: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12.4 7.5L3 21l2-5.4A8.5 8.5 0 1 1 21 11.5Z"/><path d="M8.5 9.5c0 3 2 5 5 5.5"/></svg>',
    youtube: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="3.5"/><path d="m10 9 5 3-5 3Z" fill="currentColor" stroke="none"/></svg>',
    linkedin: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.49 2.49 0 1 1 0 3.5a2.49 2.49 0 0 1 4.98 0ZM.4 8.2h4.16V24H.4V8.2Zm6.84 0h3.99v2.16h.06c.56-1.05 1.92-2.16 3.95-2.16 4.22 0 5 2.78 5 6.4V24h-4.16v-7c0-1.67-.03-3.82-2.33-3.82-2.33 0-2.69 1.82-2.69 3.7V24H7.24V8.2Z"/></svg>',
    facebook: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.5 1.49-3.89 3.78-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v6.99A10 10 0 0 0 22 12Z"/></svg>',
    instagram: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5.2"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>',
    threads: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8.2C15 6.8 13.6 6 12 6c-3 0-5 2.3-5 6s2 6 5 6c2.4 0 3.9-1.4 3.9-3.1 0-2-1.6-3-3.5-3-1.3 0-2.3.7-2.3 1.9 0 .9.7 1.5 1.6 1.5 1.2 0 2-1 2-2.6"/></svg>'
  };
  function icon(label) { return ICONS[(label || "").toLowerCase()] || ""; }

  /* ---- brand logo (inline SVG; wordmark uses currentColor so it
         shows white over the hero video and dark on light headers) ---- */
  // function logoSVG() {
  //   return '<svg class="brand-logo" viewBox="0 0 300 92" role="img" aria-label="AVK Blackgold Infra">' +
  //     '<path d="M4 76 Q 92 58 182 30" fill="none" stroke="#ff0d0d" stroke-width="13" stroke-linecap="round"/>' +
  //     '<path d="M4 76 Q 92 58 182 30" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-dasharray="9 9" stroke-linecap="round"/>' +
  //     '<text x="0" y="54" font-family="Poppins, Arial, sans-serif" font-weight="800" font-size="58" letter-spacing="-1.5" fill="currentColor">AVK</text>' +
  //     '<text x="2" y="88" font-family="Poppins, Arial, sans-serif" font-weight="700" font-size="12.5" letter-spacing="2.6" fill="currentColor">BLACKGOLD INFRA PVT. LTD.</text>' +
  //     '</svg>';
  // }
function logoSVG() {
  return '<img class="brand-logo" src="assets/img/logo-avk.png" alt="AVK Blackgold Infra">';
}

  var TOGGLE =
    '<svg class="ic-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>' +
    '<svg class="ic-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6 19 19M19 5l-1.4 1.4M6.4 17.6 5 19"/></svg>';

  function social() {
    return S.social.map(function (s) {
      return '<a href="' + s.href + '" aria-label="' + s.label + '">' + icon(s.label) + '<span>' + s.label + '</span></a>';
    }).join("");
  }

  /* ---- header nav ---- */
  function megaAbout(item) {
    return '<div class="mega"><div class="mega-grid is-3">' + item.columns.map(function (c) {
      return '<a class="mega-card" href="' + c.href + '"><span class="t">' + c.title + '</span><span class="n">' + c.note + '</span></a>';
    }).join("") + '</div></div>';
  }
  function megaDo(item) {
    var p = item.products.map(function (x) { return '<a class="mega-link" href="' + x.href + '">' + x.title + '</a>'; }).join("");
    var s = item.services.map(function (x) { return '<a class="mega-link" href="' + x.href + '">' + x.title + '</a>'; }).join("");
    return '<div class="mega"><div class="mega-tabs"><div><h4>Products</h4>' + p + '</div><div><h4>Services</h4>' + s + '</div></div></div>';
  }
  function navItems() {
    return S.nav.map(function (item) {
      if (item.mega) {
        return '<li class="nav__item"><button class="nav__link" aria-haspopup="true">' + item.label +
          '<span class="nav__caret"></span></button>' + (item.mega === "about" ? megaAbout(item) : megaDo(item)) + '</li>';
      }
      var cur = isCurrent(item.href) ? ' aria-current="page"' : "";
      return '<li class="nav__item"><a class="nav__link" href="' + item.href + '"' + cur + '>' + item.label + '</a></li>';
    }).join("");
  }
  function drawerItems() {
    return S.nav.map(function (item) {
      if (item.mega) {
        var subs = item.mega === "about"
          ? item.columns.map(function (c) { return '<a href="' + c.href + '">' + c.title + '</a>'; }).join("")
          : item.products.concat(item.services).map(function (x) { return '<a href="' + x.href + '">' + x.title + '</a>'; }).join("");
        return '<div class="dgroup"><button>' + item.label + '<span class="nav__caret"></span></button><div class="dsub">' + subs + '</div></div>';
      }
      return '<a href="' + item.href + '">' + item.label + '</a>';
    }).join("");
  }

  var headerHTML =
    '<div class="topbar"><div class="wrap">' + social() + '</div></div>' +
    '<header class="header"><div class="wrap header__bar">' +
      '<a class="logo" href="index.html" aria-label="AVK Blackgold Infra home">' + logoSVG() + '</a>' +
      '<nav aria-label="Primary"><ul class="nav">' + navItems() + '</ul></nav>' +
      '<div class="header__cta">' +
        '<button class="theme-toggle" data-theme-toggle aria-label="Toggle dark mode">' + TOGGLE + '</button>' +
        '<a class="btn btn--primary" href="#" data-open-quote>Request a Quote</a>' +
        '<button class="burger" aria-label="Open menu" aria-expanded="false"><span></span></button>' +
      '</div>' +
    '</div></header>' +
    '<div class="scrim" data-close-nav></div>' +
    '<aside class="drawer" aria-label="Mobile menu">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">' +
        '<a class="logo" href="index.html" aria-label="AVK Blackgold Infra home">' + logoSVG() + '</a>' +
        '<button class="theme-toggle" data-theme-toggle aria-label="Toggle dark mode">' + TOGGLE + '</button></div>' +
      drawerItems() +
      '<a class="btn btn--primary" style="margin-top:18px;justify-content:center" href="#" data-open-quote>Request a Quote</a>' +
    '</aside>';

  /* ---- footer ---- */
  var c = S.contact;
  var footerHTML =
    '<footer class="footer">' +
      '<div class="footer__top"><div class="wrap">' +
        S.footerLinks.map(function (l) { return '<a href="' + l.href + '">' + l.label + '</a>'; }).join("") +
      '</div></div>' +
      '<div class="footer__main"><div class="wrap">' +
        '<div class="footer__brand">' +
          '<a class="logo" href="index.html" aria-label="AVK Blackgold Infra home">' + logoSVG() + '</a>' +
          '<h4>Registered Office</h4>' +
          '<address>' + c.addressLines.join("<br>") + '<br><br>CIN: ' + c.cin +
            '<br>Working Hours: ' + c.workingHours + '<br>Working Days: ' + c.workingDays +
            '<br><br>Email: <a href="mailto:' + c.corporateEmail + '">' + c.corporateEmail + '</a>' +
            '<br>Tel: <a href="tel:' + c.phone.replace(/\s/g, "") + '">' + c.phone + '</a>' +
            (c.phoneAlt ? ' / <a href="tel:' + c.phoneAlt.replace(/\s/g, "") + '">' + c.phoneAlt + '</a>' : "") + '</address>' +
          '<div class="footer__social">' + social() + '</div>' +
        '</div>' +
        '<div><h4>Quick Links</h4><div class="qlinks">' +
          S.quickLinks.map(function (l) { return '<a href="' + l.href + '">' + l.label + '</a>'; }).join("") +
        '</div></div>' +
        '<div><h4>Our Location</h4>' +
          '<div class="mapbox"><iframe title="AVK Blackgold Infra, Magdalla, Surat" ' +
            'src="https://www.google.com/maps?q=Rajhans%20Montessa%2C%20Magdalla%2C%20Surat%20395007&output=embed" ' +
            'loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>' +
          '<p style="margin-top:12px;font-size:.85rem">714, Rajhans Montessa, Magdalla, Surat &ndash; 395 007</p>' +
        '</div>' +
      '</div></div>' +
      '<div class="footer__bottom"><div class="wrap">' +
        '<span>&copy; ' + new Date().getFullYear() + ' ' + S.brand.legalName + '. All Rights Reserved.</span>' +
      '</div></div>' +
    '</footer>';

  var h = document.getElementById("site-header");
  var f = document.getElementById("site-footer");
  if (h) h.innerHTML = headerHTML;
  if (f) f.innerHTML = footerHTML;

  /* Home page: overlay header transparently on top of the hero video */
  if (page === "index.html" || page === "") {
    document.body.classList.add("is-home");
  }

  /* Global "go to top" button (bottom-right, visible on every page) */
  if (!document.querySelector(".to-top")) {
    var top = document.createElement("button");
    top.className = "to-top";
    top.setAttribute("data-to-top", "");
    top.setAttribute("aria-label", "Back to top");
    top.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 15l6-6 6 6"/></svg>';
    document.body.appendChild(top);
  }
})();

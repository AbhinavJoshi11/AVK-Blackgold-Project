/* ============================================================
   SITE CONFIG  —  EDIT THIS FILE TO UPDATE THE WHOLE SITE
   ------------------------------------------------------------
   Company details, contact info, navigation, and the form key
   all live here. Change once, every page updates.
   ============================================================ */

window.SITE = {
  /* ---- Brand ---- */
  brand: {
    name: "AVK Blackgold Infra",
    legalName: "AVK Blackgold Infra Private Limited",
    tagline: "Engineered Bituminous Solutions",
    logoText: "AVK", // text mark;
  },

  /* ---- Contact ---- */
  contact: {
    email: "info@blackgoldinfra.com",
    corporateEmail: "info@blackgoldinfra.com",
    phone: "+91 90330 90399",
    phoneAlt: "+91 88285 99845",
    whatsapp: "https://wa.me/919033090399",
    addressLines: [
      "AVK Blackgold Infra Private Limited",
      "714, Rajhans Montessa, Beside Le Meridien Hotel,",
      "Magdalla, Surat - 395 007, Gujarat, India",
    ],
    cin: "U00000XX0000PTC000000", // EDIT: add real CIN when available
    workingHours: "9:30 am to 6:00 pm",
    workingDays: "Monday to Saturday",
  },

  /* ---- Social (EDIT links) ---- */
  social: [
    { label: "Email", href: "mailto:info@blackgoldinfra.com" },
    { label: "WhatsApp", href: "https://wa.me/919033090399" },
    { label: "YouTube", href: "#" },
    { label: "LinkedIn", href: "#" },
    { label: "Facebook", href: "#" },
    { label: "Instagram", href: "#" },
  ],

  /* ---- Web3Forms access key ----
     Forms work the moment you paste a real key here.
     Get a free key at https://web3forms.com (no backend needed).
     Leave as-is to run in DEMO mode (validates + shows success, no email sent). */
  formAccessKey: "REPLACE_WITH_YOUR_WEB3FORMS_KEY",

  /* ---- Primary navigation ----
     "mega" entries render the dropdown panels. Edit freely. */
  nav: [
    { label: "Home", href: "index.html" },

    {
      label: "About Us",
      mega: "about",
      columns: [
        {
          title: "About AVK",
          href: "about-us.html",
          note: "About us · Vision · Core Values · Quality · R&D · Certificates · Leadership",
        },
        {
          title: "Responsible Commitment",
          href: "responsible-commitment.html#CSR",
          note: "CSR · Sustainability · HSE · Risk Management · Whistleblower",
        },
        {
          title: "Our Clients",
          href: "our-clients.html",
          note: "Highways & Expressways · Airports · Race Tracks",
        },
      ],
    },

    {
      label: "What We Do",
      mega: "do",
      products: [
        { title: "Bitumen Emulsions", href: "bitumen-emulsions.html" },
        { title: "CRMB", href: "crmb.html" },
        { title: "PMB", href: "pmb.html" },
        { title: "Special Products", href: "special-products.html" },
        { title: "Pothole Repair", href: "roadbond.html" },
      ],
      services: [
        { title: "Maintenance & Repair", href: "services.html#Microsurfacing" },
        { title: "Project Management", href: "services.html#Technical-Consultancy" },
        { title: "Material Testing", href: "services.html#Material-Testing" },
      ],
    },

    { label: "Partnering Customer", href: "partnering-customer.html" },
    { label: "Join Us", href: "join-us.html" },
    { label: "Contact Us", href: "contact-us.html" },
  ],

  /* ---- Footer quick links ---- */
  quickLinks: [
    { label: "CSR", href: "responsible-commitment.html#CSR" },
    { label: "Jobs", href: "jobs.html" },
    { label: "Tenders", href: "tenders.html" },
    { label: "Blogs", href: "blogs.html" },
    { label: "Technical Consultancy", href: "services.html#Technical-Consultancy" },
    { label: "Bitumen Emulsions", href: "bitumen-emulsions.html" },
    { label: "Modified Bitumen (CRMB)", href: "crmb.html" },
    { label: "Modified Bitumen (PMB)", href: "pmb.html" },
    { label: "Microsurfacing", href: "services.html#Microsurfacing" },
    { label: "Material Testing Lab", href: "services.html#Material-Testing" },
  ],

  footerLinks: [
    { label: "Responsible Commitment", href: "responsible-commitment.html" },
    { label: "Cookies Policy", href: "privacy-policy.html" },
    { label: "Privacy Policy", href: "privacy-policy.html" },
    { label: "Jobs", href: "jobs.html" },
    { label: "Tenders", href: "tenders.html" },
    { label: "Contact Us", href: "contact-us.html" },
  ],

  /* ---- Quote form: emulsion grades (EDIT to your catalogue) ---- */
  emulsionGrades: [
    "Rapid Setting 1", "Rapid Setting 2", "Medium Setting",
    "Slow Setting SS1", "Slow Setting 2", "Slow Setting 1 ASTM",
    "Slow Setting 1h", "RAP Emulsion", "SS2 Stab", "Prime SS1 (ASTM)",
  ],
};

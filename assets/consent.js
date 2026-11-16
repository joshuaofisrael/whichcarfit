(function () {
  var KEY = "whichcarfit-consent";
  var banner = document.getElementById("consent-banner");
  var loader = document.querySelector("script[data-ga4-loader]");
  if (!banner || !loader) return;
  var id = loader.getAttribute("data-ga4-id") || "";
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };

  function show() {
    banner.hidden = false;
  }
  function hide() {
    banner.hidden = true;
  }
  function load() {
    if (!/^G-[A-Za-z0-9]+$/.test(id) || window.__ga4Loaded) return;
    window.__ga4Loaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + id;
    s.onload = function () {
      window.gtag("js", new Date());
      window.gtag("config", id);
    };
    document.head.appendChild(s);
  }
  function grant() {
    try { localStorage.setItem(KEY, "granted"); } catch (e) {}
    window.gtag("consent", "update", { analytics_storage: "granted" });
    load();
    hide();
  }
  function deny() {
    try { localStorage.setItem(KEY, "denied"); } catch (e) {}
    window.gtag("consent", "update", {
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
      analytics_storage: "denied"
    });
    hide();
  }
  var accept = document.getElementById("consent-accept");
  var reject = document.getElementById("consent-reject");
  if (accept) accept.addEventListener("click", grant);
  if (reject) reject.addEventListener("click", deny);
  var settings = document.getElementById("cookie-settings");
  if (settings) {
    settings.addEventListener("click", function (e) {
      e.preventDefault();
      show();
      if (accept) accept.focus();
    });
  }
  var choice = null;
  try { choice = localStorage.getItem(KEY); } catch (e) {}
  if (choice === "granted") grant();
  else if (choice !== "denied") show();
})();

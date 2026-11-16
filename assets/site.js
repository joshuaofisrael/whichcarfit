(function () {
  var dataEl = document.getElementById("catalog");
  var form = document.getElementById("picker");
  if (!dataEl || !form) return;
  var rows = JSON.parse(dataEl.textContent);
  var make = document.getElementById("pick-make");
  var model = document.getElementById("pick-model");
  var year = document.getElementById("pick-year");
  function uniq(list) {
    var out = [];
    list.forEach(function (x) { if (out.indexOf(x) < 0) out.push(x); });
    return out;
  }
  function fill(sel, items, placeholder) {
    sel.innerHTML = "";
    var o = document.createElement("option");
    o.value = "";
    o.textContent = placeholder;
    sel.appendChild(o);
    items.forEach(function (item) {
      var opt = document.createElement("option");
      opt.value = item;
      opt.textContent = item;
      sel.appendChild(opt);
    });
  }
  fill(make, uniq(rows.map(function (r) { return r.make; })), "Make");
  fill(model, [], "Model");
  fill(year, [], "Year");
  make.addEventListener("change", function () {
    var models = uniq(rows.filter(function (r) { return r.make === make.value; }).map(function (r) { return r.model; }));
    fill(model, models, "Model");
    fill(year, [], "Year");
  });
  model.addEventListener("change", function () {
    var years = uniq(rows.filter(function (r) { return r.make === make.value && r.model === model.value; }).map(function (r) { return r.year; }));
    years.sort();
    fill(year, years, "Year");
  });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var hit = rows.filter(function (r) {
      return r.make === make.value && r.model === model.value && r.year === year.value;
    })[0];
    var status = document.getElementById("pick-status");
    if (!hit) {
      status.hidden = false;
      status.textContent = "Choose a make, a model, and a year.";
      return;
    }
    window.location.href = hit.url;
  });
})();

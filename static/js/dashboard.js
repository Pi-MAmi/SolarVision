/* ==========================================================
   SolarVision v1.2 Professional
   Dashboard.js
   Bölüm 1
========================================================== */

const API = "/api/live";
const WEATHER_API = "/api/weather";
const SETTINGS_API = "/api/settings";

let SETTINGS = {

    electric_price: 3.24,

    refresh: 2

};

let todayEnergy = 0;

let lastUpdate = null;

let pvChart = null;


/* ==========================================================
   SETTINGS
========================================================== */

async function loadSettings() {

    try {

        const response = await fetch(SETTINGS_API);

        SETTINGS = await response.json();

        SETTINGS.electric_price =
            parseFloat(SETTINGS.electric_price);

        SETTINGS.refresh =
            parseInt(SETTINGS.refresh);

    }

    catch (err) {

        console.log("Settings okunamadı.");

    }

}


/* ==========================================================
   CANLI VERİLER
========================================================== */

async function loadLiveData() {

    try {

        const response = await fetch(API);

        const data = await response.json();

        updateValues(data);

    }

    catch (err) {

        console.log(err);

    }

}


function updateValues(data) {

    setText(
        "battery_voltage",
        Number(data.battery_voltage).toFixed(2)
    );

    setText(
        "battery_capacity",
        data.battery_capacity
    );

    setText(
        "battery_voltage_table",
        Number(data.battery_voltage).toFixed(2) + " V"
    );

    setText(
        "battery_capacity_table",
        data.battery_capacity + " %"
    );

    setText("pv_power", data.pv_power);

    setText(
        "pv_voltage",
        Number(data.pv_voltage).toFixed(1)
    );

    setText(
        "pv_current",
        Number(data.pv_current).toFixed(1)
    );

    setText(
        "output_voltage",
        data.output_voltage
    );

    setText(
        "output_watt",
        data.output_watt
    );

    setText(
        "load_percent",
        data.load_percent
    );

    setText(
        "grid_voltage",
        data.grid_voltage + " V"
    );

    setText(
        "grid_frequency",
        data.grid_frequency + " Hz"
    );

    setText(
        "output_frequency",
        data.output_frequency + " Hz"
    );

    setText(
        "temperature",
        Number(data.temperature).toFixed(1) + " °C"
    );

    updateBattery(data.battery_capacity);

    updateStatistics(data);

}


/* ==========================================================
   BATARYA
========================================================== */

function updateBattery(percent) {

    const bar =
        document.getElementById("battery_fill");

    if (!bar)
        return;

    bar.style.width = percent + "%";

    if (percent >= 80) {

        bar.style.background =
            "linear-gradient(90deg,#22c55e,#4ade80)";

    }

    else if (percent >= 50) {

        bar.style.background =
            "linear-gradient(90deg,#eab308,#fde047)";

    }

    else if (percent >= 25) {

        bar.style.background =
            "linear-gradient(90deg,#fb923c,#fdba74)";

    }

    else {

        bar.style.background =
            "linear-gradient(90deg,#dc2626,#ef4444)";

    }

}


/* ==========================================================
   HAVA DURUMU
========================================================== */

async function loadWeather() {

    try {

        const response =
            await fetch(WEATHER_API);

        const weather =
            await response.json();

        setText(
            "weather_city",
            weather.city
        );

        setText(
            "weather_text",
            weather.weather
        );

        setText(
            "weather_temp",
            Number(weather.temperature).toFixed(1) + " °C"
        );

        setText(
            "weather_icon",
            weather.icon
        );

        updateWeatherDetails(weather);

    }

    catch (err) {

        console.log(err);

    }

}


function updateWeatherDetails(weather) {

    let detail =
        document.getElementById("weather_detail");

    if (!detail) {

        detail =
            document.createElement("div");

        detail.id = "weather_detail";

        detail.style.marginTop = "12px";

        detail.style.fontSize = "16px";

        detail.style.color = "#cfd8dc";

        document
            .getElementById("weather_city")
            .parentElement
            .appendChild(detail);

    }

    detail.innerHTML =

        "💧 Nem : %" + weather.humidity +

        "<br>" +

        "💨 Rüzgar : " + weather.wind + " km/s";

}


/* ==========================================================
   SAAT
========================================================== */

function updateClock() {

    const now = new Date();

    setText(
        "clock",
        now.toLocaleTimeString("tr-TR")
    );

    setText(
        "date",
        now.toLocaleDateString(
            "tr-TR",
            {
                weekday: "long",
                year: "numeric",
                month: "long",
                day: "numeric"
            }
        )
    );

}


function setText(id, value) {

    const el =
        document.getElementById(id);

    if (el)
        el.textContent = value;

}

/* ==========================================================
   İSTATİSTİKLER
========================================================== */

function updateStatistics(data) {

    if (lastUpdate) {

        const diff = (Date.now() - lastUpdate) / 1000;

        todayEnergy +=
            (data.pv_power * diff) / 3600000;

    }

    lastUpdate = Date.now();

    setText(
        "today_energy",
        todayEnergy.toFixed(3)
    );

    setText(
        "today_income",
        (
            todayEnergy *
            SETTINGS.electric_price
        ).toFixed(2)
    );

    updateGridStatus(data);

    updateLastSeen();

}


/* ==========================================================
   ŞEBEKE DURUMU
========================================================== */

function updateGridStatus(data) {

    let badge =
        document.getElementById("grid_status");

    if (!badge) {

        badge = document.createElement("div");

        badge.id = "grid_status";

        badge.className = "status";

        document
            .querySelector("header")
            .appendChild(badge);

    }

    if (data.grid_voltage > 100) {

        badge.className =
            "status status-online";

        badge.innerHTML =
            "🟢 Şebeke Bağlı";

    }

    else {

        badge.className =
            "status status-battery";

        badge.innerHTML =
            "🟠 Akü Modu";

    }

}


/* ==========================================================
   SON GÜNCELLEME
========================================================== */

function updateLastSeen() {

    let obj =
        document.getElementById("last_update");

    if (!obj) {

        obj =
            document.createElement("div");

        obj.id = "last_update";

        obj.className = "footer";

        document
            .querySelector(".container")
            .appendChild(obj);

    }

    obj.innerHTML =
        "Son Güncelleme : " +
        new Date().toLocaleTimeString("tr-TR");

}


/* ==========================================================
   PV GRAFİĞİ
========================================================== */

async function loadHistory() {

    try {

        const response =
            await fetch("/api/history");

        const history =
            await response.json();

        const labels = [];

        const powers = [];

        history.forEach(item => {

            const t =
                new Date(item.timestamp);

            labels.push(

                t.toLocaleTimeString(

                    "tr-TR",

                    {

                        hour: "2-digit",

                        minute: "2-digit"

                    }

                )

            );

            powers.push(item.pv_power);

        });

        drawPVChart(labels, powers);

    }

    catch (err) {

        console.log(err);

    }

}


function drawPVChart(labels, data) {

    const ctx =
        document
            .getElementById("pvChart")
            .getContext("2d");

    if (pvChart)
        pvChart.destroy();

    pvChart = new Chart(ctx, {

        type: "line",

        data: {

            labels: labels,

            datasets: [

                {

                    label: "PV Gücü (W)",

                    data: data,

                    borderColor: "#FFD54F",

                    backgroundColor:
                        "rgba(255,213,79,0.15)",

                    borderWidth: 2,

                    fill: true,

                    pointRadius: 0,

                    tension: 0.35

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            animation: false,

            plugins: {

                legend: {

                    labels: {

                        color: "#ffffff"

                    }

                }

            },

            scales: {

                x: {

                    ticks: {

                        color: "#cccccc",

                        maxTicksLimit: 10

                    },

                    grid: {

                        color: "#333"

                    }

                },

                y: {

                    beginAtZero: true,

                    ticks: {

                        color: "#cccccc"

                    },

                    grid: {

                        color: "#333"

                    }

                }

            }

        }

    });

}


/* ==========================================================
   BAŞLAT
========================================================== */

async function startDashboard() {

    await loadSettings();

    updateClock();

    loadWeather();

    loadHistory();

    loadLiveData();

    setInterval(
        updateClock,
        1000
    );

    setInterval(
        loadWeather,
        600000
    );

    setInterval(
        loadHistory,
        30000
    );

    setInterval(
        loadLiveData,
        SETTINGS.refresh * 1000
    );

}

startDashboard();
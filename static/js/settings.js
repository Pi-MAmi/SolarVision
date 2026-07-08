async function loadSettings() {

    try {

        const response = await fetch("/api/settings");

        const settings = await response.json();

        document.getElementById("city").value =
            settings.city;

        document.getElementById("electric_price").value =
            settings.electric_price;

        document.getElementById("refresh").value =
            settings.refresh;

    }

    catch (err) {

        console.error(err);

        alert("Ayarlar okunamadý.");

    }

}


async function saveSettings() {

    const body = {

        city:
            document.getElementById("city").value,

        electric_price:
            document.getElementById("electric_price").value,

        refresh:
            document.getElementById("refresh").value

    };

    try {

        const response = await fetch("/api/settings", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(body)

        });

        const result = await response.json();

        if (result.status === "ok") {

            alert("Ayarlar kaydedildi.");

            loadSystemInfo();

        }

    }

    catch (err) {

        console.error(err);

        alert("Kayýt baþarýsýz.");

    }

}


async function loadSystemInfo() {

    try {

        const response = await fetch("/api/system");

        const data = await response.json();

        setText("collector", statusIcon(data.collector));
        setText("gunicorn", statusIcon(data.gunicorn));
        setText("nginx", statusIcon(data.nginx));

        setText("cpu_temp", data.cpu_temp + " °C");
        setText("memory", data.memory + " %");
        setText("disk", data.disk + " %");

        setText("python", data.python);
        setText("database", data.database + " MB");

        setText("uptime", data.uptime);

        setText("version", data.version);

    }

    catch (err) {

        console.error(err);

    }

}


function statusIcon(status) {

    if (status === "active") {

        return "?? Active";

    }

    if (status === "inactive") {

        return "?? Inactive";

    }

    if (status === "failed") {

        return "?? Failed";

    }

    return status;

}


function setText(id, value) {

    const el = document.getElementById(id);

    if (el) {

        el.textContent = value;

    }

}


loadSettings();

loadSystemInfo();

setInterval(loadSystemInfo, 10000);
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

        }

    }

    catch (err) {

        console.error(err);

        alert("Kayýt baþarýsýz.");

    }

}


loadSettings();
document.addEventListener('DOMContentLoaded', function() {
    var ageFilter = $("#ageSlider");
    var ratingFilter = $("#ratingSlider");
    var ratingFFilter = $("#ratingFSlider");
    var ratingAFilter = $("#ratingASlider");
    var ratingPFilter = $("#ratingPSlider");
    var positionFilter = document.getElementById('positionFilter');
    var contractFilter = $("#contractSlider")
    var searchFilter = document.getElementById('search'); // Assurez-vous que l'ID est correct

    // Variables pour stocker les valeurs des filtres
    var currentFilters = {
        age: [12,130],
        rating: [0,5],
        ratingA: [0, 5],  // Nouvelle propriété pour la note actuelle
        ratingP: [0, 5],  // Nouvelle propriété pour la note potentielle
        ratingF: [0, 5],  // Nouvelle propriété pour la note financière
        position: positionFilter.value,
        contract: [new Date().getFullYear() - 6, new Date().getFullYear() + 10]
    };

    // Variable pour stocker la valeur de recherche
    var currentSearch = '';

    // Fonction pour appliquer tous les filtres
    function applyFilters() {
        var table = $(".table-striped");
        var tr = table.find("tr");

        for (var i = 1; i < tr.length; i++) {
            var display = true;

            // Filtrage par âge
            var tdAge = $(tr[i]).find("td:eq(1)");
            var age = tdAge.length > 0 ? parseInt(tdAge.text()) : null;
            if (currentFilters.age !== "" && (age === null || age < currentFilters.age[0] || age > currentFilters.age[1] )) {
                display = false;
            }

            // Filtrage par note
            var tdRating = $(tr[i]).find("td:eq(8)");
            var ratingText = tdRating.length > 0 ? tdRating.text() : "";
            var rating = ratingText === "non calculable" ? -2 : parseFloat(ratingText.replace("R", ""));
            if (ratingText !== "non calculable" && currentFilters.rating !== "" && (isNaN(rating) || rating < currentFilters.rating[0] || rating > currentFilters.rating[1])) {
                display = false;
            }

            // Filtrage par note actuelle
            var tdRatingA = $(tr[i]).find("td:eq(5)");
            var ratingAText = tdRatingA.length > 0 ? tdRatingA.text() : "";
            var ratingA = ratingAText === "non calculable" ? -2 : parseFloat(ratingAText.replace("R", ""));
            if (ratingAText !== "non calculable" && currentFilters.ratingA !== "" && (isNaN(ratingA) || ratingA < currentFilters.ratingA[0] || ratingA > currentFilters.ratingA[1])) {
                display = false;
            }

            // Filtrage par note potentielle
            var tdRatingP = $(tr[i]).find("td:eq(6)");
            var ratingPText = tdRatingP.length > 0 ? tdRatingP.text() : "";
            var ratingP = ratingPText === "non calculable" ? -2 : parseFloat(ratingPText.replace("R", ""));
            if (ratingPText !== "non calculable" && currentFilters.ratingP !== "" && (isNaN(ratingP) || ratingP < currentFilters.ratingP[0] || ratingP > currentFilters.ratingP[1])) {
                display = false;
            }

            // Filtrage par note financière
            var tdRatingF = $(tr[i]).find("td:eq(7)");
            var ratingFText = tdRatingF.length > 0 ? tdRatingF.text() : "";
            var ratingF = ratingFText === "non calculable" ? -2 : parseFloat(ratingFText.replace("R", ""));
            if (ratingFText !== "non calculable" && currentFilters.ratingF !== "" && (isNaN(ratingF) || ratingF < currentFilters.ratingF[0] || ratingF > currentFilters.ratingF[1])) {
                display = false;
            }

            // Filtrage par position
            var tdPosition = $(tr[i]).find("td:eq(2)");
            var position = tdPosition.length > 0 ? tdPosition.text() : "";
            if (currentFilters.position !== "" && position !== currentFilters.position) {
                display = false;
            }

            // Filtrage par contrat
            var tdContract = $(tr[i]).find("td:eq(9)");
            // Extract year from the date string
            var contractDate = tdContract.length > 0 ? new Date(tdContract.text()) : null;
            var contractYear = contractDate ? contractDate.getFullYear() : null;

            // Compare with the filters
            if (currentFilters.contract !== "" && 
                (contractYear === null || 
                contractYear < currentFilters.contract[0] || 
                contractYear > currentFilters.contract[1])) {
                display = false;
            }

            // Filtrage par recherche
            if (currentSearch) {
                var text = $(tr[i]).text().toLowerCase();
                if (text.indexOf(currentSearch.toLowerCase()) === -1) {
                    display = false;
                }
            }

            // Afficher ou masquer la ligne
            $(tr[i]).toggle(display);
        }
    }

    // Écouteurs d'événements pour mettre à jour les filtres et les appliquer
    ageFilter.slider({
        range: true,
        min: 12,
        max: 130,
        step: 1,
        values: [12, 130],
        change: function(event, ui) {
            currentFilters.age = ui.values;
            applyFilters();
        }
    });

    ratingFilter.slider({
        range: true,
        min: 0,
        max: 5,
        step: 0.5,
        values: [0, 5],
        change: function(event, ui) {
            currentFilters.rating = ui.values;
            applyFilters();
        }
    });

    // Nouveaux sliders
    ratingAFilter.slider({
        range: true,
        min: 0,
        max: 5,
        step: 0.5,
        values: [0, 5],
        change: function(event, ui) {
            currentFilters.ratingA = ui.values;
            applyFilters();
        }
    });

    ratingPFilter.slider({
        range: true,
        min: 0,
        max: 5,
        step: 0.5,
        values: [0, 5],
        change: function(event, ui) {
            currentFilters.ratingP = ui.values;
            applyFilters();
        }
    });

    ratingFFilter.slider({
        range: true,
        min: 0,
        max: 5,
        step: 0.5,
        values: [0, 5],
        change: function(event, ui) {
            currentFilters.ratingF = ui.values;
            console.log("Finan Values:", ui.values)
            applyFilters();
        }
    });

    positionFilter.addEventListener('change', function() {
        currentFilters.position = this.value;
        applyFilters();
    });

    contractFilter.slider({
        range: true,
        min: new Date().getFullYear() - 5,
        max: new Date().getFullYear() + 10,
        step: 1,
        values: [new Date().getFullYear() - 5, new Date().getFullYear() + 10],
        change: function(event, ui) {
            currentFilters.contract = ui.values;
            console.log("Year Values:", ui.values)
            applyFilters();
        }
    });

    searchFilter.addEventListener('input', function() {
        currentSearch = this.value.toLowerCase();
        applyFilters();
    });

    // Initialisation du tableau avec les valeurs actuelles des filtres
    applyFilters();
});

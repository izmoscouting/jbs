document.addEventListener('DOMContentLoaded', function() {
    var positionFilter = document.getElementById('positionFilter');
    var contractFilter = $("#contractSlider");
    var searchFilter = document.getElementById('search'); // Assurez-vous que l'ID est correct

    // Variables pour stocker les valeurs des filtres
    var currentFilters = {
        position: [],  // Utilisez un tableau pour stocker les positions sélectionnées
        contract: [new Date().getFullYear() - 1, new Date().getFullYear() + 3]
    };

    // Variable pour stocker la valeur de recherche
    var currentSearch = '';

    // Fonction pour appliquer tous les filtres
    function applyFilters() {
        var table = $(".table-striped");
        var tr = table.find("tr");

        for (var i = 1; i < tr.length; i++) {
            var display = true;

            // Filtrage par position
            var tdPosition = $(tr[i]).find("td:eq(4)");
            var position = tdPosition.length > 0 ? tdPosition.text() : "";
            
            // Vérifier si la position est dans les positions sélectionnées
            if (currentFilters.position.length > 0 && !currentFilters.position.includes(position)) {
                display = false;
            }

            // Filtrage par contrat
            var tdContract = $(tr[i]).find("td:eq(3)")
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

    positionFilter.addEventListener('change', function() {
        // Utilisez Array.from pour convertir la collection d'options en tableau
        currentFilters.position = Array.from(this.selectedOptions).map(option => option.value);
        applyFilters();
    });

    contractFilter.slider({
        range: true,
        min: new Date().getFullYear() - 2,
        max: new Date().getFullYear() + 3,
        step: 1,
        values: [new Date().getFullYear() - 2, new Date().getFullYear() + 3],
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

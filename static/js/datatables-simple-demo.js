document.addEventListener('DOMContentLoaded', function() {
    var ageFilter = document.getElementById('ageFilter');
    var ratingFilter = document.getElementById('ratingFilter');
    var positionFilter = document.getElementById('positionFilter');
    var searchFilter = document.getElementById('search'); // Assurez-vous que l'ID est correct

    // Variables pour stocker les valeurs des filtres
    var currentFilters = {
        age: ageFilter.value,
        rating: ratingFilter.value,
        position: positionFilter.value
    };

    // Variable pour stocker la valeur de recherche
    var currentSearch = '';

    // Fonction pour appliquer tous les filtres
    function applyFilters() {
        var table = document.querySelector(".table-striped");
        var tr = table.getElementsByTagName("tr");

        for (var i = 1; i < tr.length; i++) {
            var display = true;

            // Filtrage par âge
            var tdAge = tr[i].getElementsByTagName("td")[5];
            var age = tdAge ? parseInt(tdAge.textContent || tdAge.innerText) : null;
            if (currentFilters.age !== "" && (age === null || age < currentFilters.age)) {
                display = false;
            }

            // Filtrage par note
            var tdRating = tr[i].getElementsByTagName("td")[9];
            var ratingText = tdRating ? tdRating.textContent || tdRating.innerText : "";
            var rating = ratingText === "non calculable" ? -2 : parseFloat(ratingText.replace("R", ""));
            if (ratingText !== "non calculable" && currentFilters.rating !== "" && (isNaN(rating) || rating < currentFilters.rating)) {
                display = false;
            }

            // Filtrage par position
            var tdPosition = tr[i].getElementsByTagName("td")[1];
            var position = tdPosition ? tdPosition.textContent || tdPosition.innerText : "";
            if (currentFilters.position !== "" && position !== currentFilters.position) {
                display = false;
            }

            // Filtrage par recherche
            if (currentSearch) {
                var text = tr[i].textContent.toLowerCase() || tr[i].innerText.toLowerCase();
                if (!text.includes(currentSearch)) {
                    display = false;
                }
            }

            // Afficher ou masquer la ligne
            tr[i].style.display = display ? "" : "none";
        }
    }

    // Écouteurs d'événements pour mettre à jour les filtres et les appliquer
    ageFilter.addEventListener('input', function() {
        currentFilters.age = this.value;
        applyFilters();
    });

    ratingFilter.addEventListener('input', function() {
        currentFilters.rating = this.value;
        applyFilters();
    });

    positionFilter.addEventListener('change', function() {
        currentFilters.position = this.value;
        applyFilters();
    });

    searchFilter.addEventListener('input', function() {
        currentSearch = this.value.toLowerCase();
        applyFilters();
    });

    // Initialisation du tableau avec les valeurs actuelles des filtres
    applyFilters();
});

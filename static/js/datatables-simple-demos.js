document.addEventListener('DOMContentLoaded', function() {
    var searchFilter = document.getElementById('search'); // Assurez-vous que l'ID est correct

    // Variable pour stocker la valeur de recherche
    var currentSearch = '';

    // Fonction pour appliquer tous les filtres
    function applyFilters() {
        var table = document.querySelector(".table-striped");
        var tr = table.getElementsByTagName("tr");

        // Itération à travers toutes les lignes du tableau pour appliquer les filtres
        for (var i = 0; i < tr.length; i++) {
            // On commence par supposer que la ligne doit être affichée
            var display = true;

            if (currentSearch) {
                // Assurez-vous que la comparaison de recherche ne s'applique qu'aux lignes avec des données
                var td = tr[i].getElementsByTagName("td")[0]; // Exemple pour la première colonne, ajustez selon les besoins
                if (td) {
                    var text = td.textContent.toLowerCase() || td.innerText.toLowerCase();
                    if (!text.includes(currentSearch)) {
                        display = false;
                    }
                }
            }

            // Mise à jour de l'affichage de la ligne basée sur le filtre de recherche
            tr[i].style.display = display ? "" : "none";
        }
    }

    searchFilter.addEventListener('input', function() {
        currentSearch = this.value.toLowerCase();
        applyFilters();
    });

    // Initialisation du tableau avec les valeurs actuelles des filtres
    applyFilters();
});

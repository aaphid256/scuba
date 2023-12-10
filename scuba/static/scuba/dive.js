

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOMContentLoaded event fired.');

    const toggleNewDiveForm = document.getElementById('toggleNewDiveForm');
    const newDiveForm = document.getElementById('newDiveForm');

    toggleNewDiveForm.addEventListener('click', function () {
        newDiveForm.style.display = (newDiveForm.style.display === 'none') ? 'block' : 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const showNewDestinationForm = document.getElementById('showNewDestinationForm');
    const newDestinationForm = document.getElementById('newDestinationForm');

    showNewDestinationForm.addEventListener('click', function () {
        newDestinationForm.style.display = (newDestinationForm.style.display === 'none') ? 'block' : 'none';
    });
});


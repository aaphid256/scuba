document.addEventListener('DOMContentLoaded', function () {

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

document.addEventListener('DOMContentLoaded', function () {
    function editProfile(profileId) {
        // Example using jQuery
        $.ajax({
            url: '/get_profile_data/' + profileId + '/',
            type: 'GET',
            success: function (data) {
                // Populate the form fields with the retrieved data
                $('#id_functional_sac_rate').val(data.functional_sac_rate);
                $('#id_deco_sac_rate').val(data.deco_sac_rate);
                $('#id_min_gas_sac').val(data.min_gas_sac);
    
                // Display the form
                $('#id_profile_form').show();
            },
            error: function (error) {
                console.error('Error fetching profile data:', error);
            }
        });
    }
});


document.addEventListener('DOMContentLoaded', function () {
    const decoGassesDropdown = document.getElementById('decoGasses');
    const firstSwitchDepthContainer = document.getElementById('firstSwitchDepthContainer');
    const secondSwitchDepthContainer = document.getElementById('secondSwitchDepthContainer');

    function createSwitchDepthDropdown(labelText, id) {
        const label = document.createElement('label');
        label.textContent = labelText;
        
        const select = document.createElement('select');
        select.id = id;
        // Add options from 200 to 10 in increments of 10
        for (let depth = 200; depth >= 10; depth -= 10) {
            const option = document.createElement('option');
            option.value = depth;
            option.textContent = depth;
            select.appendChild(option);
        }

        return { label, select };
    }

    function showHideSwitchDepths() {
        const selectedGasses = decoGassesDropdown.value;
        if (selectedGasses === '1') {
            const { label, select } = createSwitchDepthDropdown('First Switch Depth', 'firstSwitchDepth');
            firstSwitchDepthContainer.innerHTML = '';
            firstSwitchDepthContainer.appendChild(label);
            firstSwitchDepthContainer.appendChild(select);

            secondSwitchDepthContainer.innerHTML = ''; // Clear the second dropdown
        } else if (selectedGasses === '2') {
            const firstDropdown = createSwitchDepthDropdown('First Switch Depth', 'firstSwitchDepth');
            const secondDropdown = createSwitchDepthDropdown('Second Switch Depth', 'secondSwitchDepth');

            firstSwitchDepthContainer.innerHTML = '';
            firstSwitchDepthContainer.appendChild(firstDropdown.label);
            firstSwitchDepthContainer.appendChild(firstDropdown.select);

            secondSwitchDepthContainer.innerHTML = '';
            secondSwitchDepthContainer.appendChild(secondDropdown.label);
            secondSwitchDepthContainer.appendChild(secondDropdown.select);
        } else {
            firstSwitchDepthContainer.innerHTML = ''; // No gasses selected, clear the containers
            secondSwitchDepthContainer.innerHTML = '';
        }
    }

    decoGassesDropdown.addEventListener('change', showHideSwitchDepths);
    showHideSwitchDepths();  // Initialize visibility based on initial value
});


document.addEventListener('DOMContentLoaded', function () {


    function updateBackgassCalculations() {
        const cuFtInput = document.getElementById('cuFt');
        const pressureInput = document.getElementById('pressure');
        const fillPressureInput = document.getElementById('fillPressure');
        const psiPerCuFtOutput = document.getElementById('psiPerCuFt');
        const actCuFtOutput = document.getElementById('actCuFt');

        const cuFt = parseFloat(cuFtInput.value) || 0;
        const pressure = parseFloat(pressureInput.value) || 0;
        const fillPressure = parseFloat(fillPressureInput.value) || 0;

        const psiPerCuFt = pressure / cuFt;
        const actCuFt = fillPressure / psiPerCuFt;

        psiPerCuFtOutput.textContent = `PSI/cft: ${psiPerCuFt.toFixed(2)}`;
        actCuFtOutput.textContent = `Act. Cu Ft: ${actCuFt.toFixed(2)}`;
    }

    document.getElementById('cuFt').addEventListener('input', updateBackgassCalculations);
    document.getElementById('pressure').addEventListener('input', updateBackgassCalculations);
    document.getElementById('fillPressure').addEventListener('input', updateBackgassCalculations);

    
});

document.addEventListener('DOMContentLoaded', function () {
    // Your existing JavaScript code

    function updateDecoGasCalculations(decoGasIndex) {
        const cuFtInput = document.getElementById(`decoCuFt${decoGasIndex}`);
        const pressureInput = document.getElementById(`decoPressure${decoGasIndex}`);
        const fillPressureInput = document.getElementById(`decoFillPressure${decoGasIndex}`);
        const psiPerCuFtOutput = document.getElementById(`decoPsiPerCuFt${decoGasIndex}`);
        const actCuFtOutput = document.getElementById(`decoActCuFt${decoGasIndex}`);

        const cuFt = parseFloat(cuFtInput.value) || 0;
        const pressure = parseFloat(pressureInput.value) || 0;
        const fillPressure = parseFloat(fillPressureInput.value) || 0;

        const psiPerCuFt = pressure / cuFt;
        const actCuFt = fillPressure / psiPerCuFt;

        psiPerCuFtOutput.textContent = `PSI/cft: ${psiPerCuFt.toFixed(2)}`;
        actCuFtOutput.textContent = `Act. Cu Ft: ${actCuFt.toFixed(2)}`;
    }

    function handleDecoGassesChange() {
        const decoGassesDropdown = document.getElementById('decoGasses');
        const numDecoGasses = parseInt(decoGassesDropdown.value);

        const decoGassesContainer = document.getElementById('decoGassesContainer');
        decoGassesContainer.innerHTML = ''; // Clear previous inputs

        for (let i = 0; i < numDecoGasses; i++) {
            // Create input fields for each deco gas
            const div = document.createElement('div');
            div.innerHTML = `
                <h5>Deco Gas ${i + 1}</h5>
                <label for="decoCuFt${i}">Cu Ft</label>
                <input type="number" id="decoCuFt${i}" step="0.1" placeholder="Cu Ft" required>

                <label for="decoPressure${i}">Pressure</label>
                <input type="number" id="decoPressure${i}" step="0.1" placeholder="Pressure" required>
                <span id="decoPsiPerCuFt${i}"></span>

                <label for="decoFillPressure${i}">Fill Pressure</label>
                <input type="number" id="decoFillPressure${i}" step="0.1" placeholder="Fill Pressure" required>
                <span id="decoActCuFt${i}"></span>

                <!-- Dropdown for selecting gas type -->
                <label for="decoGasType${i}">Gas Type</label>
                <select id="decoGasType${i}" required>
                    <option value="ean100">EAN 100</option>
                    <option value="ean50">EAN 50</option>
                </select>
            `;

            // Append the div to the container
            decoGassesContainer.appendChild(div);

            // Attach event listeners for dynamic updates
            const cuFtInput = document.getElementById(`decoCuFt${i}`);
            const pressureInput = document.getElementById(`decoPressure${i}`);
            const fillPressureInput = document.getElementById(`decoFillPressure${i}`);

            cuFtInput.addEventListener('input', () => updateDecoGasCalculations(i));
            pressureInput.addEventListener('input', () => updateDecoGasCalculations(i));
            fillPressureInput.addEventListener('input', () => updateDecoGasCalculations(i));
        }
    }
            // Attach event listener for decoGasses dropdown change
            const decoGassesDropdown = document.getElementById('decoGasses');
            decoGassesDropdown.addEventListener('change', handleDecoGassesChange);

    updateDivePlanTable();

});


document.addEventListener('DOMContentLoaded', function () { 
    // Add event listener for O2 level input
    const o2LevelInput = document.getElementById('o2Level');
    o2LevelInput.addEventListener('input', calculateMOD);
  
    // Function to calculate and display Max Operating Depth (MOD)
    function calculateMOD() {
      const o2Level = parseFloat(o2LevelInput.value);
  
      // Check if the input is a valid number between 21 and 100
      if (!isNaN(o2Level) && o2Level >= 21 && o2Level <= 100) {
        const mod = calculateModValue(o2Level);
        displayMOD(mod);
      } else {
        displayMODError();
      }
    }
  
    function calculateModValue(o2Level) {
        // Convert O2 level to decimal
        const o2Decimal = o2Level / 100;
    
        // Calculate MOD and round to the nearest whole number
        const mod = Math.round(33 * (1.4 / o2Decimal - 1));
        return mod;
      }
    
      function displayMOD(mod) {
        const modOutput = document.getElementById('modOutput');
        modOutput.textContent = `Max Operating Depth (MOD): ${mod} feet`;
      }
    
      function displayMODError() {
        const modOutput = document.getElementById('modOutput');
        modOutput.textContent = 'Invalid O2 level. Please enter a number between 21 and 100.';
      }

      // Add event listener for depth input
  const depthInput = document.getElementById('depthInput');
  depthInput.addEventListener('input', calculateBestMix);

  // Function to calculate and display Best Mix
  function calculateBestMix() {
    const depth = parseFloat(depthInput.value);

    // Check if the input is a valid number between 13 and 186
    if (!isNaN(depth) && depth >= 13 && depth <= 186) {
      const bestMix = calculateBestMixValue(depth);
      displayBestMix(depth, bestMix);
    } else {
      displayBestMixError();
    }
  }

  function calculateBestMixValue(depth) {
    // Calculate Best Mix value
    const bestMix = (1.4 / ((depth / 33) + 1)) * 100;
    return Math.round(bestMix);
  }

  function displayBestMix(depth, bestMix) {
    const bestMixOutput = document.getElementById('bestMixOutput');
    bestMixOutput.textContent = `For ${depth} feet: Use EAN ${bestMix}`;
  }

  function displayBestMixError() {
    const bestMixOutput = document.getElementById('bestMixOutput');
    bestMixOutput.textContent = 'Invalid depth. Please enter a number between 13 and 186.';
  }

});
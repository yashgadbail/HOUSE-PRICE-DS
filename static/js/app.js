// Global variables
const baseUrl = 'http://127.0.0.1:5000';
let locations = [];

// DOM elements
const locationSelect = document.getElementById('location');
const sqftInput = document.getElementById('sqft');
const bhkSelect = document.getElementById('bhk');
const bathSelect = document.getElementById('bath');
const predictionForm = document.getElementById('prediction-form');
const resultCard = document.querySelector('.result-card');
const estimatedPriceElement = document.getElementById('estimated-price');

// Load locations when the page loads
document.addEventListener('DOMContentLoaded', () => {
    fetchLocations();
});

// Function to fetch locations from the API
async function fetchLocations() {
    try {
        const response = await fetch(`${baseUrl}/get_location_names`);
        const data = await response.json();
        
        locations = data.locations;
        populateLocationDropdown(locations);
    } catch (error) {
        console.error('Error fetching locations:', error);
        showError('Failed to load locations. Please refresh the page.');
    }
}

// Function to populate the location dropdown
function populateLocationDropdown(locations) {
    // Clear existing options except the first one
    locationSelect.innerHTML = '<option value="" selected disabled>Select a location</option>';
    
    // Sort locations alphabetically
    locations.sort();
    
    // Add options for each location
    locations.forEach(location => {
        const option = document.createElement('option');
        option.value = location;
        option.textContent = location;
        locationSelect.appendChild(option);
    });
}

// Event listener for form submission
predictionForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Validate inputs
    if (!validateInputs()) {
        return;
    }
    
    // Get form values
    const formData = {
        location: locationSelect.value,
        total_sqft: sqftInput.value,
        bhk: bhkSelect.value,
        bath: bathSelect.value
    };
    
    // Send prediction request
    try {
        const response = await fetch(`${baseUrl}/predict_home_price`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error('Failed to get prediction');
        }
        
        const data = await response.json();
        displayResult(data.estimated_price);
    } catch (error) {
        console.error('Error making prediction:', error);
        showError('Failed to get prediction. Please try again.');
    }
});

// Function to validate form inputs
function validateInputs() {
    if (!locationSelect.value) {
        showError('Please select a location');
        return false;
    }
    
    if (!sqftInput.value || sqftInput.value < 100) {
        showError('Please enter a valid square footage (minimum 100)');
        return false;
    }
    
    return true;
}

// Function to display the prediction result
function displayResult(price) {
    // Format the price to 2 decimal places
    const formattedPrice = parseFloat(price).toFixed(2);
    
    // Update the result element
    estimatedPriceElement.textContent = formattedPrice;
    
    // Show the result card
    resultCard.classList.remove('d-none');
    resultCard.classList.add('show');
    
    // Scroll to the result card
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Function to show error message
function showError(message) {
    // You can replace this with a more sophisticated error handling
    alert(message);
}

// Add event listener for input validation
sqftInput.addEventListener('input', () => {
    if (sqftInput.value < 100) {
        sqftInput.classList.add('is-invalid');
    } else {
        sqftInput.classList.remove('is-invalid');
    }
});

// Add event listener to check if bathrooms are more than BHK
bathSelect.addEventListener('change', () => {
    if (parseInt(bathSelect.value) > parseInt(bhkSelect.value)) {
        showError('Warning: Number of bathrooms is usually not more than number of bedrooms');
    }
});
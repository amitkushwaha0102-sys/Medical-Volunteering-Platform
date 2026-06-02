const API_URL = 'http://13.205.15.119/api';

// Patient form
const patientForm = document.getElementById('patientForm');
if (patientForm) {
    patientForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = {
            name: document.getElementById('name').value,
            father_name: document.getElementById('father_name').value,
            city: document.getElementById('city').value,
            disease: document.getElementById('disease').value,
            contact_number: document.getElementById('contact_number').value
        };
        const res = await fetch(`${API_URL}/register-patient`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await res.json();
        document.getElementById('message').innerText = result.message;
    });
}

// Volunteer form
const volunteerForm = document.getElementById('volunteerForm');
if (volunteerForm) {
    volunteerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = {
            name: document.getElementById('name').value,
            father_name: document.getElementById('father_name').value,
            city: document.getElementById('city').value,
            contact_number: document.getElementById('contact_number').value,
            specialization: document.getElementById('specialization').value
        };
        const res = await fetch(`${API_URL}/register-volunteer`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await res.json();
        document.getElementById('message').innerText = result.message;
    });
}

// Search volunteers
async function searchVolunteers() {
    const city = document.getElementById('citySearch').value;
    const res = await fetch(`${API_URL}/volunteers/${city}`);
    const volunteers = await res.json();
    const results = document.getElementById('results');
    if (volunteers.length === 0) {
        results.innerHTML = '<p>No volunteers found in this city.</p>';
        return;
    }
    results.innerHTML = volunteers.map(v => `
        <div class="volunteer-card">
            <h3>${v.name}</h3>
            <p>Specialization: ${v.specialization}</p>
            <p>Contact: ${v.contact_number}</p>
        </div>
    `).join('');
}
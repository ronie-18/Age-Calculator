document.getElementById('ageForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const dob = new Date(document.getElementById('dob').value);
    const now = new Date();

    let years = now.getFullYear() - dob.getFullYear();
    let months = now.getMonth() - dob.getMonth();
    let days = now.getDate() - dob.getDate();
    let hours = now.getHours() - dob.getHours();

    if (hours < 0) {
        hours += 24;
        days--;
    }
    if (days < 0) {
        months--;
        const prevMonth = new Date(now.getFullYear(), now.getMonth(), 0);
        days += prevMonth.getDate();
    }
    if (months < 0) {
        months += 12;
        years--;
    }

    document.getElementById('years').innerText = `${years} Years`;
    document.getElementById('months').innerText = `${months} Months`;
    document.getElementById('days').innerText = `${days} Days`;
    document.getElementById('hours').innerText = `${hours} Hours`;
});

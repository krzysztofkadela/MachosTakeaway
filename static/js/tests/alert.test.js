import '@testing-library/jest-dom';

// alert.test.js
// Mock the setTimeout function
jest.useFakeTimers();

document.body.innerHTML = `
    <div class="auto-close-alert show">Alert 1</div>
    <div class="auto-close-alert show">Alert 2</div>
`;

const hideAlerts = () => {
    const alerts = document.querySelectorAll('.auto-close-alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show'); // Remove the 'show' class to hide the alert
            alert.classList.add('fade'); // Add 'fade' class to smoothly fade it out
            // Remove from DOM
            setTimeout(() => {
                alert.remove(); // remove the alert from the DOM
            }, 500); // for css transition
        }, 5000); // Time in milliseconds (5000 ms = 5 seconds)
    });
};

describe('Auto-close alerts', () => {
    test('should hide alerts after 5 seconds', () => {
        hideAlerts(); // Call the function to hide alerts

        // Fast forward time by 5 seconds
        jest.advanceTimersByTime(5000);

        const alerts = document.querySelectorAll('.auto-close-alert');
        alerts.forEach(alert => {
            expect(alert.classList.contains('show')).toBe(false);
            expect(alert.classList.contains('fade')).toBe(true);
        });
        
        // Fast forward an additional 500 milliseconds to check if alerts are removed
        jest.advanceTimersByTime(500);

        alerts.forEach(alert => {
            expect(alert).not.toBeInTheDocument(); // Check that alert is removed from the DOM
        });
    });
});
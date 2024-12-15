// jest.config.js
module.exports = {
    testEnvironment: 'jest-environment-jsdom',
    testMatch: ['**/static/js/tests/**/*.test.js'],
    setupFilesAfterEnv: ['<rootDir>/static/js/tests/setupTests.js'],
    transform: {
        '^.+\\.jsx?$': 'babel-jest', // Transpile JS/JSX files
    },
};
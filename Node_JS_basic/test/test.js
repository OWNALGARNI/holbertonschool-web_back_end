const assert = require('assert');
const displayMessage = require('../0-console');

describe('Test displayMessage', () => {
  it('should run without error', () => {
    displayMessage('Hello');
  });
});
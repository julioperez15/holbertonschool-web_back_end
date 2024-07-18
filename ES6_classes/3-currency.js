export default class Currency {
    constructor(code, name) {
      // Type checks
      if (typeof code !== 'string') {
        throw new TypeError('Code must be a string');
      }
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
  
      // Assign attributes
      this._code = code;
      this._name = name;
    }
  
    // Getter and Setter for code
    get code() {
      return this._code;
    }
  
    set code(code) {
      if (typeof code !== 'string') {
        throw new TypeError('Code must be a string');
      }
      this._code = code;
    }
  
    // Getter and Setter for name
    get name() {
      return this._name;
    }
  
    set name(name) {
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
      this._name = name;
    }
  
    // Method to display the full currency
    displayFullCurrency() {
      return `${this._name} (${this._code})`;
    }
  }
  
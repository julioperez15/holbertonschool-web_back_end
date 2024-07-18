export default class Building {
    constructor(sqft) {
      // Type check
      if (typeof sqft !== 'number') {
        throw new TypeError('Square footage must be a number');
      }
  
      // Assign attribute
      this._sqft = sqft;
  
      // Ensure abstract method is implemented
      if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  
    // Getter for sqft
    get sqft() {
      return this._sqft;
    }
  }
  
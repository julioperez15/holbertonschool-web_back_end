// Define the class
export default class HolbertonCourse {
    constructor(name, length, students) {
      // Type checks
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
      if (typeof length !== 'number') {
        throw new TypeError('Length must be a number');
      }
      if (!Array.isArray(students)) {
        throw new TypeError('Students must be an array of strings');
      }
      if (!students.every(student => typeof student === 'string')) {
        throw new TypeError('Students must be an array of strings');
      }
      
      // Assign attributes
      this._name = name;
      this._length = length;
      this._students = students;
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
  
    // Getter and Setter for length
    get length() {
      return this._length;
    }
  
    set length(length) {
      if (typeof length !== 'number') {
        throw new TypeError('Length must be a number');
      }
      this._length = length;
    }
  
    // Getter and Setter for students
    get students() {
      return this._students;
    }
  
    set students(students) {
      if (!Array.isArray(students)) {
        throw new TypeError('Students must be an array of strings');
      }
      if (!students.every(student => typeof student === 'string')) {
        throw new TypeError('Students must be an array of strings');
      }
      this._students = students;
    }
  }
  
export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
      let task = true; // This variable declaration is scoped to the if block
      const task2 = false; // This variable is also scoped to the if block
    }
  
    return [task, task2];
  }
  
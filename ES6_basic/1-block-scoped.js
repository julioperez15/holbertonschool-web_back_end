export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // No need to re-declare new variables in the if block because they aren't used
  }

  return [task, task2];
}

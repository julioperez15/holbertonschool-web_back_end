export const taskFirst = () => 'I prefer const when I can.';

export const getLast = () => ' is okay';

export const taskNext = () => {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
};

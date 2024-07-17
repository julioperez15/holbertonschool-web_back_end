const taskFirstMessage = 'I prefer const when I can.';

export const taskFirst = () => taskFirstMessage;

export const getLast = () => ' is okay';

export const taskNext = () => {
  let combination = 'But sometimes let';
  combination += getLast();
  return combination;
};
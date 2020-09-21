#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const listReverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listReverse.push(list[i]);
  }
  return listReverse;
};

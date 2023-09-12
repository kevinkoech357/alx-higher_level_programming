#!/usr/bin/node

// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence

const dataModule = require('./101-data');

// extracting to dictionary

const occurrencesByUser = dataModule.dict;

// function to compute a new dictionary of user ids by occurrences

function computeNewDict (occurrencesDict) {
  // initialize an empty dict
  const usersByOccurence = {};

  for (const [user, occurrences] of Object.entries(occurrencesDict)) {
    if (!usersByOccurence[occurrences]) {
      usersByOccurence[occurrences] = user;
    } else {
      usersByOccurence[occurrences].push(user);
    }
  }

  return usersByOccurence;
}

const usersByOccurence = computeNewDict(occurrencesByUser);
console.log(usersByOccurence);

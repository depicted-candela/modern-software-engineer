"use strict";
// Movie with complete data
const movie1 = {
    title: "Inception",
    director: "Christopher Nolan",
    releaseYear: 2010,
    boxOffice: {
        budget: 160000000,
        gross: 829900000
    }
};
// Movie without box office data
const movie2 = {
    title: "Primer",
    director: "Shane Carruth",
    releaseYear: 2004
};
;
const interfacedMovie1 = movie1;
const interfacedMovie2 = movie2;
console.log(interfacedMovie1);
console.log(interfacedMovie2);

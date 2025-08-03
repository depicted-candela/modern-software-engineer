// Movie with complete data
var movie1 = {
    title: "Inception",
    director: "Christopher Nolan",
    releaseYear: 2010,
    boxOffice: {
        budget: 160000000,
        gross: 829900000
    }
};
// Movie without box office data
var movie2 = {
    title: "Primer",
    director: "Shane Carruth",
    releaseYear: 2004
};
;
var interfacedMovie1 = movie1;
var interfacedMovie2 = movie2;
console.log(interfacedMovie1);
console.log(interfacedMovie2);

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

interface Movie {
    title: string;
    director: string;
    releaseYear: number;
    boxOffice?: {budget: number; gross: number};
};

const interfacedMovie1: Movie = movie1;
const interfacedMovie2: Movie = movie2;

console.log(interfacedMovie1);
console.log(interfacedMovie2);
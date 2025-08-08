import { log } from 'console';

const numericData: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

type NumberPredicate = {
    (n: number): boolean;
}

const filterEvenNumber: NumberPredicate = (n: number) => n % 2 == 0;
const filterGreaterThan5Number: NumberPredicate = (n: number) => n > 5;

function filterData(
    data: number[], 
    predicate: NumberPredicate
): number[] {
    const filtered_records: number[] = [];
    data.forEach((record) => predicate(record));
    for (const record of data) if (predicate(record)) filtered_records.push(record);
    return filtered_records;
}

const evenNumbers = filterData(numericData, filterEvenNumber);
const greaterThan5Numbers = filterData(numericData, filterGreaterThan5Number);

log(evenNumbers);
log(greaterThan5Numbers);
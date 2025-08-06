import { log } from "console";

const singleString = "hello world";
const stringArray = ["typescript", "is", "powerful"];

function formatInput(string: string): string;
function formatInput(string: string[]): string;

function formatInput(string: string | string[]) {
    if (typeof string == 'string') return string.toUpperCase();
    return string.join(", ");
}

log(formatInput(singleString));
log(formatInput(stringArray));
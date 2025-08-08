"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const console_1 = require("console");
class LibraryItem {
    constructor(title) {
        this.libraryId = LibraryItem.nextId;
        LibraryItem.nextId++;
        this.title = title;
    }
}
LibraryItem.nextId = 1;
class Book extends LibraryItem {
    constructor(title, author) {
        super(title);
        this.author = author;
        this.isBorrowed = false;
    }
    borrow() {
        if (!this.isBorrowed)
            this.isBorrowed = true;
    }
    returnItem() {
        this.isBorrowed = false;
    }
    ;
    getDetails() {
        return `Title: ${this.title}, Author: ${this.author}, Status: ${this.isBorrowed}`;
    }
}
class Magazine extends LibraryItem {
    constructor(title, issueNumber) {
        super(title);
        this.issueNumber = issueNumber;
        this.isBorrowed = false;
    }
    borrow() {
        if (!this.isBorrowed)
            this.isBorrowed = true;
    }
    returnItem() {
        this.isBorrowed = false;
    }
    ;
    getDetails() {
        return `Title: ${this.title}, Issue Number: ${this.issueNumber}, Status: ${this.isBorrowed}`;
    }
}
const bookData = { title: "Designing Data-Intensive Applications", author: "Martin Kleppmann" };
const magazineData = { title: "Communications of the ACM", issue: 12 };
const book = new Book(bookData.title, bookData.author);
const magazine = new Magazine(magazineData.title, magazineData.issue);
(0, console_1.log)(book.getDetails());
(0, console_1.log)(magazine.getDetails());
book.borrow();
(0, console_1.log)(`Borrowed book details ${book.getDetails()}`);
book.borrow();
(0, console_1.log)(`Already borrowed item borrowed again: ${book}, details: ${book.getDetails()}`);

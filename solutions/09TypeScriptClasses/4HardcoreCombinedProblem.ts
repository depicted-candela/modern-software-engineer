import { log } from "console";

interface ILendable {
    borrow: () => void;
    returnItem: () => void;
}

abstract class LibraryItem {
    public readonly libraryId: number;
    protected static nextId = 1;
    public title: string;
    constructor(title: string) {
        this.libraryId = LibraryItem.nextId;
        LibraryItem.nextId++;
        this.title = title;
    }
    public abstract getDetails(): string;
}

class Book extends LibraryItem implements ILendable {
    private author: string;
    protected isBorrowed: boolean;
    constructor(title: string, author: string) {
        super(title);
        this.author = author;
        this.isBorrowed = false;
    }
    public borrow() {
        if (!this.isBorrowed) this.isBorrowed = true;
    }
    public returnItem() {
        this.isBorrowed = false;
    };
    public getDetails(): string {
        return `Title: ${this.title}, Author: ${this.author}, Status: ${this.isBorrowed}`;
    }
}

class Magazine extends LibraryItem implements ILendable {
    private issueNumber: number;
    protected isBorrowed: boolean;
    constructor(title: string, issueNumber: number) {
        super(title);
        this.issueNumber = issueNumber;
        this.isBorrowed = false;
    }
    public borrow() {
        if (!this.isBorrowed) this.isBorrowed = true;
    }
    public returnItem() {
        this.isBorrowed = false;
    };
    public getDetails(): string {
        return `Title: ${this.title}, Issue Number: ${this.issueNumber}, Status: ${this.isBorrowed}`;
    }
}

const bookData = { title: "Designing Data-Intensive Applications", author: "Martin Kleppmann" };
const magazineData = { title: "Communications of the ACM", issue: 12 };

const book = new Book(bookData.title, bookData.author);
const magazine = new Magazine(magazineData.title, magazineData.issue);

log(book.getDetails());
log(magazine.getDetails());

book.borrow();
log(`Borrowed book details ${book.getDetails()}`);

book.borrow();
log(`Already borrowed item borrowed again: ${book}, details: ${book.getDetails()}`);

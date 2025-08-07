"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var console_1 = require("console");
var LibraryItem = /** @class */ (function () {
    function LibraryItem(title) {
        this.libraryId = LibraryItem.nextId;
        LibraryItem.nextId++;
        this.title = title;
    }
    LibraryItem.nextId = 1;
    return LibraryItem;
}());
var Book = /** @class */ (function (_super) {
    __extends(Book, _super);
    function Book(title, author) {
        var _this = _super.call(this, title) || this;
        _this.author = author;
        _this.isBorrowed = false;
        return _this;
    }
    Book.prototype.borrow = function () {
        if (!this.isBorrowed)
            this.isBorrowed = true;
    };
    Book.prototype.returnItem = function () {
        this.isBorrowed = false;
    };
    ;
    Book.prototype.getDetails = function () {
        return "Title: ".concat(this.title, ", Author: ").concat(this.author, ", Status: ").concat(this.isBorrowed);
    };
    return Book;
}(LibraryItem));
var Magazine = /** @class */ (function (_super) {
    __extends(Magazine, _super);
    function Magazine(title, issueNumber) {
        var _this = _super.call(this, title) || this;
        _this.issueNumber = issueNumber;
        _this.isBorrowed = false;
        return _this;
    }
    Magazine.prototype.borrow = function () {
        if (!this.isBorrowed)
            this.isBorrowed = true;
    };
    Magazine.prototype.returnItem = function () {
        this.isBorrowed = false;
    };
    ;
    Magazine.prototype.getDetails = function () {
        return "Title: ".concat(this.title, ", Issue Number: ").concat(this.issueNumber, ", Status: ").concat(this.isBorrowed);
    };
    return Magazine;
}(LibraryItem));
var bookData = { title: "Designing Data-Intensive Applications", author: "Martin Kleppmann" };
var magazineData = { title: "Communications of the ACM", issue: 12 };
var book = new Book(bookData.title, bookData.author);
var magazine = new Magazine(magazineData.title, magazineData.issue);
(0, console_1.log)(book.getDetails());
(0, console_1.log)(magazine.getDetails());
book.borrow();
(0, console_1.log)("Borrowed book details ".concat(book.getDetails()));
book.borrow();
(0, console_1.log)("Already borrowed item borrowed again: ".concat(book, ", details: ").concat(book.getDetails()));

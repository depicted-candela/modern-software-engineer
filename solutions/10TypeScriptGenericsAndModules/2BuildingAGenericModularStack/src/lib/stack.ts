class Stack<T> {
    public items: T[] = [];
    push(item: T): void {
        this.items.push(item);
    }
    pop(): T | undefined {
        return this.items.pop();
    }
    peek(): T | undefined {
        return this.items[0];
    }
    isEmpty(): boolean {
        return this.items.length == 0;
    }
    size(): number {
        return this.items.length;
    }
}

export default Stack;
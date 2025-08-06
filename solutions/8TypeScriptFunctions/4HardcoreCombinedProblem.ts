interface User {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
}

const users: User[] = [
    { 
        id: 1, 
        name: "Alice", 
        email: "alice@example.com", 
        isActive: true 
    },
    { 
        id: 2, 
        name: "Bob", 
        email: "bob@example.com", 
        isActive: false 
    },
    { 
        id: 3, 
        name: "Charlie", 
        email: "charlie@example.com", 
        isActive: true 
    },
];

// Type alias for any transformation function
type Transform<T, U> = (data: T) => U;

// Default callback if none is provided
const defaultCallback = (result: any) => console.log("Pipeline Result:", result);

// Overload 1: Immediate execution
function createDataPipeline<T>(
  initialData: T[],
  ...transformers: Transform<any, any>[]
): void;

// Overload 2: Deferred execution (returns a new function)
function createDataPipeline<T, U>(
  ...transformers: Transform<any, any>[]
): (initialData: T[], onComplete?: (finalData: U) => void) => void;

// Implementation
function createDataPipeline(
  ...args: any[]
): void | ((initialData: any[], onComplete?: (finalData: any) => void) => void) {
  // Check if the first argument is data (for immediate execution)
  const isImmediate = Array.isArray(args[0]);
  const transformers: Transform<any, any>[] = isImmediate ? args.slice(1) : args;
  
  const pipelineLogic = (
    initialData: any[],
    onComplete: (finalData: any) => void = defaultCallback
  ): any => {
    const result = transformers.reduce(
      (currentData, transformer) => transformer(currentData), initialData
    )
    onComplete(result);
  }

  if (isImmediate) {
    pipelineLogic(args[0]);
    return;
  } else {
    return pipelineLogic;
  }
}

const filterActive: Transform<User[], User[]> = (data) => data.filter((u) => u.isActive);
const getEmails: Transform<User[], string[]> = (data) => data.map(u => u.email);
const countItems: Transform<User[], void> = (data) => console.log(`There exists ${data.length} items`);




// --- Usage 1: Immediate Execution ---
console.log("--- Immediate Execution ---");

createDataPipeline(users, filterActive, getEmails, countItems);

createDataPipeline(users, filterActive, getEmails, countItems); // Uses default console.log callback

// --- Usage 2: Deferred Execution ---
console.log("\n--- Deferred Execution ---");



const reusablePipeline = createDataPipeline<User, User>(filterActive);

reusablePipeline(users);



const nameToUppercase: Transform<User[], { name: string }[]> = (data) => 
  data.map(u => ({ name: u.name.toUpperCase() }));



const reusablePipeline1 = createDataPipeline<User, { name: string }[]>(
  nameToUppercase
);



reusablePipeline1(users, (finalData) => {
  console.log("Transformed User Names:", finalData);
});

const reusablePipeline2 = createDataPipeline<User, { name: string }[]>(
  filterActive
);

reusablePipeline2(users, (finalData) => {
  console.log("Transformed User Names:", finalData);
});

const reusablePipeline3 = createDataPipeline<User, { name: string }[]>(
  getEmails
);

reusablePipeline3(users, (finalData) => {
  console.log("Transformed User Names:", finalData);
});
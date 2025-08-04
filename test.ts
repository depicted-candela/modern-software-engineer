// --- Type Definitions ---
type Transformer<T, U> = (data: T) => U;

// --- Artificial Data & Transformers ---
interface RawLog { timestamp: number; level: 'INFO' | 'WARN' | 'ERROR'; message: string; }
const rawLogs: RawLog[] = [
  { timestamp: 1, level: 'INFO', message: 'User logged in' },
  { timestamp: 2, level: 'ERROR', message: 'Database connection failed' },
  { timestamp: 3, level: 'WARN', message: 'API rate limit approaching' },
];

const filterErrors: Transformer<RawLog[], RawLog[]> = (logs) => logs.filter(l => l.level === 'ERROR');
const extractMessages: Transformer<RawLog[], string[]> = (logs) => logs.map(l => l.message);
const createReport: Transformer<string[], string> = (msgs) => `Critical Report:\n- ${msgs.join('\n- ')}`;

// --- Overloaded Pipeline Function ---
function createDataPipeline<T, U>(initialData: T, ...transformers: Transformer<any, any>[]): U;
function createDataPipeline<T, U>(...transformers: Transformer<any, any>[]): (initialData: T) => U;

// --- Implementation ---
function createDataPipeline(...args: any[]): any {
  const isImmediate = !(typeof args[0] === 'function');
  const transformers: Transformer<any, any>[] = isImmediate ? args.slice(1) : args;

  const pipelineExecutor = (initialData: any) => {
    return transformers.reduce((data, transform) => transform(data), initialData);
  };

  return isImmediate ? pipelineExecutor(args[0]) : pipelineExecutor;
}

// --- Usage 1: Immediate Execution ---
console.log("--- IMMEDIATE EXECUTION ---");
const report = createDataPipeline(rawLogs, filterErrors, extractMessages, createReport);
console.log(report);
// Output: Critical Report:
// - Database connection failed

// --- Usage 2: Deferred Execution (Building a reusable tool) ---
console.log("\n--- DEFERRED EXECUTION ---");
const warningMessageExtractor = createDataPipeline(
  (logs: RawLog[]) => logs.filter(log => log.level === 'WARN'),
  extractMessages // Re-using a transformer
);

const warningMessages = warningMessageExtractor(rawLogs);
console.log("Reusable Pipeline Result:", warningMessages);
// Output: Reusable Pipeline Result: ["API rate limit approaching"]
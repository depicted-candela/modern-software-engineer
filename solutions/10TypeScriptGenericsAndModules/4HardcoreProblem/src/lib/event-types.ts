export default interface EventMap {
  'user:created': { userId: number; name: string; timestamp: Date };
  'user:deleted': { userId: number; timestamp: Date };
  'order:placed': { orderId: string; amount: number; userId: number };
}
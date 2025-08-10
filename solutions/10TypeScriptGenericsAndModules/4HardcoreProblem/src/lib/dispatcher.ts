type Callback<T> = (payload: T) => void;

export default class EventDispatcher<T extends object> {
    private listener : {[S in keyof T]?: Callback<T[S]>[]} = {}

    on<S extends keyof T>(eventName: S, callback: (payload: T[S]) => void): void {
        (this.listener[eventName] = this.listener[eventName] || []).push(callback);
    }

    dispatch<S extends keyof T>(eventName: S, payload: T[S]): void {
        this.listener[eventName]?.forEach(subscriber => subscriber(payload));
    }
}
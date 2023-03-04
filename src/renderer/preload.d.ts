import {Channels} from 'main/preload';

declare global {
    interface Window {
        electron: {
            ipcRenderer: {
                sendMessage(channel: Channels, args: unknown[]): void;
                on(
                    channel: Channels,
                    func: (...args: unknown[]) => void
                ): (() => void) | undefined;
                once(channel: Channels, func: (...args: unknown[]) => void): void;
            };
            getDir(): undefined | string,
            isPath(string: string): boolean,
            scanDirectory(directoryPath: string): string[],
        };
    }
}

export {};

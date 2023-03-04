import {Dirent} from "fs";
import * as fs from 'node:fs'

/**
 * gets all files of a certain type in a given directory and its subdirectories
 *
 * @param dir
 * @param recursive
 */
export const getFiles = (dir: string, recursive: boolean = false): string[] => {
    const files: Dirent[] = fs.readdirSync(dir, {
        withFileTypes: true,
    })
    let fileArray: string[] = []

    for (const file of files) {
        if (file.isDirectory() && recursive) {
            fileArray = [
                ...fileArray,
                ...getFiles(`${dir}/${file.name}`)
            ]
        } else {
            fileArray.push(`${dir}/${file.name}`)
        }
    }
    return fileArray
}
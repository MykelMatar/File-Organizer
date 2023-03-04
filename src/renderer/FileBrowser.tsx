import {AiFillFolderOpen} from "react-icons/ai";
import React, {SetStateAction, useEffect, useState} from "react";

const FileBrowser = () => {
    const initialText: string = 'File Directory'
    const [inputText, setInputText] = useState(initialText)
    const [files, setFiles]: string[] | SetStateAction<any> = useState([])
    const [checked, setChecked]: string[] | SetStateAction<any> = useState(false)
    const [expanded, setExpanded]: string[] | SetStateAction<any> = useState([])
    const [fileTree, setFileTree] = useState(
        <h1 className="text-white">
            File Tree
        </h1>
    )

    useEffect(() => {
        if (inputText != 'File Directory') {
            setFiles(window.electron.scanDirectory(inputText))
        }
    }, [inputText]);

    useEffect(() => {
        Promise.resolve(files)
            .then((res) => {
                console.log(res)
                createFileTree(res)
            })
    }, [files]);

    const handleChange = () => {
        setChecked(!checked);
    };

    async function changeInputText() {
        let directoryPath = await window.electron.getDir();
        if (directoryPath == undefined) { // if cancelled
            if (window.electron.isPath(inputText)) return
            else directoryPath = 'invalid Path'
        }
        setInputText(directoryPath);
    }

    function changeExpandState() {
        setExpanded(['mars'])
    }

    function createFileTree(fileArray: string[]) {
        return setFileTree(
            <div className="text-white">
                <div>
                    <label><input type="checkbox"
                                  checked={checked}
                                  onChange={handleChange}
                    />
                        Test
                    </label><br/>
                    {fileArray.map((file: string) => <li>{file}</li>)}
                </div>
            </div>
        )
    }

    return (
        <div className="w-screen">
            <div
                className="flex mx-16 mt-5 items-center justify-left text-black dark:text-white text-md font-medium">
                File Directory to Sort
            </div>
            <div className="flex items-center justify-center mx-16">
                <label htmlFor="browse-files" className="sr-only">File Directory</label>
                <div className="relative w-screen">
                    <div
                        className="absolute inset-y-0 left-0 pt-0.5 flex items-center pl-3 pointer-events-none text-white">
                        <AiFillFolderOpen size="20"/>
                    </div>
                    <button
                        className="bg-gray-50 h-10 text-left shadow-lg border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        onClick={changeInputText}>
                        {inputText}
                    </button>
                </div>
                <button className="button group py-2 px-4 m-2" onClick={changeInputText}>
                    <span className="px-1">Browse</span>
                </button>
            </div>
            {/*<p className="mx-16 text-sm text-gray-500 dark:text-gray-400">Select using the "Browse" button</p>*/}
            <div>{fileTree}</div>
        </div>
    )
}

export default FileBrowser;
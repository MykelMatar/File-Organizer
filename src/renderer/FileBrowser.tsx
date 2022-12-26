import {AiFillFolderOpen} from "react-icons/ai";
import {useState} from "react";

const FileBrowser = () => {
    const initialText: string = 'File Directory'
    const [inputText, setInputText] = useState(initialText)

    async function changeInputText() {
        setInputText('test');
    }

    return (
        <div className="fixed top-0 left-0 w-screen">
            <div
                className="flex mx-20 mt-5 items-center justify-left text-black dark:text-white text-md font-medium">
                File Directory to Sort
            </div>
            <form className="flex items-center justify-center mx-20">
                <label htmlFor="browse-files" className="sr-only">File Directory</label>
                <div className="relative w-screen">
                    <div
                        className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-white">
                        <AiFillFolderOpen size="20"/>
                    </div>
                    <input type="text" id="browse-files"
                           className="bg-gray-50 shadow-lg cursor-not-allowed border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                           placeholder={inputText} disabled readOnly/>
                </div>
                <button className="button group py-2 px-4 m-2" onClick={changeInputText}>
                    <span className="px-1">Browse</span>
                </button>
            </form>
            <p className="mx-20 text-sm text-gray-500 dark:text-gray-400">Select using the "Browse" button</p>
        </div>
    )
}

const BrowseButton = ({text, icon}: any) => (
    <button className="button group py-2 px-4 m-2" onClick={BrowseDirectory}>
        {icon}
        <span className="px-1">{text}</span>
    </button>
)

const BrowseDirectory = async () => {
    let path = await window.electron.getDir();
    if (path == undefined) return 'invalid Path'
    else return path
}

export default FileBrowser;
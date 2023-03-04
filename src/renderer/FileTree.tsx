import {useState} from "react";

const FileTree = (props: any) => {
    let directoryPath: string = props.data
    if (directoryPath == 'File Directory' || directoryPath == undefined) return (
        <h1 className="text-white">
            File Tree
        </h1>
    )

    // let fileArray: string[] = window.electron.scanDirectory(directoryPath)
    const [fileArray, setFileArray] = useState(window.electron.scanDirectory(directoryPath))
    return (
        <div className="text-white">
            <div>
                {fileArray.map((file: string) => <li>{file}</li>)}
            </div>
        </div>
    )
}

export default FileTree;
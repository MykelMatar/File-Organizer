import {BsFillLightningFill, BsPlus} from 'react-icons/bs';
import {FaFire, FaPoo} from 'react-icons/fa';
import {AiFillFolderOpen} from "react-icons/ai";

const FileBrowser = () => {
    return (
        <div className="static top-0 left-0 w-screen h-52 flex flex-row bg-primary text-secondary shadow-lg">
            <span className="text-sm font-medium text-gray-900 dark:text-white">
                Directory to Sort
            </span>
            <div className="flex justify-between items-center gap-3">
                <input type="text" id="directory"
                       className="w-96 md:max-lg:flex bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                       placeholder="" required/>
                <BrowseButton icon={<AiFillFolderOpen size="20"/>} text="Browse"/>
            </div>
            {/*<SideBarIcon icon={<FaFire size="28"/>}/>*/}
            {/*<SideBarIcon icon={<BsPlus size="32"/>}/>*/}
            {/*<SideBarIcon icon={<BsFillLightningFill size="20"/>}/>*/}
            {/*<SideBarIcon icon={<FaPoo size="20"/>}/>*/}
        </div>
    )
}

const BrowseButton = ({text, icon}: any) => (
    <button className="button group py-2 px-2 m-2">
        {icon}
        <span className="px-1">{text}</span>
    </button>
)

const SideBarIcon = ({icon, text = 'tooltip 💡'}: any) => (
    <div className="sidebar-icon group">
        {icon}

        <span className="sidebar-tooltip group-hover:scale-100">{text}</span>
    </div>
);

export default FileBrowser;
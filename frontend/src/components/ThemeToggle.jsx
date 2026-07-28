import {useState} from "react";


function ThemeToggle(){

    const [dark,setDark]=useState(false);

    function toggle(){
        setDark(!dark);
        document.body.style.background = !dark ? "#111827" : "white";
        document.body.style.color = !dark ? "white" : "black";
    }

    return (
        <button onClick={toggle}>
            {
                dark ? "Light" : "Dark"
            }
        </button>
    );
}

export default ThemeToggle;
import {useState} from "react";


function UploadDocument({
    onUpload
}) {

    const [file,setFile]=useState(null);
    const [loading,setLoading]=useState(false);

    async function upload(){

        if(!file)
            return;


        setLoading(true);

        try{
            await onUpload(file);
            setFile(null);

        } finally{
            setLoading(false);
        }

    }

    return (
        <div>
            <h2>
                Upload Document
            </h2>

            <input
                type="file"
                onChange={
                    e=>setFile(e.target.files[0])
                }
            />

            <button 
                onClick={upload}
                disabled={loading}
            >
                {
                    loading
                    ? "Uploading..."
                    : "Upload"
                }
            </button>
        </div>
    )
}


export default UploadDocument;
import { useState } from "react";
import UploadScreen from "./components/UploadScreen";
import ResultScreen from "./components/ResultScreen";

function App() {

    const [uploaded, setUploaded] = useState(false);

    return (
        <>
            {
                uploaded
                ? <ResultScreen />
                : <UploadScreen
                    onUpload={() => setUploaded(true)}
                  />
            }
        </>
    );
}

export default App;
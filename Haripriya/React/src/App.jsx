import { useState } from "react";
import UploadScreen from "./components/UploadScreen";
import ResultScreen from "./components/ResultScreen";
import GithubUser from "./components/GithubUser";
import PostDemo from "./components/PostDemo";
import Spinner from "./components/Spinner";

function App() {

  const [uploaded, setUploaded] = useState(false);
  const [loading, setLoading] = useState(false);

  return (
    <>
      <UploadScreen/>
      {
        loading && <Spinner/>
      }
      {/* <div
        className="
            min-h-screen
            bg-purple-100
            flex
            flex-col
            items-center
            justify-center
            gap-8
            "
      >

        <GithubUser />

        <PostDemo />

      </div> */}
      {/* {
                uploaded
                ? <ResultScreen />
                : <UploadScreen
                    onUpload={() => setUploaded(true)}
                  />
            } */}
    </>
  );
}

export default App;
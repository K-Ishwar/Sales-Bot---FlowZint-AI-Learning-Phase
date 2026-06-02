import { useState } from "react";
import axios from "axios";

function PostDemo() {

    const [msg, setMsg] = useState("");

    async function sendData() {

        try {

            const response =
            await axios.post(
                "https://jsonplaceholder.typicode.com/posts",
                {
                    name: "Haripriya"
                }
            );
            console.log(response.data);
            setMsg(
                `POST Success! ID: ${response.data.id}`
            );

        }
        catch {

            setMsg("POST Failed");

        }

    }

    return (

        <div className="bg-white p-8 rounded-2xl shadow-lg w-[500px]">

            <h1 className="text-3xl font-bold mb-6">
                POST Demo
            </h1>

            <button
                onClick={sendData}
                className="
                w-full
                bg-green-600
                text-white
                p-3
                rounded-lg
                "
            >
                Test POST
            </button>

            <p className="mt-4">
                {msg}
            </p>

        </div>

    );
}

export default PostDemo;
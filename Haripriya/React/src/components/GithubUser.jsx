import { useState } from "react";
import axios from "axios";

function GithubUser() {

    const [username, setUsername] = useState("");
    const [user, setUser] = useState(null);
    const [error, setError] = useState("");

    async function getUser() {

        try {

            setError("");

            const response = await axios.get(
                `https://api.github.com/users/${username}`
            );

            setUser(response.data);

        }
        catch {

            setError("User not found");
            setUser(null);

        }
    }

    return (

        <div className="bg-white p-8 rounded-2xl shadow-lg w-[500px]">

            <h1 className="text-3xl font-bold text-center mb-6">
                GitHub User Search
            </h1>

            <input
                type="text"
                placeholder="Enter username"
                value={username}
                onChange={(e) =>
                    setUsername(e.target.value)
                }
                className="
                w-full
                border
                p-3
                rounded-lg
                mb-4
                "
            />

            <button
                onClick={getUser}
                className="
                w-full
                bg-purple-700
                text-white
                p-3
                rounded-lg
                "
            >
                Get User
            </button>

            {error && (
                <p className="text-red-500 mt-4">
                    {error}
                </p>
            )}

            {user && (

                <div className="mt-6">

                    <img
                        src={user.avatar_url}
                        alt=""
                        className="
                        w-24
                        h-24
                        rounded-full
                        mx-auto
                        "
                    />

                    <h2 className="text-xl font-bold text-center mt-3">
                        {user.login}
                    </h2>

                    <p>
                        Followers: {user.followers}
                    </p>

                    <p>
                        Following: {user.following}
                    </p>

                    <p>
                        Public Repos: {user.public_repos}
                    </p>

                </div>

            )}

        </div>

    );
}

export default GithubUser;
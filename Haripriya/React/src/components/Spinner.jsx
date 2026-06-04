function Spinner({ message = "Loading..." }) {

    return (

        <div
            className="
            flex
            flex-col
            items-center
            justify-center
            gap-6
            "
        >

            <div className="relative">

                <div
                    className="
                    w-20
                    h-20
                    border-4
                    border-purple-200
                    rounded-full
                    "
                ></div>

                <div
                    className="
                    absolute
                    top-0
                    left-0
                    w-20
                    h-20
                    border-4
                    border-transparent
                    border-t-purple-700
                    rounded-full
                    animate-spin
                    "
                ></div>

            </div>

            <p
                className="
                text-lg
                font-medium
                text-purple-700
                animate-pulse
                "
            >
                {message}
            </p>

        </div>

    );
}

export default Spinner;
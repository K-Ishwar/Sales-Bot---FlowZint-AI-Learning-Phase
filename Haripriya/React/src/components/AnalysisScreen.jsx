function AnalysisScreen({
    analysis,
    onDraftEmail,
    onDownload
}) {

    return (

        <div
            className="
            min-h-screen
            bg-purple-100
            flex
            justify-center
            items-center
            "
        >

            <div
                className="
                bg-white
                w-[800px]
                p-8
                rounded-3xl
                shadow-xl
                "
            >

                <h1
                    className="
                    text-4xl
                    font-bold
                    text-purple-700
                    mb-8
                    "
                >
                    Analysis Result
                </h1>

                <div className="space-y-4">

                    <p>
                        <strong>Client Name:</strong>
                        {" "}
                        {analysis.clientName}
                    </p>

                    <p>
                        <strong>Industry:</strong>
                        {" "}
                        {analysis.industry}
                    </p>

                    <p>
                        <strong>Budget:</strong>
                        {" "}
                        {analysis.budget}
                    </p>

                    <p>
                        <strong>Deadline:</strong>
                        {" "}
                        {analysis.deadline}
                    </p>

                </div>

                <div
                    className="
                    flex
                    justify-end
                    gap-4
                    mt-8
                    "
                >

                    <button
                        onClick={onDownload}
                        className="
                        bg-green-600
                        text-white
                        px-6
                        py-3
                        rounded-xl
                        "
                    >
                        Download PDF
                    </button>

                    <button
                        onClick={onDraftEmail}
                        className="
                        bg-purple-700
                        text-white
                        px-6
                        py-3
                        rounded-xl
                        "
                    >
                        Draft Email
                    </button>

                </div>

            </div>

        </div>

    );
}

export default AnalysisScreen;

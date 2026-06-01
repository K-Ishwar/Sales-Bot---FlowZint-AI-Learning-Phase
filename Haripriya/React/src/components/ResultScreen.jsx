function ResultScreen() {

  return (

    <div className="min-h-screen bg-purple-100 flex justify-center items-center">

      <div
        className="
        bg-white
        w-[700px]
        p-10
        rounded-2xl
        shadow-lg
        "
      >

        <h1
          className="
          text-4xl
          font-bold
          text-purple-700
          text-center
          mb-8
          "
        >
          Analysis Result
        </h1>

        <div className="space-y-5">

          <div
            className="
            bg-purple-50
            p-4
            rounded-lg
            "
          >
            <p className="text-lg">
              <span className="font-bold">
                Client:
              </span>
              {" "}
              ABC Ltd
            </p>
          </div>

          <div
            className="
            bg-purple-50
            p-4
            rounded-lg
            "
          >
            <p className="text-lg">
              <span className="font-bold">
                Score:
              </span>
              {" "}
              92
            </p>
          </div>

          <div
            className="
            bg-purple-50
            p-4
            rounded-lg
            "
          >
            <p className="text-lg">
              <span className="font-bold">
                Status:
              </span>
              {" "}
              Approved
            </p>
          </div>

        </div>  

      </div>

    </div>

  )
}

export default ResultScreen
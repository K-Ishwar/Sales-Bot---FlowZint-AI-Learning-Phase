function UploadScreen({ onUpload }) {

  return (
    <div className="min-h-screen bg-purple-100 flex flex-col items-center pt-8">

      <h1 className="text-5xl font-bold mb-4">
        Upload Your File
      </h1>

      <p className="text-gray-600 text-xl mb-10">
        Drag and drop a file or click on the button below
      </p>

      <div
        className="
        w-[700px]
        h-[400px]
        bg-gray-100
        border-2
        border-dashed
        border-purple-600
        rounded-2xl
        flex
        flex-col
        justify-center
        items-center
        "
      >

        <h2 className="text-4xl font-semibold mb-6">
          Drag and drop your file here
        </h2>

        <p className="text-gray-500 text-2xl mb-6">
          Formats: Png, JPG, PDF, DOCX
        </p>

        <p className="font-bold text-xl mb-6">
          OR
        </p>

        <button
          className="
          bg-purple-700
          text-white
          px-16
          py-4
          rounded-md
          text-2xl
          hover:bg-purple-800
          transition
          "
          onClick={onUpload}
        >
          Choose file
        </button>

      </div>

      

    </div>
  )
}

export default UploadScreen
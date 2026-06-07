import { useState, useRef } from "react";
import { analyzeImage } from "../api/stylist";

export default function ImageUploader({ onResult, loading, setLoading }) {
  const [preview, setPreview] = useState(null);
  const [error, setError] = useState(null);
  const [dragOver, setDragOver] = useState(false);
  const inputRef = useRef();

  const handleFile = async (file) => {
    if (!file || !file.type.startsWith("image/")) {
      setError("Please upload a valid image file.");
      return;
    }
    setPreview(URL.createObjectURL(file));
    setError(null);
    setLoading(true);
    try {
      const result = await analyzeImage(file);
      onResult(result);
    } catch (e) {
      setError("Analysis failed. Please try a clearer front-facing photo.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto">
      <div
        className={`border-2 border-dashed rounded-2xl p-8 text-center cursor-pointer transition-all ${
          dragOver ? "border-purple-500 bg-purple-50" : "border-gray-300 hover:border-purple-400"
        }`}
        onClick={() => inputRef.current.click()}
        onDragOver={(e) => { e.preventDefault(); setDragOver(true); }}
        onDragLeave={() => setDragOver(false)}
        onDrop={(e) => { e.preventDefault(); setDragOver(false); handleFile(e.dataTransfer.files[0]); }}
      >
        {preview ? (
          <img src={preview} className="w-40 h-40 object-cover rounded-full mx-auto mb-4 shadow-lg" alt="preview" />
        ) : (
          <div className="mb-4">
            <div className="text-6xl mb-3">📸</div>
            <p className="text-gray-500 text-sm">Drag and drop or click to upload</p>
            <p className="text-gray-400 text-xs mt-1">JPG, PNG supported</p>
          </div>
        )}
        <input
          ref={inputRef}
          type="file"
          accept="image/*"
          className="hidden"
          onChange={(e) => handleFile(e.target.files[0])}
        />
        <button
          className="mt-2 bg-purple-600 hover:bg-purple-700 text-white px-6 py-2 rounded-full text-sm font-medium transition-all"
          onClick={(e) => { e.stopPropagation(); inputRef.current.click(); }}
        >
          {loading ? "Analyzing..." : preview ? "Try Another Photo" : "Upload Photo"}
        </button>
      </div>
      {error && <p className="text-red-500 text-sm text-center mt-3">{error}</p>}
    </div>
  );
}
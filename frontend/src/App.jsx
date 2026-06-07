import { useState } from "react";
import Sidebar from "./components/Sidebar";
import HeroCard from "./components/HeroCard";
import MetricCards from "./components/MetricCards";
import StyleScore from "./components/StyleScore";
import ColorPalette from "./components/ColorPalette";
import ResultsDashboard from "./components/ResultsDashboard";
import ImageUploader from "./components/ImageUploader";

function DashboardPage({ result }) {
  return (
    <div className="space-y-4">
      <HeroCard skin={result.skin} shape={result.shape} />
      <MetricCards skin={result.skin} shape={result.shape} />
      <div className="grid grid-cols-2 gap-4">
        <ColorPalette colors={result.skin.best_colors} title="Colors that suit you" />
        <StyleScore />
      </div>
    </div>
  );
}

function HairPage({ shape }) {
  return (
    <div className="bg-white border border-gray-100 rounded-2xl p-6">
      <h2 className="text-xl font-semibold text-gray-800 mb-1">Face Shape: {shape.shape}</h2>
      <p className="text-gray-400 text-sm mb-6">{shape.description}</p>
      <h3 className="text-sm font-semibold text-gray-600 uppercase tracking-wide mb-3">Recommended Hairstyles</h3>
      <div className="space-y-3 mb-6">
        {shape.hairstyle_recommendations.map((h, i) => (
          <div key={i} className="flex items-start gap-3 bg-purple-50 rounded-xl p-4">
            <span className="text-purple-600 font-bold text-lg">{i + 1}</span>
            <span className="text-gray-700 text-sm pt-0.5">{h}</span>
          </div>
        ))}
      </div>
      <h3 className="text-sm font-semibold text-gray-600 uppercase tracking-wide mb-3">Best Necklines</h3>
      <div className="flex flex-wrap gap-2">
        {shape.neckline_recommendations.map((n, i) => (
          <span key={i} className="bg-purple-100 text-purple-700 px-4 py-1.5 rounded-full text-sm">{n}</span>
        ))}
      </div>
    </div>
  );
}

function MakeupPage({ makeup }) {
  return (
    <div className="space-y-4">
      <div className="bg-amber-50 border border-amber-100 rounded-2xl p-5">
        <p className="text-xs font-semibold text-amber-700 uppercase tracking-wide mb-3">Foundation Shades</p>
        <div className="flex flex-wrap gap-2">
          {makeup.foundation_shades.map((f, i) => (
            <span key={i} className="bg-white border border-amber-200 text-amber-800 px-3 py-1.5 rounded-full text-sm">{f}</span>
          ))}
        </div>
      </div>
      <div className="grid grid-cols-2 gap-4">
        <div className="bg-pink-50 border border-pink-100 rounded-2xl p-5">
          <p className="text-xs font-semibold text-pink-700 uppercase tracking-wide mb-3">Blush</p>
          <div className="flex flex-wrap gap-2">
            {makeup.blush.map((b, i) => (
              <span key={i} className="bg-white border border-pink-200 text-pink-700 px-3 py-1.5 rounded-full text-sm">{b}</span>
            ))}
          </div>
          <p className="text-xs text-pink-500 mt-3">{makeup.blush_technique}</p>
        </div>
        <div className="bg-red-50 border border-red-100 rounded-2xl p-5">
          <p className="text-xs font-semibold text-red-700 uppercase tracking-wide mb-3">Lip Colors</p>
          <p className="text-xs text-gray-400 mb-2">Everyday</p>
          <div className="flex flex-wrap gap-2 mb-3">
            {makeup.lip_everyday.map((l, i) => (
              <span key={i} className="bg-white border border-red-200 text-red-700 px-3 py-1 rounded-full text-sm">{l}</span>
            ))}
          </div>
          <p className="text-xs text-gray-400 mb-2">Bold</p>
          <div className="flex flex-wrap gap-2">
            {makeup.lip_bold.map((l, i) => (
              <span key={i} className="bg-white border border-red-300 text-red-800 px-3 py-1 rounded-full text-sm font-medium">{l}</span>
            ))}
          </div>
        </div>
      </div>
      <div className="bg-purple-50 border border-purple-100 rounded-2xl p-5">
        <p className="text-xs font-semibold text-purple-700 uppercase tracking-wide mb-3">Eye Makeup</p>
        <div className="flex flex-wrap gap-2">
          {makeup.eye_makeup.map((e, i) => (
            <span key={i} className="bg-white border border-purple-200 text-purple-700 px-3 py-1.5 rounded-full text-sm">{e}</span>
          ))}
        </div>
      </div>
      <div className="bg-gray-50 border border-gray-100 rounded-2xl p-4">
        <p className="text-sm text-gray-600">💡 {makeup.pro_tip}</p>
      </div>
    </div>
  );
}

function ColorsPage({ skin }) {
  return (
    <div className="space-y-4">
      <div className="bg-white border border-gray-100 rounded-2xl p-6">
        <h3 className="text-sm font-semibold text-gray-600 uppercase tracking-wide mb-4">Colors that suit you</h3>
        <div className="flex flex-wrap gap-4">
          {skin.best_colors.map((color) => (
            <div key={color} className="flex flex-col items-center gap-2">
              <div className="w-14 h-14 rounded-2xl shadow-sm border border-gray-100"
                style={{ backgroundColor: getColor(color) }} />
              <span className="text-xs text-gray-500 text-center w-16 leading-tight">{color}</span>
            </div>
          ))}
        </div>
      </div>
      <div className="bg-white border border-gray-100 rounded-2xl p-6">
        <h3 className="text-sm font-semibold text-gray-600 uppercase tracking-wide mb-4">Colors to avoid</h3>
        <div className="flex flex-wrap gap-4">
          {skin.avoid_colors.map((color) => (
            <div key={color} className="flex flex-col items-center gap-2">
              <div className="w-14 h-14 rounded-2xl shadow-sm border border-gray-100 relative"
                style={{ backgroundColor: getColor(color) }}>
                <span className="absolute inset-0 flex items-center justify-center text-red-500 text-2xl">✕</span>
              </div>
              <span className="text-xs text-gray-500 text-center w-16 leading-tight">{color}</span>
            </div>
          ))}
        </div>
      </div>
      <div className="bg-purple-50 border border-purple-100 rounded-2xl p-4">
        <p className="text-sm text-purple-700">{skin.outfit_tip}</p>
      </div>
    </div>
  );
}

function SummaryPage({ result }) {
  const rows = [
    ["Skin Tone", result.skin.tone_label],
    ["Undertone", result.skin.undertone],
    ["ITA Angle", `${result.skin.ITA_angle}°`],
    ["Face Shape", result.shape.shape],
    ["Forehead Ratio", result.shape.measurements.forehead_ratio],
    ["Jaw Ratio", result.shape.measurements.jaw_ratio],
    ["Foundation", result.makeup.foundation_shades[0]],
    ["Best Color", result.skin.best_colors[0]],
    ["Top Hairstyle", result.shape.hairstyle_recommendations[0]],
  ];
  return (
    <div className="bg-white border border-gray-100 rounded-2xl p-6">
      <h2 className="text-lg font-semibold text-gray-800 mb-4">Complete Summary</h2>
      <div className="divide-y divide-gray-50">
        {rows.map(([label, value]) => (
          <div key={label} className="flex justify-between items-center py-3">
            <span className="text-gray-400 text-sm">{label}</span>
            <span className="font-medium text-gray-800 text-sm">{value}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function getColor(name) {
  const map = {
    "Coral":"#FF6B6B","Mustard":"#E3A020","Olive":"#6B7B3A","Peach":"#FFBA93",
    "Terracotta":"#C0694E","Warm Red":"#C0392B","Camel":"#C19A6B","Gold":"#FFD700",
    "Lavender":"#B57BED","Silver":"#A8A9AD","Navy":"#003366","Emerald":"#2ECC71",
    "Rose":"#E8A0BF","Icy Pink":"#F4C2C2","Stark White":"#F5F5F5","Cool Grey":"#9E9E9E",
    "Black":"#222222","Icy Blue":"#B3D9FF","Orange":"#FF9800","Mustard2":"#FFC107",
  };
  return map[name] || "#e5e7eb";
}

export default function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [active, setActive] = useState("dashboard");

  if (!result) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 flex items-center justify-center">
        <div className="w-full max-w-lg px-4">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-purple-700 mb-2">✦ AI Stylist</h1>
            <p className="text-gray-500">Upload your photo for a personalised style analysis</p>
          </div>
          <ImageUploader onResult={setResult} loading={loading} setLoading={setLoading} />
          {loading && (
            <div className="text-center mt-8">
              <div className="inline-block w-10 h-10 border-4 border-purple-600 border-t-transparent rounded-full animate-spin mb-3"></div>
              <p className="text-purple-600 font-medium">Analysing your photo...</p>
              <p className="text-gray-400 text-sm mt-1">Detecting skin tone, face shape and more</p>
            </div>
          )}
        </div>
      </div>
    );
  }

  const renderPage = () => {
    switch (active) {
      case "hair":     return <HairPage shape={result.shape} />;
      case "makeup":   return <MakeupPage makeup={result.makeup} />;
      case "colors":   return <ColorsPage skin={result.skin} />;
      case "fashion":  return <SummaryPage result={result} />;
      case "saved":    return <SummaryPage result={result} />;
      default:         return <DashboardPage result={result} />;
    }
  };

  return (
    <div className="flex h-screen bg-gray-50 overflow-hidden">
      <Sidebar active={active} setActive={setActive} />
      <div className="flex-1 overflow-y-auto p-6">
        <div className="max-w-3xl mx-auto space-y-4">
          {renderPage()}
          <div className="text-center pt-4 pb-8">
            <button
              onClick={() => { setResult(null); setActive("dashboard"); }}
              className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-2 rounded-full text-sm font-medium transition-all"
            >
              Analyse another photo
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
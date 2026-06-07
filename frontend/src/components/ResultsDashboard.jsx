import { useState } from "react";
import ColorPalette from "./ColorPalette";

const TABS = ["🎨 Colors", "💇 Hair", "💄 Makeup", "📊 Summary"];

export default function ResultsDashboard({ result }) {
  const [activeTab, setActiveTab] = useState(0);
  const { skin, shape, makeup } = result;

  return (
    <div className="max-w-2xl mx-auto mt-8">
      <div className="bg-gradient-to-r from-purple-600 to-pink-500 rounded-2xl p-6 text-white mb-6 shadow-lg">
        <h2 className="text-2xl font-bold mb-1">Your Style Analysis</h2>
        <p className="opacity-80 text-sm">
          {skin.tone_label} skin · {skin.undertone} undertone · {shape.shape} face shape
        </p>
      </div>
      <div className="flex gap-2 mb-6 overflow-x-auto">
        {TABS.map((tab, i) => (
          <button
            key={i}
            onClick={() => setActiveTab(i)}
            className={`px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-all ${
              activeTab === i
                ? "bg-purple-600 text-white shadow"
                : "bg-gray-100 text-gray-600 hover:bg-gray-200"
            }`}
          >
            {tab}
          </button>
        ))}
      </div>
      <div className="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
        {activeTab === 0 && (
          <div>
            <h3 className="text-lg font-bold mb-4">Your Color Palette</h3>
            <ColorPalette colors={skin.best_colors} title="✅ Colors that suit you" />
            <ColorPalette colors={skin.avoid_colors} title="❌ Colors to avoid" />
            <div className="mt-4 bg-purple-50 rounded-xl p-4">
              <p className="text-sm text-purple-700">{skin.outfit_tip}</p>
            </div>
          </div>
        )}
        {activeTab === 1 && (
          <div>
            <h3 className="text-lg font-bold mb-2">Face Shape: {shape.shape}</h3>
            <p className="text-gray-500 text-sm mb-4">{shape.description}</p>
            <h4 className="font-semibold text-gray-700 mb-3">Recommended Hairstyles</h4>
            <div className="space-y-2 mb-5">
              {shape.hairstyle_recommendations.map((h, i) => (
                <div key={i} className="flex items-start gap-2 bg-gray-50 rounded-xl p-3">
                  <span className="text-purple-500 font-bold">{i + 1}.</span>
                  <span className="text-sm text-gray-700">{h}</span>
                </div>
              ))}
            </div>
            <h4 className="font-semibold text-gray-700 mb-3">Best Necklines</h4>
            <div className="flex flex-wrap gap-2">
              {shape.neckline_recommendations.map((n, i) => (
                <span key={i} className="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm">{n}</span>
              ))}
            </div>
          </div>
        )}
        {activeTab === 2 && (
          <div>
            <h3 className="text-lg font-bold mb-4">Makeup Recommendations</h3>
            <div className="space-y-4">
              <div className="bg-amber-50 rounded-xl p-4">
                <p className="text-xs font-semibold text-amber-700 uppercase mb-2">Foundation Shades</p>
                <div className="flex flex-wrap gap-2">
                  {makeup.foundation_shades.map((f, i) => (
                    <span key={i} className="bg-white border border-amber-200 text-amber-800 px-3 py-1 rounded-full text-sm">{f}</span>
                  ))}
                </div>
              </div>
              <div className="bg-pink-50 rounded-xl p-4">
                <p className="text-xs font-semibold text-pink-700 uppercase mb-2">Blush</p>
                <div className="flex flex-wrap gap-2">
                  {makeup.blush.map((b, i) => (
                    <span key={i} className="bg-white border border-pink-200 text-pink-700 px-3 py-1 rounded-full text-sm">{b}</span>
                  ))}
                </div>
                <p className="text-xs text-pink-600 mt-2">{makeup.blush_technique}</p>
              </div>
              <div className="bg-red-50 rounded-xl p-4">
                <p className="text-xs font-semibold text-red-700 uppercase mb-2">Lip Colors</p>
                <p className="text-xs text-gray-500 mb-1">Everyday:</p>
                <div className="flex flex-wrap gap-2 mb-2">
                  {makeup.lip_everyday.map((l, i) => (
                    <span key={i} className="bg-white border border-red-200 text-red-700 px-3 py-1 rounded-full text-sm">{l}</span>
                  ))}
                </div>
                <p className="text-xs text-gray-500 mb-1">Bold:</p>
                <div className="flex flex-wrap gap-2">
                  {makeup.lip_bold.map((l, i) => (
                    <span key={i} className="bg-white border border-red-300 text-red-800 px-3 py-1 rounded-full text-sm font-medium">{l}</span>
                  ))}
                </div>
              </div>
              <div className="bg-purple-50 rounded-xl p-4">
                <p className="text-xs font-semibold text-purple-700 uppercase mb-2">Eye Makeup</p>
                <div className="flex flex-wrap gap-2">
                  {makeup.eye_makeup.map((e, i) => (
                    <span key={i} className="bg-white border border-purple-200 text-purple-700 px-3 py-1 rounded-full text-sm">{e}</span>
                  ))}
                </div>
              </div>
              <div className="bg-gray-50 rounded-xl p-4">
                <p className="text-sm text-gray-600">💡 {makeup.pro_tip}</p>
              </div>
            </div>
          </div>
        )}
        {activeTab === 3 && (
          <div>
            <h3 className="text-lg font-bold mb-4">Complete Summary</h3>
            <div className="space-y-3">
              {[
                ["Skin Tone", skin.tone_label],
                ["Undertone", skin.undertone],
                ["ITA Angle", `${skin.ITA_angle}°`],
                ["Face Shape", shape.shape],
                ["Forehead Ratio", shape.measurements.forehead_ratio],
                ["Jaw Ratio", shape.measurements.jaw_ratio],
                ["Foundation", makeup.foundation_shades[0]],
                ["Best Color", skin.best_colors[0]],
              ].map(([label, value]) => (
                <div key={label} className="flex justify-between items-center py-2 border-b border-gray-100">
                  <span className="text-gray-500 text-sm">{label}</span>
                  <span className="font-medium">{value}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

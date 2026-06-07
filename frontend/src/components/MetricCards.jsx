export default function MetricCards({ skin, shape }) {
  const cards = [
    { label: "Skin tone", value: skin.tone_label, sub: `${skin.undertone} undertone` },
    { label: "Face shape", value: shape.shape, sub: "95% confidence" },
    { label: "ITA angle", value: `${skin.ITA_angle}°`, sub: "Fitzpatrick scale" },
    { label: "Best colors", value: skin.best_colors.length, sub: "Matched palettes" },
  ];

  return (
    <div className="grid grid-cols-4 gap-3">
      {cards.map((card) => (
        <div key={card.label} className="bg-white border border-gray-100 rounded-xl p-3">
          <p className="text-xs text-gray-400 mb-1">{card.label}</p>
          <p className="text-xl font-semibold text-gray-800">{card.value}</p>
          <p className="text-xs text-purple-500 mt-1">{card.sub}</p>
        </div>
      ))}
    </div>
  );
}
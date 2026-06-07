const bars = [
  { label: "Face shape", pct: 95 },
  { label: "Undertone match", pct: 92 },
  { label: "Hair match", pct: 88 },
  { label: "Makeup match", pct: 90 },
];

export default function StyleScore() {
  return (
    <div className="bg-white border border-gray-100 rounded-2xl p-5">
      <h3 className="text-sm font-semibold text-gray-700 mb-4">Style score breakdown</h3>
      <div className="space-y-3">
        {bars.map((bar) => (
          <div key={bar.label}>
            <div className="flex justify-between text-xs text-gray-500 mb-1">
              <span>{bar.label}</span>
              <span>{bar.pct}%</span>
            </div>
            <div className="h-1.5 bg-gray-100 rounded-full overflow-hidden">
              <div
                className="h-full bg-purple-500 rounded-full transition-all duration-700"
                style={{ width: `${bar.pct}%` }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
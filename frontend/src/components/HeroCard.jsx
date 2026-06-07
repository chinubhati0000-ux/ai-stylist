export default function HeroCard({ skin, shape }) {
  return (
    <div className="bg-white border border-gray-100 rounded-2xl p-5 flex items-center gap-5">
      <div className="w-14 h-14 rounded-full bg-purple-100 flex items-center justify-center text-purple-600 font-semibold text-xl flex-shrink-0">
        A
      </div>
      <div className="flex-1">
        <h2 className="text-lg font-semibold text-gray-800">Hey there 👋</h2>
        <p className="text-gray-400 text-sm">Here is your personalised style analysis</p>
      </div>
      <div className="flex flex-col items-end gap-1">
        <div className="bg-purple-100 text-purple-700 text-sm font-medium px-3 py-1 rounded-full">
          91 / 100 style score
        </div>
        <p className="text-xs text-gray-400">
          {skin.tone_label} · {skin.undertone} · {shape.shape}
        </p>
      </div>
    </div>
  );
}
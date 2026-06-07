const COLOR_MAP = {
  "Coral": "#FF6B6B", "Mustard": "#E3A020", "Olive": "#6B7B3A",
  "Peach": "#FFBA93", "Terracotta": "#C0694E", "Warm Red": "#C0392B",
  "Camel": "#C19A6B", "Gold": "#FFD700", "Lavender": "#B57BED",
  "Silver": "#A8A9AD", "Navy": "#003366", "Emerald": "#2ECC71",
  "Rose": "#E8A0BF", "Icy Pink": "#F4C2C2", "Cobalt": "#0047AB",
  "Mauve": "#E0B0D4", "Ivory": "#FFFFF0", "Teal": "#008080",
  "Burgundy": "#800020", "Forest Green": "#228B22", "Dusty Rose": "#DCAE96",
  "Jade": "#00A86B", "Blush": "#DE5D83",
};

export default function ColorPalette({ colors, title }) {
  return (
    <div className="mb-6">
      <h3 className="text-sm font-semibold text-gray-600 mb-3 uppercase tracking-wide">{title}</h3>
      <div className="flex flex-wrap gap-3">
        {colors.map((color) => (
          <div key={color} className="flex flex-col items-center gap-1">
            <div
              className="w-10 h-10 rounded-full shadow-md border border-gray-200"
              style={{ backgroundColor: COLOR_MAP[color] || "#ccc" }}
              title={color}
            />
            <span className="text-xs text-gray-500 text-center w-14 leading-tight">{color}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

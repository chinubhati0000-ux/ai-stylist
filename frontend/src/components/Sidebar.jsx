import { FiGrid, FiScissors, FiDroplet, FiSun, FiShoppingBag, FiStar, FiHeart, FiUser } from "react-icons/fi";

const NAV = [
  { icon: <FiGrid />, label: "Dashboard", id: "dashboard" },
  { icon: <FiScissors />, label: "Hair Style", id: "hair" },
  { icon: <FiDroplet />, label: "Makeup", id: "makeup" },
  { icon: <FiSun />, label: "Colors", id: "colors" },
  { icon: <FiShoppingBag />, label: "Fashion", id: "fashion" },
  { icon: <FiStar />, label: "Try-On Studio", id: "tryon" },
  { icon: <FiHeart />, label: "Saved Looks", id: "saved" },
];

export default function Sidebar({ active, setActive }) {
  return (
    <div className="w-48 bg-white border-r border-gray-100 flex flex-col py-4 flex-shrink-0 h-full">
      <div className="px-4 pb-4 border-b border-gray-100 mb-2">
        <span className="text-purple-600 font-semibold text-base">✦ AI Stylist</span>
      </div>
      <div className="flex flex-col flex-1">
        {NAV.map((item) => (
          <button
            key={item.id}
            onClick={() => setActive(item.id)}
            className={`flex items-center gap-3 px-4 py-2.5 text-sm transition-all text-left ${
              active === item.id
                ? "bg-purple-50 text-purple-600 font-medium"
                : "text-gray-500 hover:bg-gray-50 hover:text-gray-700"
            }`}
          >
            <span className="text-base">{item.icon}</span>
            {item.label}
          </button>
        ))}
      </div>
      <button className="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-500 hover:bg-gray-50">
        <FiUser className="text-base" />
        Profile
      </button>
    </div>
  );
}
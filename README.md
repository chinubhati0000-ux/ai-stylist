# ✦ AI Personal Stylist & Beauty Analyzer

An AI-powered personal stylist web application that analyzes facial features from a uploaded photo and generates personalized style, color, hair, and makeup recommendations.

## 🌐 Live Demo

**🔗 App:** https://ai-stylist-dusky.vercel.app  
**📖 API:** https://ai-stylist-klip.onrender.com/docs  
**💻 GitHub:** https://github.com/chinubhati0000-ux/ai-stylist

---

## ✨ Features

- 🎨 **Skin Tone Detection** — Detects Fitzpatrick scale (Very Fair to Dark) using OpenCV and K-Means clustering
- 🌡️ **Undertone Analysis** — Classifies Warm, Cool, or Neutral undertones using ITA angle from LAB color space
- 💇 **Face Shape Detection** — Detects Oval, Round, Square, Heart, Diamond, Oblong using MediaPipe Face Mesh (468 landmarks)
- 💄 **Makeup Recommendations** — Suggests foundation shades, blush, lip colors, and eye makeup
- 🎨 **Color Palette** — Personalized best colors and colors to avoid based on undertone
- 📊 **Style Score** — Breakdown of face shape, undertone, hair and makeup match scores
- 💅 **Premium Dashboard** — Sidebar navigation with 5 sections: Dashboard, Hair, Makeup, Colors, Fashion

---

## 🖥️ Screenshots

### Upload Page
Clean upload interface with drag and drop support

### Dashboard
Full analysis with metric cards, color swatches and style score

### Hair Recommendations
Face shape detection with hairstyle recommendations

### Makeup Tab
Foundation shades, blush, lip and eye makeup suggestions

---

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose |
|---|---|
| React.js | UI framework |
| Tailwind CSS | Styling |
| Vite | Build tool |

### Backend
| Technology | Purpose |
|---|---|
| Python | Core language |
| FastAPI | REST API framework |
| OpenCV | Image processing |
| MediaPipe | Face landmark detection |
| Scikit-learn | K-Means clustering |
| Pillow | Image handling |

### Database & Deployment
| Technology | Purpose |
|---|---|
| MongoDB Atlas | Database |
| Render | Backend hosting |
| Vercel | Frontend hosting |
| UptimeRobot | Server monitoring |

---

## 🧠 ML Modules

### Module 1 — Skin Tone Detection

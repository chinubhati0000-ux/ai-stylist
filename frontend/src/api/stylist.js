const BASE = import.meta.env.VITE_API_URL || "http://localhost:8001";

export async function analyzeImage(file) {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${BASE}/analyze`, {
    method: "POST",
    body: form,
  });
  if (!res.ok) {
    const error = await res.text();
    throw new Error(error);
  }
  return res.json();
}
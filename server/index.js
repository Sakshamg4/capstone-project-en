require("dotenv").config({ path: require("path").join(__dirname, "../.env") });
const express = require("express"), cors = require("cors"), { execSync } = require("child_process");
const archiver = require("archiver"), path = require("path"), fs = require("fs");
const app = express(), PORT = process.env.PORT || 5000;
app.use(cors()); app.use(express.json());
function findPython() { const r = path.join(__dirname, ".."); for (const p of [r + "/venv/bin/python3", r + "/venv/Scripts/python.exe", r + "/.venv/bin/python3"]) if (fs.existsSync(p)) return p; return "python3"; }
const PY = findPython(); console.log("🐍 Python:", PY);
if (process.env.NODE_ENV === "production") app.use(express.static(path.join(__dirname, "../client/dist")));
app.get("/api/health", (q, r) => r.json({ status: "ok", ai: !!(process.env.GROQ_API_KEY || process.env.GEMINI_API_KEY) }));
app.post("/api/preview", (req, res) => {
  const { name, email, country } = req.body;
  if (!name || name.trim().length < 2) return res.status(400).json({ error: "Name too short" });
  if (!email || !email.includes("@")) return res.status(400).json({ error: "Invalid email" });
  const c = ["France", "Belgique", "Ghana", "Ireland"].includes(country) ? country : "Ghana";
  const sd = path.join(__dirname, "../scripts"), od = path.join(sd, "output");
  if (fs.existsSync(od)) fs.rmSync(od, { recursive: true });
  try {
    const cmd = `"${PY}" generate.py "${name.trim()}" "${email.trim()}" "${c}" "en"`;
    console.log("\n🌱", cmd);
    console.log(execSync(cmd, { cwd: sd, encoding: "utf-8", timeout: 60000, env: { ...process.env, PYTHONIOENCODING: "utf-8", GROQ_API_KEY: process.env.GROQ_API_KEY || "", GEMINI_API_KEY: process.env.GEMINI_API_KEY || "" } }));
    const files = fs.readdirSync(od).filter(f => f.endsWith(".pptx") || f.endsWith(".docx"));
    if (files.length < 3) return res.status(500).json({ error: `Got ${files.length} files` });
    let content = {}; const cp = path.join(od, "content.json");
    if (fs.existsSync(cp)) content = JSON.parse(fs.readFileSync(cp, "utf-8"));
    res.json({ success: true, files, content });
  } catch (e) { console.error("❌", e.stderr || e.message); res.status(500).json({ error: "Generation failed", details: (e.stderr || e.message).slice(0, 500) }) }
});
app.get("/api/download", (req, res) => {
  const od = path.join(__dirname, "../scripts/output");
  if (!fs.existsSync(od)) return res.status(404).json({ error: "No files" });
  const files = fs.readdirSync(od).filter(f => f.endsWith(".pptx") || f.endsWith(".docx"));
  if (files.length < 3) return res.status(404).json({ error: "Files not ready" });
  const nm = files[0].split("_").slice(1).join("_").replace(/\.(pptx|docx)/, "");
  res.setHeader("Content-Type", "application/zip");
  res.setHeader("Content-Disposition", `attachment; filename=Capstone_${nm}.zip`);
  const ar = archiver("zip", { zlib: { level: 9 } }); ar.on("error", () => res.status(500).end()); ar.pipe(res);
  files.forEach(f => ar.file(path.join(od, f), { name: f })); ar.finalize();
});
if (process.env.NODE_ENV === "production") app.get("*", (q, r) => r.sendFile(path.join(__dirname, "../client/dist/index.html")));
app.listen(PORT, () => console.log(`\n🌱 http://localhost:${PORT}\n`));
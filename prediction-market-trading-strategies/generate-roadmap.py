#!/usr/bin/env python3
"""Generate a self-contained interactive HTML roadmap from roadmap-final.json."""
import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(SCRIPT_DIR, "architecture", "roadmap-final.json")
OUT_PATH = os.path.join(SCRIPT_DIR, "roadmap.html")

with open(JSON_PATH) as f:
    data = json.load(f)

# Minify JSON for embedding (remove unnecessary whitespace)
json_blob = json.dumps(data, separators=(',', ':'))

meta = data["metadata"]
title = meta["title"]

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg-dark:#0f172a;--bg-light:#f8fafc;--bg-card:#ffffff;
  --text-primary:#1e293b;--text-secondary:#64748b;--text-light:#f8fafc;
  --border:#e2e8f0;--shadow:0 1px 3px rgba(0,0,0,.1);
  --green-bg:#E8F5E9;--green-border:#4CAF50;--green-text:#2E7D32;
  --blue-bg:#E3F2FD;--blue-border:#2196F3;--blue-text:#1565C0;
  --orange-bg:#FFF3E0;--orange-border:#FF9800;--orange-text:#E65100;
  --red-bg:#FFEBEE;--red-border:#F44336;--red-text:#C62828;
  --gold-bg:#FFF8E1;--gold-border:#FFC107;--gold-text:#795548;
  --purple-bg:#F3E5F5;--purple-border:#9C27B0;--purple-text:#6A1B9A;
  --panel-width:420px;
}}
html{{scroll-behavior:smooth}}
body{{
  font-family:'Inter',system-ui,-apple-system,sans-serif;
  background:var(--bg-light);color:var(--text-primary);
  line-height:1.5;overflow-x:hidden;
}}
/* HEADER */
.header{{
  background:var(--bg-dark);color:var(--text-light);
  padding:24px 32px;position:sticky;top:0;z-index:100;
  box-shadow:0 2px 8px rgba(0,0,0,.3);
}}
.header-inner{{max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px}}
.header h1{{font-size:1.35rem;font-weight:700;line-height:1.3}}
.header-subtitle{{font-size:.85rem;color:#94a3b8;margin-top:2px}}
.header-stats{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}}
.progress-circle{{position:relative;width:56px;height:56px}}
.progress-circle svg{{transform:rotate(-90deg)}}
.progress-circle circle{{fill:none;stroke-width:5}}
.progress-bg{{stroke:#334155}}
.progress-fg{{stroke:#22c55e;transition:stroke-dashoffset .5s ease}}
.progress-text{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700;color:var(--text-light)}}
.stat-pill{{background:#1e293b;border:1px solid #334155;border-radius:20px;padding:4px 12px;font-size:.75rem;color:#94a3b8}}
.stat-pill strong{{color:#e2e8f0}}

/* TOOLBAR */
.toolbar{{
  background:var(--bg-card);border-bottom:1px solid var(--border);
  padding:12px 32px;position:sticky;top:0;z-index:90;
  box-shadow:var(--shadow);
}}
.toolbar-inner{{max-width:1200px;margin:0 auto;display:flex;gap:12px;align-items:center;flex-wrap:wrap}}
.search-box{{
  flex:1;min-width:200px;padding:8px 12px 8px 36px;border:1px solid var(--border);
  border-radius:8px;font-size:.875rem;background:var(--bg-light);
  outline:none;transition:border-color .2s;
}}
.search-box:focus{{border-color:var(--blue-border)}}
.search-icon{{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--text-secondary);pointer-events:none}}
.search-wrap{{position:relative;flex:1;min-width:200px}}
.filter-pills{{display:flex;gap:6px;flex-wrap:wrap}}
.filter-pill{{
  padding:4px 12px;border-radius:16px;font-size:.75rem;font-weight:500;
  border:1px solid var(--border);background:var(--bg-light);
  cursor:pointer;transition:all .2s;user-select:none;
}}
.filter-pill:hover{{border-color:var(--text-secondary)}}
.filter-pill.active{{color:#fff}}
.filter-pill[data-diff="all"].active{{background:var(--text-primary);border-color:var(--text-primary)}}
.filter-pill[data-diff="beginner"].active{{background:var(--green-border);border-color:var(--green-border)}}
.filter-pill[data-diff="intermediate"].active{{background:var(--blue-border);border-color:var(--blue-border)}}
.filter-pill[data-diff="advanced"].active{{background:var(--orange-border);border-color:var(--orange-border)}}
.filter-pill[data-diff="expert"].active{{background:var(--red-border);border-color:var(--red-border)}}

/* LEGEND */
.legend{{
  max-width:1200px;margin:16px auto;padding:0 32px;
  display:flex;gap:16px;flex-wrap:wrap;align-items:center;font-size:.75rem;color:var(--text-secondary);
}}
.legend-item{{display:flex;align-items:center;gap:4px}}
.legend-swatch{{width:16px;height:16px;border-radius:4px;border:2px solid}}

/* CANVAS */
.canvas{{max-width:1200px;margin:0 auto;padding:24px 32px 80px}}

/* SECTION */
.section{{margin-bottom:32px;border-radius:12px;overflow:hidden;background:var(--bg-card);box-shadow:var(--shadow);border:1px solid var(--border)}}
.section-header{{
  display:flex;align-items:center;justify-content:space-between;
  padding:16px 20px;cursor:pointer;user-select:none;transition:background .2s;
}}
.section-header:hover{{filter:brightness(.97)}}
.section-title-area{{display:flex;align-items:center;gap:12px}}
.section-title{{font-size:1.1rem;font-weight:700}}
.section-meta{{font-size:.75rem;color:var(--text-secondary)}}
.section-chevron{{font-size:1.2rem;transition:transform .3s}}
.section.collapsed .section-chevron{{transform:rotate(-90deg)}}
.section-progress{{display:flex;align-items:center;gap:8px}}
.section-progress-bar{{width:120px;height:6px;background:#e2e8f0;border-radius:3px;overflow:hidden}}
.section-progress-fill{{height:100%;border-radius:3px;transition:width .4s ease}}
.section-progress-text{{font-size:.75rem;color:var(--text-secondary);min-width:48px;text-align:right}}
.section-body{{padding:0 20px 20px;transition:max-height .3s ease}}
.section.collapsed .section-body{{display:none}}

/* CHECKPOINT NODE */
.checkpoint-node{{
  display:flex;align-items:center;gap:10px;
  padding:10px 16px;margin-bottom:16px;
  background:var(--purple-bg);border:2px solid var(--purple-border);
  border-radius:8px;color:var(--purple-text);font-weight:600;font-size:.85rem;
}}
.checkpoint-icon{{font-size:1.2rem}}

/* NODE GRID */
.node-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:12px;
}}
@media(max-width:900px){{.node-grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:600px){{.node-grid{{grid-template-columns:1fr}}}}

/* NODE */
.node{{
  border-radius:10px;padding:12px 14px;cursor:pointer;
  transition:all .2s;position:relative;min-height:56px;
  display:flex;align-items:flex-start;gap:10px;
}}
.node:hover{{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.12)}}
.node.locked{{opacity:.55;cursor:not-allowed}}
.node.locked:hover{{transform:none;box-shadow:none}}
.node.completed{{opacity:.7}}
.node.hidden{{display:none}}
.node-checkbox{{
  width:18px;height:18px;min-width:18px;border-radius:4px;border:2px solid;
  display:flex;align-items:center;justify-content:center;
  cursor:pointer;transition:all .2s;margin-top:1px;font-size:11px;
}}
.node-checkbox.checked{{color:#fff}}
.node-content{{flex:1;min-width:0}}
.node-title{{font-size:.82rem;font-weight:600;line-height:1.3}}
.node-badges{{display:flex;gap:4px;margin-top:4px;flex-wrap:wrap}}
.node-badge{{
  font-size:.65rem;padding:1px 6px;border-radius:8px;font-weight:500;
  white-space:nowrap;
}}
.node-lock-icon{{position:absolute;top:6px;right:8px;font-size:.75rem;opacity:.6}}
.node-milestone-icon{{font-size:.7rem;margin-right:2px}}

/* DETAIL PANEL */
.panel-overlay{{
  position:fixed;inset:0;background:rgba(0,0,0,.3);z-index:200;
  opacity:0;pointer-events:none;transition:opacity .3s;
}}
.panel-overlay.open{{opacity:1;pointer-events:auto}}
.detail-panel{{
  position:fixed;top:0;right:0;bottom:0;width:var(--panel-width);
  max-width:100vw;background:var(--bg-card);z-index:210;
  transform:translateX(100%);transition:transform .3s ease;
  overflow-y:auto;box-shadow:-4px 0 20px rgba(0,0,0,.15);
}}
.detail-panel.open{{transform:translateX(0)}}
.panel-close{{
  position:absolute;top:12px;right:12px;width:32px;height:32px;
  border:none;background:#f1f5f9;border-radius:8px;cursor:pointer;
  font-size:1.1rem;display:flex;align-items:center;justify-content:center;
  transition:background .2s;
}}
.panel-close:hover{{background:#e2e8f0}}
.panel-header{{padding:24px 24px 16px;border-bottom:1px solid var(--border)}}
.panel-title{{font-size:1.2rem;font-weight:700;padding-right:40px}}
.panel-diff-badge{{
  display:inline-block;padding:2px 10px;border-radius:12px;
  font-size:.75rem;font-weight:600;margin-top:8px;
}}
.panel-hours{{font-size:.8rem;color:var(--text-secondary);margin-top:4px}}
.panel-section{{padding:16px 24px;border-bottom:1px solid var(--border)}}
.panel-section-title{{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--text-secondary);margin-bottom:8px}}
.panel-description{{font-size:.875rem;color:var(--text-primary);line-height:1.6}}
.concept-pills{{display:flex;gap:6px;flex-wrap:wrap}}
.concept-pill{{background:#f1f5f9;border:1px solid var(--border);padding:2px 10px;border-radius:12px;font-size:.75rem;color:var(--text-primary)}}
.prereq-list{{list-style:none}}
.prereq-list li{{padding:4px 0}}
.prereq-link{{
  color:var(--blue-text);text-decoration:none;font-size:.85rem;
  cursor:pointer;display:flex;align-items:center;gap:4px;
}}
.prereq-link:hover{{text-decoration:underline}}
.prereq-check{{font-size:.75rem}}

/* RESOURCE LIST */
.resource-item{{
  padding:10px 12px;border:1px solid var(--border);border-radius:8px;
  margin-bottom:8px;transition:background .2s;
}}
.resource-item:hover{{background:#f8fafc}}
.resource-title{{font-size:.85rem;font-weight:500}}
.resource-title a{{color:var(--blue-text);text-decoration:none}}
.resource-title a:hover{{text-decoration:underline}}
.resource-badges{{display:flex;gap:4px;margin-top:4px;flex-wrap:wrap}}
.resource-badge{{
  font-size:.65rem;padding:1px 8px;border-radius:10px;font-weight:500;
}}
.rbadge-type{{background:#e0e7ff;color:#3730a3}}
.rbadge-free{{background:#dcfce7;color:#166534}}
.rbadge-paid{{background:#fed7aa;color:#9a3412}}
.rbadge-time{{background:#f1f5f9;color:var(--text-secondary)}}
.rbadge-recommended{{background:#fef9c3;color:#854d0e}}
.show-more-btn{{
  background:none;border:1px solid var(--border);border-radius:8px;
  padding:6px 16px;font-size:.8rem;color:var(--text-secondary);
  cursor:pointer;width:100%;margin-top:4px;
}}
.show-more-btn:hover{{background:#f1f5f9}}

/* FOOTER */
.footer{{
  text-align:center;padding:32px;color:var(--text-secondary);
  font-size:.75rem;border-top:1px solid var(--border);margin-top:32px;
}}
</style>
</head>
<body>

<div class="header">
 <div class="header-inner">
  <div>
   <h1>{title}</h1>
   <div class="header-subtitle">{meta['description'][:120]}...</div>
  </div>
  <div class="header-stats">
   <div class="progress-circle" id="overallProgress">
    <svg width="56" height="56"><circle class="progress-bg" cx="28" cy="28" r="22"/><circle class="progress-fg" id="progressArc" cx="28" cy="28" r="22" stroke-dasharray="138.23" stroke-dashoffset="138.23"/></svg>
    <div class="progress-text" id="progressPct">0%</div>
   </div>
   <div class="stat-pill"><strong>{meta['nodeCount']}</strong> topics</div>
   <div class="stat-pill"><strong>{meta['resourceCount']}</strong> resources</div>
   <div class="stat-pill"><strong>{meta['totalEstimatedHours']}</strong> hours</div>
  </div>
 </div>
</div>

<div class="toolbar">
 <div class="toolbar-inner">
  <div class="search-wrap">
   <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
   <input type="text" class="search-box" id="searchBox" placeholder="Search topics, concepts...">
  </div>
  <div class="filter-pills" id="filterPills">
   <span class="filter-pill active" data-diff="all">All</span>
   <span class="filter-pill" data-diff="beginner">Beginner</span>
   <span class="filter-pill" data-diff="intermediate">Intermediate</span>
   <span class="filter-pill" data-diff="advanced">Advanced</span>
   <span class="filter-pill" data-diff="expert">Expert</span>
  </div>
 </div>
</div>

<div class="legend">
 <span style="font-weight:600">Legend:</span>
 <div class="legend-item"><div class="legend-swatch" style="background:var(--green-bg);border-color:var(--green-border)"></div>Beginner</div>
 <div class="legend-item"><div class="legend-swatch" style="background:var(--blue-bg);border-color:var(--blue-border)"></div>Intermediate</div>
 <div class="legend-item"><div class="legend-swatch" style="background:var(--orange-bg);border-color:var(--orange-border)"></div>Advanced</div>
 <div class="legend-item"><div class="legend-swatch" style="background:var(--red-bg);border-color:var(--red-border)"></div>Expert</div>
 <div class="legend-item"><div class="legend-swatch" style="background:var(--gold-bg);border-color:var(--gold-border);border-width:3px"></div>Milestone</div>
 <div class="legend-item"><div class="legend-swatch" style="background:var(--purple-bg);border-color:var(--purple-border)"></div>Checkpoint</div>
 <div class="legend-item"><div class="legend-swatch" style="border-style:dashed;border-color:var(--text-secondary);background:#fafafa"></div>Optional</div>
</div>

<div class="canvas" id="canvas"></div>

<div class="panel-overlay" id="panelOverlay"></div>
<div class="detail-panel" id="detailPanel">
 <button class="panel-close" id="panelClose">&times;</button>
 <div id="panelContent"></div>
</div>

<div class="footer">
 Generated on {meta['generatedAt']} &mdash; {meta['nodeCount']} topics across {len(data['sections'])} sections &mdash; {meta['totalEstimatedHours']} estimated hours
</div>

<script>
const ROADMAP = {json_blob};

const DIFF_COLORS = {{
  beginner: {{bg:'#E8F5E9',border:'#4CAF50',text:'#2E7D32'}},
  intermediate: {{bg:'#E3F2FD',border:'#2196F3',text:'#1565C0'}},
  advanced: {{bg:'#FFF3E0',border:'#FF9800',text:'#E65100'}},
  expert: {{bg:'#FFEBEE',border:'#F44336',text:'#C62828'}}
}};
const MILESTONE_COLORS = {{bg:'#FFF8E1',border:'#FFC107',text:'#795548'}};
const CHECKPOINT_COLORS = {{bg:'#F3E5F5',border:'#9C27B0',text:'#6A1B9A'}};

const STORAGE_KEY = ROADMAP.progressTracking.storageKey;
let completed = {{}};
try {{ completed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{{}}'); }} catch(e) {{}}

function save() {{ localStorage.setItem(STORAGE_KEY, JSON.stringify(completed)); }}

function isComplete(id) {{ return !!completed[id]; }}

function prereqsMet(node) {{
  if (!node.prerequisites || !node.prerequisites.length) return true;
  return node.prerequisites.every(p => isComplete(p));
}}

const nodeMap = {{}};
ROADMAP.nodes.forEach(n => nodeMap[n.id] = n);

const sectionNodes = {{}};
ROADMAP.sections.forEach(s => sectionNodes[s.id] = []);
ROADMAP.nodes.forEach(n => {{
  if (sectionNodes[n.sectionId]) sectionNodes[n.sectionId].push(n);
}});

// Build canvas
function render() {{
  const canvas = document.getElementById('canvas');
  canvas.innerHTML = '';
  ROADMAP.sections.forEach(sec => {{
    const nodes = sectionNodes[sec.id] || [];
    const checkpoint = nodes.find(n => n.isCheckpoint);
    const regularNodes = nodes.filter(n => !n.isCheckpoint);
    const completedCount = regularNodes.filter(n => isComplete(n.id)).length;
    const total = regularNodes.length;
    const pct = total ? Math.round(completedCount / total * 100) : 0;
    const sColor = sec.color || DIFF_COLORS[sec.difficulty] || DIFF_COLORS.beginner;

    const secEl = document.createElement('div');
    secEl.className = 'section';
    secEl.id = 'sec-' + sec.id;
    secEl.innerHTML = `
      <div class="section-header" style="background:${{sColor.bg}};border-left:4px solid ${{sColor.border}}" onclick="toggleSection('${{sec.id}}')">
        <div class="section-title-area">
          <span class="section-chevron">&#9660;</span>
          <div>
            <div class="section-title" style="color:${{sColor.text}}">${{sec.title}}</div>
            <div class="section-meta">${{sec.description}} &mdash; ${{sec.estimatedHours}}h estimated</div>
          </div>
        </div>
        <div class="section-progress">
          <div class="section-progress-bar"><div class="section-progress-fill" id="spf-${{sec.id}}" style="width:${{pct}}%;background:${{sColor.border}}"></div></div>
          <div class="section-progress-text" id="spt-${{sec.id}}">${{completedCount}}/${{total}}</div>
        </div>
      </div>
      <div class="section-body" id="sb-${{sec.id}}">
        ${{checkpoint ? `<div class="checkpoint-node"><span class="checkpoint-icon">&#10003;</span>${{checkpoint.title}}</div>` : ''}}
        <div class="node-grid" id="ng-${{sec.id}}"></div>
      </div>
    `;
    canvas.appendChild(secEl);

    const grid = secEl.querySelector('.node-grid');
    regularNodes.forEach(node => {{
      const c = node.isMilestone ? MILESTONE_COLORS : (DIFF_COLORS[node.difficulty] || DIFF_COLORS.beginner);
      const locked = !prereqsMet(node);
      const done = isComplete(node.id);
      const nodeEl = document.createElement('div');
      nodeEl.className = 'node' + (locked ? ' locked' : '') + (done ? ' completed' : '');
      nodeEl.id = 'node-el-' + node.id;
      nodeEl.setAttribute('data-id', node.id);
      nodeEl.setAttribute('data-diff', node.difficulty);
      nodeEl.setAttribute('data-title', node.title.toLowerCase());
      nodeEl.setAttribute('data-concepts', (node.keyConcepts || []).join(' ').toLowerCase());
      nodeEl.style.background = c.bg;
      nodeEl.style.border = `${{node.style?.borderWidth || 2}}px ${{node.isOptional ? 'dashed' : 'solid'}} ${{c.border}}`;
      if (node.isOptional) nodeEl.style.opacity = '0.8';

      const dc = DIFF_COLORS[node.difficulty] || DIFF_COLORS.beginner;
      nodeEl.innerHTML = `
        <div class="node-checkbox ${{done ? 'checked' : ''}}" style="border-color:${{c.border}};${{done ? 'background:'+c.border : ''}}" data-id="${{node.id}}" onclick="event.stopPropagation();toggleComplete('${{node.id}}')">
          ${{done ? '&#10003;' : ''}}
        </div>
        <div class="node-content">
          <div class="node-title" style="color:${{c.text}}">
            ${{node.isMilestone ? '<span class="node-milestone-icon">&#9733;</span>' : ''}}
            ${{node.title}}
          </div>
          <div class="node-badges">
            <span class="node-badge" style="background:${{dc.bg}};color:${{dc.text}}">${{node.difficulty}}</span>
            ${{node.estimatedHours ? `<span class="node-badge" style="background:#f1f5f9;color:#64748b">${{node.estimatedHours}}h</span>` : ''}}
            ${{node.isOptional ? '<span class="node-badge" style="background:#fafafa;color:#94a3b8;border:1px dashed #cbd5e1">optional</span>' : ''}}
          </div>
        </div>
        ${{locked ? '<span class="node-lock-icon">&#128274;</span>' : ''}}
      `;
      nodeEl.addEventListener('click', () => {{
        if (!locked) openPanel(node.id);
      }});
      grid.appendChild(nodeEl);
    }});
  }});
  updateOverallProgress();
}}

function toggleSection(secId) {{
  const el = document.getElementById('sec-' + secId);
  if (el) el.classList.toggle('collapsed');
}}

function toggleComplete(nodeId) {{
  const node = nodeMap[nodeId];
  if (!node) return;
  if (!prereqsMet(node) && !isComplete(nodeId)) return;
  if (isComplete(nodeId)) {{
    delete completed[nodeId];
  }} else {{
    completed[nodeId] = true;
  }}
  save();
  render();
}}

function updateOverallProgress() {{
  const allNodes = ROADMAP.nodes.filter(n => !n.isCheckpoint);
  const total = allNodes.length;
  const done = allNodes.filter(n => isComplete(n.id)).length;
  const pct = total ? Math.round(done / total * 100) : 0;
  const circumference = 2 * Math.PI * 22;
  const offset = circumference - (pct / 100) * circumference;
  document.getElementById('progressArc').style.strokeDashoffset = offset;
  document.getElementById('progressPct').textContent = pct + '%';
}}

// Detail panel
function openPanel(nodeId) {{
  const node = nodeMap[nodeId];
  if (!node) return;
  const dc = DIFF_COLORS[node.difficulty] || DIFF_COLORS.beginner;
  const resources = node.resources || [];
  const maxShow = 10;
  const showAll = resources.length <= maxShow;

  let prereqHtml = '';
  if (node.prerequisites && node.prerequisites.length) {{
    prereqHtml = `<div class="panel-section">
      <div class="panel-section-title">Prerequisites</div>
      <ul class="prereq-list">
        ${{node.prerequisites.map(pid => {{
          const pn = nodeMap[pid];
          const done = isComplete(pid);
          return `<li><a class="prereq-link" onclick="scrollToNode('${{pid}}')" title="Click to navigate"><span class="prereq-check">${{done ? '&#9989;' : '&#9744;'}}</span>${{pn ? pn.title : pid}}</a></li>`;
        }}).join('')}}
      </ul>
    </div>`;
  }}

  let conceptsHtml = '';
  if (node.keyConcepts && node.keyConcepts.length) {{
    conceptsHtml = `<div class="panel-section">
      <div class="panel-section-title">Key Concepts</div>
      <div class="concept-pills">${{node.keyConcepts.map(c => `<span class="concept-pill">${{c}}</span>`).join('')}}</div>
    </div>`;
  }}

  let subtopicsHtml = '';
  if (node.subTopics && node.subTopics.length) {{
    subtopicsHtml = `<div class="panel-section">
      <div class="panel-section-title">Sub-Topics</div>
      <ul style="padding-left:18px;font-size:.85rem">${{node.subTopics.map(s => `<li>${{s}}</li>`).join('')}}</ul>
    </div>`;
  }}

  const resHtml = resources.length ? `<div class="panel-section">
    <div class="panel-section-title">Resources (${{resources.length}})</div>
    <div id="resourceList">
      ${{resources.slice(0, showAll ? resources.length : maxShow).map(r => resourceCard(r)).join('')}}
    </div>
    ${{!showAll ? `<button class="show-more-btn" onclick="showAllResources('${{nodeId}}')">Show all ${{resources.length}} resources</button>` : ''}}
  </div>` : '';

  document.getElementById('panelContent').innerHTML = `
    <div class="panel-header">
      <div class="panel-title">${{node.isMilestone ? '&#9733; ' : ''}}${{node.title}}</div>
      <span class="panel-diff-badge" style="background:${{dc.bg}};color:${{dc.text}};border:1px solid ${{dc.border}}">${{node.difficulty}}</span>
      <div class="panel-hours">${{node.estimatedHours ? node.estimatedHours + ' hours estimated' : ''}}</div>
    </div>
    <div class="panel-section">
      <div class="panel-section-title">Description</div>
      <div class="panel-description">${{node.description}}</div>
    </div>
    ${{conceptsHtml}}
    ${{subtopicsHtml}}
    ${{prereqHtml}}
    ${{resHtml}}
  `;
  document.getElementById('detailPanel').classList.add('open');
  document.getElementById('panelOverlay').classList.add('open');
}}

function resourceCard(r) {{
  const recBadge = r.isRecommended ? '<span class="resource-badge rbadge-recommended">&#9733; recommended</span>' : '';
  const costBadge = r.cost === 'free' ? '<span class="resource-badge rbadge-free">FREE</span>' : '<span class="resource-badge rbadge-paid">PAID</span>';
  const time = r.estimatedTime || (r.estimatedMinutes ? r.estimatedMinutes + ' min' : '');
  const timeBadge = time ? `<span class="resource-badge rbadge-time">${{time}}</span>` : '';
  return `<div class="resource-item">
    <div class="resource-title"><a href="${{r.url}}" target="_blank" rel="noopener">${{r.title}}</a></div>
    <div class="resource-badges">
      ${{recBadge}}
      <span class="resource-badge rbadge-type">${{r.type || ''}}</span>
      ${{costBadge}}${{timeBadge}}
    </div>
  </div>`;
}}

function showAllResources(nodeId) {{
  const node = nodeMap[nodeId];
  if (!node) return;
  const el = document.getElementById('resourceList');
  if (el) {{
    el.innerHTML = (node.resources || []).map(r => resourceCard(r)).join('');
    const btn = el.parentElement.querySelector('.show-more-btn');
    if (btn) btn.remove();
  }}
}}

function closePanel() {{
  document.getElementById('detailPanel').classList.remove('open');
  document.getElementById('panelOverlay').classList.remove('open');
}}

function scrollToNode(nodeId) {{
  closePanel();
  setTimeout(() => {{
    const el = document.getElementById('node-el-' + nodeId);
    if (el) {{
      // Expand parent section if collapsed
      const sec = el.closest('.section');
      if (sec && sec.classList.contains('collapsed')) sec.classList.remove('collapsed');
      el.scrollIntoView({{ behavior:'smooth', block:'center' }});
      el.style.outline = '3px solid #2196F3';
      el.style.outlineOffset = '2px';
      setTimeout(() => {{ el.style.outline = ''; el.style.outlineOffset = ''; }}, 2000);
    }}
  }}, 350);
}}

document.getElementById('panelOverlay').addEventListener('click', closePanel);
document.getElementById('panelClose').addEventListener('click', closePanel);
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closePanel(); }});

// Search
document.getElementById('searchBox').addEventListener('input', applyFilters);

// Filter pills
let activeFilter = 'all';
document.querySelectorAll('.filter-pill').forEach(pill => {{
  pill.addEventListener('click', () => {{
    document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    activeFilter = pill.getAttribute('data-diff');
    applyFilters();
  }});
}});

function applyFilters() {{
  const q = document.getElementById('searchBox').value.toLowerCase().trim();
  document.querySelectorAll('.node').forEach(el => {{
    const diff = el.getAttribute('data-diff');
    const title = el.getAttribute('data-title');
    const concepts = el.getAttribute('data-concepts');
    const matchDiff = activeFilter === 'all' || diff === activeFilter;
    const matchSearch = !q || title.includes(q) || concepts.includes(q);
    el.classList.toggle('hidden', !(matchDiff && matchSearch));
  }});
}}

// Init
render();
</script>
</body>
</html>'''

with open(OUT_PATH, 'w') as f:
    f.write(html)

size = os.path.getsize(OUT_PATH)
print(f"Written: {OUT_PATH}")
print(f"Size: {size} bytes ({size/1024:.1f} KB)")

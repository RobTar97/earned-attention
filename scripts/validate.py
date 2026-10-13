"""Validate this skill repository's portable structure using the standard library."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = 'psychological-content-strategy'
SKILL = ROOT / 'skills' / SKILL_NAME
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f'{path.relative_to(ROOT)}: {exc}')
        return None


required = ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'CHANGELOG.md',
            'docs/installation.md', 'docs/examples.md', 'docs/workflow.md',
            'docs/evidence.md', 'evals/evals.json', 'evals/summary.json',
            'skills.sh.json', 'skills/psychological-content-strategy/SKILL.md',
            'skills/psychological-content-strategy/LICENSE']
for rel in required:
    check((ROOT / rel).is_file(), f'Missing required file: {rel}')

if (SKILL / 'LICENSE').exists() and (ROOT / 'LICENSE').exists():
    check((SKILL / 'LICENSE').read_text(encoding='utf-8') == (ROOT / 'LICENSE').read_text(encoding='utf-8'),
          'Installable skill must include the same license as the repository')

skill_path = SKILL / 'SKILL.md'
if skill_path.exists():
    content = skill_path.read_text(encoding='utf-8')
    header = re.match(r'^---\n(.*?)\n---\n', content, re.S)
    check(header is not None, 'SKILL.md needs YAML frontmatter at the start')
    if header:
        # This repository deliberately uses one-line name/description fields.
        fields = dict(re.findall(r'^([a-z-]+): (.+)$', header[1], re.M))
        name = fields.get('name', '').strip('"\'')
        description = fields.get('description', '').strip('"\'')
        check(name == SKILL_NAME, 'Skill name must match its stable directory identifier')
        check(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)), 'Skill name must be lowercase kebab-case')
        check(1 <= len(description) <= 1024, 'Description must have 1–1024 characters')
        check(fields.get('license') == 'MIT', 'Public skill must declare the repository MIT license')
    check(len(content.splitlines()) < 500, 'Keep SKILL.md below 500 lines; route detail to references')

expected_refs = ['psychology-brand.md', 'hooks-copy.md', 'video-production.md',
                 'analytics-testing.md', 'templates-examples.md', 'sources-evidence.md',
                 'hook-patterns.md']
for name in expected_refs:
    check((SKILL / 'references' / name).is_file(), f'Missing reference: {name}')

markdown_files = [p for p in ROOT.rglob('*.md') if not any(part.startswith('.') for part in p.relative_to(ROOT).parts)]
for path in markdown_files:
    text = path.read_text(encoding='utf-8')
    check(not re.search(r'[A-Z]:[\\/]Users[\\/]', text), f'{path.relative_to(ROOT)} contains a machine-specific user path')
    check(not re.search(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{24,})\b', text),
          f'{path.relative_to(ROOT)} appears to contain a credential')
    for link in re.findall(r'\]\(([^)\n]+)\)', text):
        link = link.strip().strip('<>')
        url = urlsplit(link)
        if url.scheme or link.startswith('#'):
            continue
        target = (path.parent / unquote(url.path)).resolve()
        check(target.is_relative_to(ROOT), f'{path.relative_to(ROOT)} link leaves repository: {link}')
        check(target.exists(), f'{path.relative_to(ROOT)} broken local link: {link}')

catalog = read_json(ROOT / 'skills.sh.json')
if isinstance(catalog, dict):
    groups = catalog.get('groupings', [])
    check(isinstance(groups, list) and bool(groups), 'Catalog needs at least one grouping')
    for group in groups:
        check(isinstance(group.get('title'), str) and bool(group['title']), 'Catalog group needs a title')
        check(group.get('skills') == [SKILL_NAME], 'Catalog grouping must reference the published skill')

evals = read_json(ROOT / 'evals/evals.json')
if isinstance(evals, dict):
    check(evals.get('skill_name') == SKILL_NAME, 'Evaluation skill name must match metadata')
    entries = evals.get('evals', [])
    check(len(entries) == 3, 'Preserve the three initial regression prompts')
    check(len({entry.get('id') for entry in entries}) == len(entries), 'Evaluation IDs must be unique')
    for entry in entries:
        check(bool(entry.get('prompt')) and bool(entry.get('expected_output')), 'Each evaluation needs a prompt and expected output')
        check(len(entry.get('expectations', [])) == 8, 'Each initial evaluation needs its eight expectations')
        check(entry.get('files') == [], 'Initial evaluation prompts should not depend on private input files')

summary = read_json(ROOT / 'evals/summary.json')
if isinstance(summary, dict):
    check(summary.get('skill_name') == SKILL_NAME, 'Result summary must name the published skill')
    check(summary.get('runs_per_configuration') == 1, 'Initial evaluation summary must preserve one-sample scope')
    check(len(summary.get('tasks', [])) == 3, 'Result summary needs three tasks')
    check(bool(summary.get('limitations')), 'Evaluation limitations must remain explicit')

manifest = read_json(SKILL / 'references/source-manifest.json')
if isinstance(manifest, dict):
    check(manifest.get('originals_required_at_runtime') is False, 'Runtime must not depend on the original supplied files')
    for source in manifest.get('sources', []):
        check(bool(re.fullmatch(r'[0-9a-f]{64}', source.get('sha256', ''))), 'Source fingerprints must be SHA-256 hashes')

if errors:
    for error in errors:
        print('FAIL:', error)
    sys.exit(1)

print(f'PASS: metadata, {len(expected_refs)} references, {len(markdown_files)} Markdown documents, local links, catalog, provenance, and evaluation schema.')
print('Structural checks do not grade creative quality or establish audience performance.')

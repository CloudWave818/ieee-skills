#!/usr/bin/env bash
set -euo pipefail

PULL=0
CHECK=0
DRY_RUN=0
DEST="${HOME}/.codex/skills"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --pull)
      PULL=1
      shift
      ;;
    --check)
      CHECK=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --dest)
      DEST="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SKILLS_DIR="${REPO_ROOT}/skills"

check_skill_tree() {
  if [[ ! -d "${SKILLS_DIR}" ]]; then
    echo "skills directory not found: ${SKILLS_DIR}" >&2
    exit 1
  fi

  shopt -s nullglob
  local skill_dirs=("${SKILLS_DIR}"/ieee-*)
  shopt -u nullglob

  if [[ ${#skill_dirs[@]} -eq 0 ]]; then
    echo "no ieee-* skill directories found under ${SKILLS_DIR}" >&2
    exit 1
  fi

  local dir
  for dir in "${skill_dirs[@]}"; do
    if [[ ! -f "${dir}/SKILL.md" ]]; then
      echo "missing SKILL.md in ${dir}" >&2
      exit 1
    fi
  done

  if [[ ! -d "${SKILLS_DIR}/_shared" ]]; then
    echo "missing shared directory: ${SKILLS_DIR}/_shared" >&2
    exit 1
  fi

  echo "Skill tree check passed."
}

if [[ "${PULL}" -eq 1 ]]; then
  if ! command -v git >/dev/null 2>&1; then
    echo "git is not available. Install git or run without --pull." >&2
    exit 1
  fi
  git -C "${REPO_ROOT}" pull
fi

check_skill_tree

if [[ "${CHECK}" -eq 1 ]]; then
  exit 0
fi

mkdir -p "${DEST}"

echo "Installing skills from ${SKILLS_DIR}"
echo "Installing skills to   ${DEST}"

for item in "${SKILLS_DIR}"/_shared "${SKILLS_DIR}"/ieee-*; do
  [[ -d "${item}" ]] || continue
  name="$(basename "${item}")"
  target="${DEST}/${name}"

  if [[ "${DRY_RUN}" -eq 1 ]]; then
    echo "[dry-run] copy ${item} -> ${target}"
    continue
  fi

  rm -rf "${target}"
  cp -R "${item}" "${target}"
  echo "Installed ${name}"
done

echo "Done. Restart Codex or start a new turn for updated skills to be discovered."

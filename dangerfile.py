touched_files = danger.git.modified_files + danger.git.created_files
has_source_changes = any(map(lambda f: f.startswith("danger_python"), touched_files))
has_changelog_entry = "CHANGELOG.md" in touched_files
is_trivial = "#trivial" in danger.github.pr.title

if has_source_changes and not has_changelog_entry and not is_trivial:
    warn("Please, add a CHANGELOG.md entry for non-trivial changes")

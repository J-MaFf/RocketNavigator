# Copilot Instructions

## Code Style & Formatting Standards

### Commit Messages (Conventional Commits)
Use the following prefixes for all commits:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes (formatting, missing semicolons, etc.)
- `refactor:` Code refactoring without changing behavior
- `perf:` Performance improvements
- `test:` Add or update tests
- `chore:` Maintenance, dependency updates, CI/CD
- `ci:` CI/CD pipeline changes
- `revert:` Revert a previous commit

Example: `feat: Add ETA automation with timezone awareness`

### PR Titles (Emoji Prefix)
Use emoji prefix followed by brief description:
- `✨ Add new feature`
- `🐛 Fix bug or issue`
- `📚 Update documentation`
- `🔧 Maintenance or refactoring`
- `🎯 Refactor or restructure code`
- `🚀 Deploy or release feature`
- `⚡ Performance improvement`
- `🧪 Add or update tests`

Example: `✨ Add interactive task selection with rich UI`

### PR Body (GitHub-Flavored Markdown)
Structure all PR descriptions with these sections:
```markdown
### What does this PR do?
Brief explanation of changes and what was implemented.

### Why are we doing this?
Context, motivation, and reason for the changes.

### How should this be tested?
Testing instructions, test cases, and validation steps.

### Any deployment notes?
Environment variables, migrations, breaking changes, or special instructions.
```

Include related issue references: `Closes #71, #77` (at end of description)

### PR Metadata Requirements
Always ensure the following metadata is set on every PR:
- **Labels**: Assign relevant labels (e.g., `enhancement`, `bug`, `documentation`, `refactor`, `testing`)
- **Assignees**: Assign to yourself (J-MaFf)
- **Issues**: Link all related issues in the PR description and GitHub's linked issues feature

**Using GitHub CLI to set metadata:**

```bash
# Add a single label
gh issue edit <PR_NUMBER> --add-label "documentation"

# Add multiple labels
gh issue edit <PR_NUMBER> --add-label "documentation" --add-label "enhancement"

# Assign to yourself
gh issue edit <PR_NUMBER> --add-assignee <USERNAME>

# Complete metadata setup example (add labels and assignee)
gh issue edit 84 --add-label "documentation" --add-assignee "J-MaFf"
```

Note: Use `gh issue edit` for both issues and pull requests. Replace `<PR_NUMBER>` with the PR number and `<USERNAME>` with the GitHub username. Labels must exist in the repository; check available labels with `gh label list`.

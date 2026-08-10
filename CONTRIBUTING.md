# Contributing to Good First Issues

Thank you for your interest in contributing! This is a project aimed at helping developers find good opportunities in open source, and this project is also available to be that opportunity :).

## Important note

**We are all learning here**. There is no problem at all with making mistakes, and iterating. But please, try solving the problems yourself. Using an LLM at some point to understand what is happening is OK, but **do not**:
- **Use this repo for contribution farming**: don't block the opportunity for others to onboard genuinely.
- **Generate messages with LLMs**: nobody will judge you for your English. AI generated text may be asked to be rewritten.

**Only one open PR per issue and per user at a time.**

## How to contribute
- Browse open issues. You can pick one labeled `good first issue` if you want to get started with an easy one.
- **Comment on the issue before you start** so I can assign it to you. This is how issues get claimed here, and it is what stops two people from doing the same work.
- Fork the repository and ideally create a branch with a descriptive name of what you are solving.
- **Submit a pull request to main** with a clear description of your changes. If it's related with an existing Issue, please link it.
- PRs are expected to follow the [PULL REQUEST TEMPLATE](./.github/PULL_REQUEST_TEMPLATE.md)

## Running tests

See [TESTING.md](TESTING.md) for instructions on running the test suite.

Every pull request runs the tests automatically and **must keep coverage at 100%**. If you add code, add its tests in the same PR — CI will fail otherwise.

## Code style
This project uses Python, Javascript, HTML, CSS and Markdown. Try to follow the existing style of the code, it is based on the PEP 8 conventions.

## Questions & Other Issues
Open an issue if you:
- Have any questions before starting.
- Want to solve a specific problem that is not reflected in the Issues opened at the moment.

## Reviews

**Anyone can comment on a PR**: feedback from other contributors is welcome and useful.

- **A PR solves one issue.** If you spot something else while you are in there, open a new issue instead of fixing it in the same PR. Someone may already be working on it.
- **An issue someone else is already solving is not yours to finish.** If a PR is open for it, comment on it, don't send your own version of the same fix.
- **Use `Comment` for suggestions**: preferences, style, ideas for later. It doesn't block anything, and it is the right button for almost everything.
- **`Request changes` is for things that are wrong**: a bug, a failing test, something that doesn't do what the issue asked. It blocks the merge until the reviewer resolves it, so it is reserved for collaborators.

If you receive a `Request changes`, something needs fixing before the PR can go in. A `Comment` is a suggestion, you are free to take it or leave it.

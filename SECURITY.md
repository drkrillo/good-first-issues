# Security Policy

## Supported Versions

The latest release and the `main` branch are currently supported.

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it privately through GitHub's security advisory system:

https://github.com/drkrillo/good-first-issues/security/advisories/new

Please do not report security vulnerabilities through public issues, pull requests, or discussions.

When submitting a vulnerability report, please include:

- The affected version or commit.
- Clear steps to reproduce the vulnerability.
- The potential impact of the vulnerability.
- Any known mitigations or workarounds.

Providing this information will help us investigate and address the vulnerability effectively.

## Scope

The following components are within the scope of this security policy:

- `action.yml`
- `app/`
- `.github/workflows/`
- `app/mcp_server.py`
- `index.html`

## Out of Scope

The following are outside the scope of this security policy:

- Vulnerabilities in third-party dependencies. Please report these to the maintainers of the affected dependency.
- Vulnerabilities in repositories listed in the project's dataset.

## What to Expect

We will review submitted vulnerability reports and investigate confirmed security issues.

If a reported vulnerability is confirmed, we will:

1. Create a GitHub Security Advisory for the vulnerability.
2. Develop and release an appropriate fix.
3. Credit the reporter for responsibly disclosing the vulnerability.

We follow a 90-day disclosure timeline for confirmed vulnerabilities. This provides time to investigate the issue, develop a fix, and release the fix before public disclosure.

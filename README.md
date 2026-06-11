<div align="center">

# Good First Issues

[![Update Issues](https://github.com/drkrillo/good-first-issues/actions/workflows/update-issues.yml/badge.svg)](https://github.com/drkrillo/good-first-issues/actions/workflows/update-issues.yml)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Good%20First%20Issues-green?logo=github)](https://github.com/marketplace/actions/good-first-issues)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

This repo helps you automatically discover open issues labeled **good first issue** across GitHub repositories. It is a **community driven project**, and always welcoming interested contributors. Updated daily via GitHub Actions.

</div>

---

## Overview

This tool scans public repositories for a given list of GitHub usernames or organizations, collects issues tagged with `good first issue`, and renders them into a browsable table. It is available both as a **standalone script** and as a **GitHub Action** on the Marketplace.

## Documentation

| Resource | Description |
|---|---|
| [Contributing](CONTRIBUTING.md) | Guidelines for contributing to this project. It's not that long. Read it! |
| [Action Usage Guide](docs/action-usage.md) | How to use this Action in your workflows |
| [Local Setup](docs/setup.md) | How to install, configure, and run the project locally |
| [How It Works](docs/how-it-works.md) | Architecture and internal logic |
| [Testing](TESTING.md) | How to run the test suite |

## Usage as a GitHub Action

Add the following step to any workflow file:

```yaml
- name: Fetch good first issues
  uses: drkrillo/good-first-issues@main
  with:
    usernames: "owner1,owner2,owner3"
    github-token: ${{ secrets.GITHUB_TOKEN }}
    output-format: csv          # csv (default) or json
    output-path: issues.csv     # default: good_first_issues.csv
```

The action outputs a CSV or JSON file with all discovered issues.

| Input | Required | Default | Description |
|---|---|---|---|
| `github-token` | Yes | — | GitHub token for API access |
| `usernames` | No | `''` | Comma-separated GitHub usernames or organizations to scan |
| `output-format` | No | `csv` | Output format: `csv` or `json` |
| `output-path` | No | `good_first_issues.csv` | Path where the output file is written |

For complete workflow examples, output schema, and authentication details, see the [Action Usage Guide](docs/action-usage.md).

---

## ⭐ Support

Did the repo helped you finding an issue? learning something? Consider giving it a star :) Helps keeping me motivated!

---

## Good First Issues <sub><sub>Last run: 2026-06-11</sub></sub>

| Repo | Language | Title | Comments |
|---|---|---|---|
| microsoft/ebpf-for-windows | C | [OpenCppCoverage install step fails silently](https://github.com/microsoft/ebpf-for-windows/issues/5330) | 0 |
| microsoft/ebpf-for-windows | C | [Code quality: NULL pointer dereference on global_helper_function_addresses in program attach](https://github.com/microsoft/ebpf-for-windows/issues/5292) | 0 |
| microsoft/ebpf-for-windows | C | [Cleanup: catch2 now allows multiple threads](https://github.com/microsoft/ebpf-for-windows/issues/4553) | 0 |
| microsoft/msquic | C | [Miss check for the return value of CXPLAT_ALLOC_NONPAGED and CxPlatPoolAlloc](https://github.com/microsoft/msquic/issues/5233) | 0 |
| microsoft/jbpf | C | [jbpf_io_ipc_test passes with error messages](https://github.com/microsoft/jbpf/issues/54) | 0 |
| microsoft/ebpf-for-windows | C | [Update tests/sample/undocked/map.c](https://github.com/microsoft/ebpf-for-windows/issues/4547) | 1 |
| microsoft/ntttcp | C | [per-thread throughput is always 0.00 with ntttcp version 5.40.](https://github.com/microsoft/ntttcp/issues/24) | 1 |
| microsoft/PowerToys | C | [.opus support for Peek](https://github.com/microsoft/PowerToys/issues/42576) | 2 |
| microsoft/msquic | C | [Support in-memory certificate stores](https://github.com/microsoft/msquic/issues/4951) | 2 |
| microsoft/ebpf-for-windows | C | [ebpf-verifier is cloned twice](https://github.com/microsoft/ebpf-for-windows/issues/4174) | 2 |
| microsoft/msquic | C | [Failing to use close-on-exec](https://github.com/microsoft/msquic/issues/4980) | 3 |
| microsoft/aspire | C# | [aspire deploy/publish fail in Aspire terminal](https://github.com/microsoft/aspire/issues/18017) | 0 |
| microsoft/aspire | C# | [aspire extension telemetry should include the Aspire version being targeted by the AppHost](https://github.com/microsoft/aspire/issues/17921) | 0 |
| microsoft/aspire | C# | [[bug] aspire describe --non-interactive crashes with 'An unexpected error occurred' when no AppHost in cwd](https://github.com/microsoft/aspire/issues/17619) | 0 |
| microsoft/aspire | C# | [[bug] `aspire describe --format json` exposes plaintext values of secret parameters in dependent resources' env vars](https://github.com/microsoft/aspire/issues/17616) | 0 |
| microsoft/CsWin32 | C# | [Inherited COM methods do not have documentation comments](https://github.com/microsoft/CsWin32/issues/1391) | 0 |
| microsoft/profile-explorer | C# | [Mapping code gap?](https://github.com/microsoft/profile-explorer/issues/7) | 0 |
| microsoft/aspire | C# | [VS Code extension should execute resource commands without opening the terminal](https://github.com/microsoft/aspire/issues/17911) | 1 |
| microsoft/aspire | C# | [Dashboard: "Export JSON" resource action opens Text Visualizer instead of direct download; name and sensitive-value message need improvement](https://github.com/microsoft/aspire/issues/17690) | 1 |
| microsoft/aspire | C# | [Add aspire doctor hint when legacy .aspire/settings.json is detected](https://github.com/microsoft/aspire/issues/17632) | 1 |
| microsoft/aspire | C# | [Add VSCode commands to open the dashboard](https://github.com/microsoft/aspire/issues/16815) | 1 |
| microsoft/aspire | C# | [Aspire dashboard - URL column click shows details](https://github.com/microsoft/aspire/issues/12307) | 1 |
| microsoft/kiota | C# | [Stacktrace on exceptions](https://github.com/microsoft/kiota/issues/7014) | 1 |
| microsoft/aspire | C# | [Provide CSV export option in dashboard console logs](https://github.com/microsoft/aspire/issues/11121) | 2 |
| microsoft/aspire | C# | [CLI error message when AppHost exits before backchannel connection is vague and missing exit code](https://github.com/microsoft/aspire/issues/17277) | 3 |
| microsoft/aspire | C# | [[nit]: "Operation cancelled by user action" log is too incessant](https://github.com/microsoft/aspire/issues/9311) | 3 |
| microsoft/aspire | C# | [`aspire new` lists "yes" and "no" options in inconsistent orders](https://github.com/microsoft/aspire/issues/12272) | 4 |
| microsoft/mcp | C# | [[COMMUNITY] Auto generate CHANGELOG, including adding contributors for each release](https://github.com/microsoft/mcp/issues/156) | 4 |
| microsoft/aspire | C# | [Improve Exception Message for Missing Project Metadata Annotation in ResourceContainerImageBuilder.cs](https://github.com/microsoft/aspire/issues/11299) | 12 |
| microsoft/snmalloc | C++ | [Implement accurate size storage for Windows `_msize` and `_recalloc`](https://github.com/microsoft/snmalloc/issues/786) | 0 |
| microsoft/react-native-windows | C++ | [Scroll wheel behavior differs significantly in new architecture (Windows App SDK) vs WinUI 3 Gallery app](https://github.com/microsoft/react-native-windows/issues/14653) | 1 |
| microsoft/react-native-windows | C++ | [Deprecate autolink functionality to copy flags from react-native.config.js into ExperimentalFeature.props.](https://github.com/microsoft/react-native-windows/issues/14601) | 1 |
| microsoft/terminal | C++ | ["Export text" action invoked from cmd paletter forwards Enter key](https://github.com/microsoft/terminal/issues/20188) | 3 |
| microsoft/react-native-windows | C++ | [[Bug] init-windows adds incorrect name of Native Codegen File Include](https://github.com/microsoft/react-native-windows/issues/15094) | 4 |
| godotengine/godot | C++ | [[Godot v4.4] Gizmos exponentially increasing Draw Calls and Objects when turned on](https://github.com/godotengine/godot/issues/103676) | 25 |
| godotengine/godot | C++ | [You're breathtaking!](https://github.com/godotengine/godot/issues/100000) | 34 |
| godotengine/godot | C++ | [[TRACKER] Unit tests to add or improve](https://github.com/godotengine/godot/issues/43440) | 254 |
| mattermost/mattermost-developer-documentation | CSS | [Help Wanted: Gitpod docs have outdated screenshots for the mattermost GitHub repository](https://github.com/mattermost/mattermost-developer-documentation/issues/1244) | 2 |
| mattermost/mattermost-developer-documentation | CSS | [Help Wanted: Document how to do local development on a plugin that requires an E20/Enterprise license](https://github.com/mattermost/mattermost-developer-documentation/issues/815) | 2 |
| mattermost/mattermost-developer-documentation | CSS | [Enhance Documentation for Registering Plugins on the Mattermost Webapp Sidebar](https://github.com/mattermost/mattermost-developer-documentation/issues/1352) | 3 |
| mattermost/mattermost-developer-documentation | CSS | [Help Wanted: Open all external links in a new browser tab](https://github.com/mattermost/mattermost-developer-documentation/issues/1142) | 11 |
| godotengine/emacs-gdscript-mode | Emacs Lisp | [Rewrite gdscript-imenu to provide GDScript-specific tables](https://github.com/godotengine/emacs-gdscript-mode/issues/89) | 0 |
| godotengine/emacs-gdscript-mode | Emacs Lisp | [Buffer does not revert or update instantly after formatting buffer](https://github.com/godotengine/emacs-gdscript-mode/issues/88) | 3 |
| godotengine/godot-benchmarks | GDScript | [[Call to Action] Benchmarks for the benchmark server](https://github.com/godotengine/godot-benchmarks/issues/36) | 5 |
| godotengine/godot-benchmarks | GDScript | [[TRACKER] Benchmarks to create](https://github.com/godotengine/godot-benchmarks/issues/11) | 11 |
| hashicorp/packer-plugin-azure | Go | [Option to delete secret when build_key_vault_name is supplied](https://github.com/hashicorp/packer-plugin-azure/issues/506) | 0 |
| hashicorp/nomad | Go | [unclear message in task event from executor crash](https://github.com/hashicorp/nomad/issues/24220) | 0 |
| hashicorp/packer-plugin-googlecompute | Go | [Add disk_attachment labels](https://github.com/hashicorp/packer-plugin-googlecompute/issues/210) | 0 |
| hashicorp/vault-secrets-operator | Go | [Add allowedNamespaces spec to helm chart values.yaml](https://github.com/hashicorp/vault-secrets-operator/issues/426) | 0 |
| hashicorp/pandora | Go | [tools/generator-terraform: validation function on lists/sets](https://github.com/hashicorp/pandora/issues/1514) | 0 |
| hashicorp/waypoint | Go | [Replace pluralize helper in user-facing text](https://github.com/hashicorp/waypoint/issues/3446) | 0 |
| hashicorp/consul-template | Go | [Feature: parseInt and parseFloat should handle json.Number](https://github.com/hashicorp/consul-template/issues/1584) | 0 |
| mattermost/mattermost-plugin-mscalendar | Go | [Improve layout of `viewcal` command](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/325) | 0 |
| mattermost/mattermost-plugin-mscalendar | Go | [Use button instead of link and update language for `/trigger connect` message](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/316) | 0 |
| mattermost/mattermost-plugin-mscalendar | Go | [Review `viewcal` command dates or help text](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/315) | 0 |
| mattermost/mattermost-plugin-apps | Go | [Test-App Subscribe commands error when trying to add a bot to the channel](https://github.com/mattermost/mattermost-plugin-apps/issues/461) | 0 |
| mattermost/release-bot | Go | [Improve Bot Metrics](https://github.com/mattermost/release-bot/issues/4) | 0 |
| mattermost/ops-tool | Go | [Integrate GitLab with Ops Tool](https://github.com/mattermost/ops-tool/issues/32) | 0 |
| mattermost/notice-file-generator | Go | [Missing dependencies for mattermost-focalboard project](https://github.com/mattermost/notice-file-generator/issues/11) | 0 |
| mattermost/notice-file-generator | Go | [Unrecognized imports for mattermost-server](https://github.com/mattermost/notice-file-generator/issues/10) | 0 |
| mattermost/ops-tool | Go | [Mattermost go client usage](https://github.com/mattermost/ops-tool/issues/30) | 0 |
| mattermost/ops-tool | Go | [Add data_source support so Dialog Options will be dynamic](https://github.com/mattermost/ops-tool/issues/29) | 0 |
| mattermost/ops-tool | Go | [Add Support For Multiple Slash Commands](https://github.com/mattermost/ops-tool/issues/27) | 0 |
| mattermost/ops-tool | Go | [Configure Mattermost Server on Startup](https://github.com/mattermost/ops-tool/issues/26) | 0 |
| mattermost/mattermost-plugin-wrangler | Go | [With Mattermost v7.1 the reactions table has a channelid column](https://github.com/mattermost/mattermost-plugin-wrangler/issues/136) | 0 |
| mattermost/ops-tool | Go | [Remove external shell script support](https://github.com/mattermost/ops-tool/issues/23) | 0 |
| mattermost/mattermost-plugin-demo | Go | [Make an example of using the Custom Status plugin API methods](https://github.com/mattermost/mattermost-plugin-demo/issues/146) | 0 |
| mattermost/mattermost-plugin-mscalendar | Go | [Any user-facing error messages should be user-friendly](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/189) | 0 |
| mattermost/mattermost-plugin-github | Go | [Investigate proper parsing of API errors on webapp side](https://github.com/mattermost/mattermost-plugin-github/issues/337) | 0 |
| mattermost/mattermost-plugin-github | Go | [Render markdown in tooltip with post-utils, instead of ReactMarkdown](https://github.com/mattermost/mattermost-plugin-github/issues/327) | 0 |
| mattermost/mattermost-plugin-community | Go | [Add slash command autocomplete functionality](https://github.com/mattermost/mattermost-plugin-community/issues/16) | 0 |
| mattermost/mattermost-plugin-confluence | Go | [Support notifications to users "watching" in Confluence](https://github.com/mattermost/mattermost-plugin-confluence/issues/50) | 0 |
| mattermost/mattermost-plugin-confluence | Go | [Add per user Authentication for Confluence](https://github.com/mattermost/mattermost-plugin-confluence/issues/49) | 0 |
| mattermost/mattermost-plugin-mscalendar | Go | [Allow "create event" command to accept spaces in values](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/97) | 0 |
| mattermost/mattermost-plugin-github | Go | [Create tests for `createIssue()` method](https://github.com/mattermost/mattermost-plugin-github/issues/223) | 0 |
| mattermost/mattermost-plugin-mscalendar | Go | [Add mapped Mattermost users as attendees in CreateEvent API method](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/28) | 0 |
| hashicorp/nomad | Go | [Improve description of Consul tokens to include client information](https://github.com/hashicorp/nomad/issues/28048) | 1 |
| hashicorp/terraform-provider-kubernetes | Go | [Add CSI Driver fsGroup Support](https://github.com/hashicorp/terraform-provider-kubernetes/issues/2702) | 1 |
| hashicorp/terraform-provider-aws | Go | [[Docs]: Document necessary dependency between aws_eks_access_entry and aws_eks_access_policy_association](https://github.com/hashicorp/terraform-provider-aws/issues/40951) | 1 |
| hashicorp/nomad | Go | [show embedded template diffs line-by-line](https://github.com/hashicorp/nomad/issues/23603) | 1 |
| hashicorp/packer-plugin-azure | Go | [Improve error messaging for "Managed Images not supporting ARM64 images error"](https://github.com/hashicorp/packer-plugin-azure/issues/367) | 1 |
| hashicorp/waypoint | Go | [Show job created time in CLI output](https://github.com/hashicorp/waypoint/issues/4293) | 1 |
| hashicorp/nomad | Go | [docs: correctly detail endpoints that support PUT and POST](https://github.com/hashicorp/nomad/issues/15243) | 1 |
| hashicorp/terraform-provider-azurerm | Go | [r/data_factory_linked_service_postgresql: export `key_vault_connection_string`](https://github.com/hashicorp/terraform-provider-azurerm/issues/16500) | 1 |
| hashicorp/waypoint | Go | [Makefile: Add a make target to generate changelog text files](https://github.com/hashicorp/waypoint/issues/3219) | 1 |
| mattermost/mattermost-plugin-google-calendar | Go | [`/gcal viewcal` and daily summary show up declined events](https://github.com/mattermost/mattermost-plugin-google-calendar/issues/53) | 1 |
| mattermost/mattermost-plugin-mscalendar | Go | [Add space between time and AM/PM for events](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/318) | 1 |
| mattermost/mattermost-plugin-apps | Go | [If the App stops running I see a whole HTML response as the error](https://github.com/mattermost/mattermost-plugin-apps/issues/462) | 1 |
| mattermost/mattermost-plugin-mscalendar | Go | [Change Azure URL?](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/240) | 1 |
| mattermost/mattermost-plugin-wrangler | Go | [Wrangling a post does not bring followers over to the new thread](https://github.com/mattermost/mattermost-plugin-wrangler/issues/135) | 1 |
| mattermost/mattermost-plugin-github | Go | [Create Issue modal should disable labels etc instead of hiding the elements](https://github.com/mattermost/mattermost-plugin-github/issues/438) | 1 |
| mattermost/mattermost-plugin-nps | Go | [Use SiteURL for all calls from the webapp](https://github.com/mattermost/mattermost-plugin-nps/issues/70) | 1 |
| mattermost/mattermost-plugin-google-calendar | Go | [Improve error handling in `completeCalendar` to avoid panic](https://github.com/mattermost/mattermost-plugin-google-calendar/issues/8) | 1 |
| mattermost/mattermost-plugin-github | Go | [Use custom post type to display TODO list](https://github.com/mattermost/mattermost-plugin-github/issues/86) | 1 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: aws_bedrockagentcore_memory_strategy missing reflection configuration for EPISODIC type](https://github.com/hashicorp/terraform-provider-aws/issues/47938) | 2 |
| hashicorp/terraform-provider-aws | Go | [aws_fms_policy resource_tag_logical_operator not correctly displaying diff during a plan](https://github.com/hashicorp/terraform-provider-aws/issues/47771) | 2 |
| hashicorp/terraform-provider-aws | Go | [Add private DNS endpoint attribute to `aws_dsql_cluster` resource](https://github.com/hashicorp/terraform-provider-aws/issues/47596) | 2 |
| hashicorp/terraform-provider-aws | Go | [aws_quicksight_dashboard / aws_quicksight_analysis: scatter_plot_categorically_aggregated_field_wells missing label block](https://github.com/hashicorp/terraform-provider-aws/issues/46529) | 2 |
| hashicorp/terraform-provider-aws | Go | [Can't update aws_controltower_baseline resource version](https://github.com/hashicorp/terraform-provider-aws/issues/45871) | 2 |
| hashicorp/terraform-provider-aws | Go | [iot_topic_rule CloudWatch metric timestamp Wrong validator](https://github.com/hashicorp/terraform-provider-aws/issues/45375) | 2 |
| hashicorp/packer-plugin-azure | Go | [Create a technical document giving detailed steps on how to configure Packer to use private Azure vNet with public IP](https://github.com/hashicorp/packer-plugin-azure/issues/503) | 2 |
| hashicorp/terraform-provider-aws | Go | [QuickSight reguires Admin or Admin Pro group](https://github.com/hashicorp/terraform-provider-aws/issues/42457) | 2 |
| hashicorp/terraform-provider-aws | Go | [aws_pipes_pipe resource does not support target Timestream for Live Analytics](https://github.com/hashicorp/terraform-provider-aws/issues/42400) | 2 |
| hashicorp/terraform-provider-aws | Go | [[Docs]: A notation may cause confusion in import exmaple](https://github.com/hashicorp/terraform-provider-aws/issues/40935) | 2 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: Request warning for possible OpenSearch blue/green deployments](https://github.com/hashicorp/terraform-provider-aws/issues/40045) | 2 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: aws_redshiftserverless_namespace - manageAdminPassword/redshiftIdcApplicationArn](https://github.com/hashicorp/terraform-provider-aws/issues/35135) | 2 |
| hashicorp/packer-plugin-openstack | Go | [Verify checksums of images imported via external_source_image_url](https://github.com/hashicorp/packer-plugin-openstack/issues/116) | 2 |
| hashicorp/copywrite | Go | [Support overriding `ensureCorrectName` (e.g. support `LICENSE.md` instead of `LICENSE`)](https://github.com/hashicorp/copywrite/issues/101) | 2 |
| hashicorp/packer-plugin-qemu | Go | [Support multiple accelerators](https://github.com/hashicorp/packer-plugin-qemu/issues/160) | 2 |
| hashicorp/nomad | Go | [[documentation] job `port` does not provide information how to bind port to 0.0.0.0](https://github.com/hashicorp/nomad/issues/18338) | 2 |
| hashicorp/terraform-provider-azurerm | Go | [Support for azurerm_relay_namespace/azurerm_relay_hybrid_connection data sources](https://github.com/hashicorp/terraform-provider-azurerm/issues/21144) | 2 |
| hashicorp/nomad | Go | [hcl2 coalesce function returning empty string element when the second element is a non-empty string](https://github.com/hashicorp/nomad/issues/15599) | 2 |
| hashicorp/waypoint | Go | [CLI: DRY up how the CLI shows deployment and release URLs](https://github.com/hashicorp/waypoint/issues/4209) | 2 |
| mattermost/mattermost-plugin-github | Go | [Explain in docs not to fill out the `Enterprise Base URL` config setting if the GH Enterprise instance is hosted on GitHub's domain](https://github.com/mattermost/mattermost-plugin-github/issues/714) | 2 |
| mattermost/mattermost-plugin-jira | Go | [Add `/jira setup` to slash command autocomplete](https://github.com/mattermost/mattermost-plugin-jira/issues/892) | 2 |
| mattermost/mattermost-plugin-github | Go | [Able to Unsubscribe from Repositories without being Subscribed](https://github.com/mattermost/mattermost-plugin-github/issues/546) | 2 |
| mattermost/mattermost-plugin-github | Go | [Show author of PR/issue in link tooltip](https://github.com/mattermost/mattermost-plugin-github/issues/439) | 2 |
| mattermost/mattermost-plugin-github | Go | [Support filtering of repositories in RHS](https://github.com/mattermost/mattermost-plugin-github/issues/265) | 2 |
| mattermost/mattermost-plugin-mscalendar | Go | [Improve Daily Summary weekday setup](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/56) | 2 |
| kubernetes/cloud-provider-openstack | Go | [[all]: openstack API debugger shows `client.go:128` for all calls](https://github.com/kubernetes/cloud-provider-openstack/issues/2300) | 3 |
| kubernetes/kops | Go | [Update AWS China documentation with Route53 Support](https://github.com/kubernetes/kops/issues/9138) | 3 |
| microsoft/retina | Go | [Update documentation with Hubble CLI and Hubble UI deployment instructions on Retina.](https://github.com/microsoft/retina/issues/1387) | 3 |
| hashicorp/terraform-provider-aws | Go | [data/aws_bedrock_foundation_model: modelLifecycle attribute not exposed](https://github.com/hashicorp/terraform-provider-aws/issues/47779) | 3 |
| hashicorp/terraform-provider-aws | Go | [aws_s3tables_table_replication: Create fails with "A version token is not specified"](https://github.com/hashicorp/terraform-provider-aws/issues/46675) | 3 |
| hashicorp/terraform-provider-aws | Go | [[EMR on EKS] aws_emrcontainers_job_template: add support for job_template_data.parameter_configuration](https://github.com/hashicorp/terraform-provider-aws/issues/46502) | 3 |
| hashicorp/terraform-provider-aws | Go | [aws_transfer_server::identity_provider_type causes replacement](https://github.com/hashicorp/terraform-provider-aws/issues/46229) | 3 |
| hashicorp/terraform-provider-aws | Go | [Unable to update a RAM share to use the latest version of a custom permission](https://github.com/hashicorp/terraform-provider-aws/issues/46219) | 3 |
| hashicorp/terraform-provider-kubernetes | Go | [Helper function for creating `env` name/value pair list from a map.](https://github.com/hashicorp/terraform-provider-kubernetes/issues/2767) | 3 |
| hashicorp/terraform-provider-aws | Go | [aws_efs_replication_configuration is missing role-arn for cross-account-replication](https://github.com/hashicorp/terraform-provider-aws/issues/42814) | 3 |
| hashicorp/terraform-provider-aws | Go | [AWS IVS Real Time Stage Terraform Module](https://github.com/hashicorp/terraform-provider-aws/issues/42644) | 3 |
| hashicorp/terraform-provider-aws | Go | [[Bug]: SageMaker App Image Config: API rejects valid UID/GID pairs defined in provider schema](https://github.com/hashicorp/terraform-provider-aws/issues/40976) | 3 |
| hashicorp/terraform-provider-aws | Go | [[Bug]: aws_emr_cluster Inappropriate value for attribute "configurations": string required.](https://github.com/hashicorp/terraform-provider-aws/issues/39959) | 3 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: aws_sagemaker_domain add Hidden Image Versions options to the studio_web_portal_settings](https://github.com/hashicorp/terraform-provider-aws/issues/39876) | 3 |
| hashicorp/nomad | Go | [Show last job status in UI in jobs list](https://github.com/hashicorp/nomad/issues/23893) | 3 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: bootstrap_brokers_vpc_connectivity attributes on data.aws_msk_cluster](https://github.com/hashicorp/terraform-provider-aws/issues/34607) | 3 |
| hashicorp/terraform-provider-vault | Go | [Update vault_kubernetes_auth_backend_role Resource to support allowed_kubernetes_namespace_selector Field](https://github.com/hashicorp/terraform-provider-vault/issues/1882) | 3 |
| hashicorp/nomad | Go | [Enable k8s discovery support in go-discover](https://github.com/hashicorp/nomad/issues/16351) | 3 |
| hashicorp/terraform-provider-azurerm | Go | [There are a couple of issues with the Logic apps Standard terraform template shared at https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/logic_app_standard](https://github.com/hashicorp/terraform-provider-azurerm/issues/18351) | 3 |
| mattermost/mattermost-plugin-servicenow | Go | [Only allow user to select channels to add subscriptions to in which they are channel admins](https://github.com/mattermost/mattermost-plugin-servicenow/issues/188) | 3 |
| mattermost/mattermost-plugin-github | Go | [Support dismissing notifications from the RHS view](https://github.com/mattermost/mattermost-plugin-github/issues/620) | 3 |
| mattermost/mattermost-plugin-github | Go | [Support tooltip preview on hovering over RHS notifications](https://github.com/mattermost/mattermost-plugin-github/issues/619) | 3 |
| mattermost/mattermost-plugin-nps | Go | [JS error when telling Surveybot to disable the survey on old post](https://github.com/mattermost/mattermost-plugin-nps/issues/81) | 3 |
| mattermost/mattermost-plugin-zoom | Go | [Synch Status: When on a Zoom call, show as “Busy”](https://github.com/mattermost/mattermost-plugin-zoom/issues/170) | 3 |
| mattermost/mattermost-plugin-github | Go | [Register autolinks for GitHub URLs](https://github.com/mattermost/mattermost-plugin-github/issues/269) | 3 |
| microsoft/retina | Go | [hubble-relay image v1.15.0 missing h2 ALPN support that breaks hubble CLI (grpc-go >= 1.67)](https://github.com/microsoft/retina/issues/2165) | 4 |
| microsoft/terraform-provider-azuredevops | Go | [Full unit test suite isn't running on CI](https://github.com/microsoft/terraform-provider-azuredevops/issues/1439) | 4 |
| hashicorp/terraform-provider-aws | Go | [aws_ec2_transit_gateway_route_table_association support for timeouts block](https://github.com/hashicorp/terraform-provider-aws/issues/42705) | 4 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: `aws_cloudwatch_metric_alarm`: Add validation to prevent specifying both `metric` and `expression`](https://github.com/hashicorp/terraform-provider-aws/issues/41680) | 4 |
| hashicorp/terraform-provider-aws | Go | [[Docs]: quicksight_data_source](https://github.com/hashicorp/terraform-provider-aws/issues/41672) | 4 |
| hashicorp/terraform-provider-aws | Go | [[Bug]: aws_backup_selection `selection_tag` and `resources` do not interact as expected](https://github.com/hashicorp/terraform-provider-aws/issues/41274) | 4 |
| hashicorp/nomad | Go | [Render JSON String Diffs as JSON](https://github.com/hashicorp/nomad/issues/18103) | 4 |
| hashicorp/terraform-provider-aws | Go | [[Docs]: Add support for package version overrides on aws_amplify_app resource](https://github.com/hashicorp/terraform-provider-aws/issues/27768) | 4 |
| hashicorp/nomad | Go | [Less-imperious validation of variable error_message contents](https://github.com/hashicorp/nomad/issues/15075) | 4 |
| hashicorp/terraform-provider-aws | Go | [Add CodeArtifact Package Origin Controls](https://github.com/hashicorp/terraform-provider-aws/issues/26623) | 4 |
| hashicorp/terraform-provider-aws | Go | [Cannot get bucket configuration information from s3 data source](https://github.com/hashicorp/terraform-provider-aws/issues/26054) | 4 |
| hashicorp/terraform-provider-aws | Go | [Improve error message when AMI id was recently deregistered](https://github.com/hashicorp/terraform-provider-aws/issues/26046) | 4 |
| hashicorp/terraform-provider-aws | Go | [AWS network firewall: Ability to attach a firewall policy to a firewall within the same resource](https://github.com/hashicorp/terraform-provider-aws/issues/25352) | 4 |
| mattermost/mattermost-plugin-jira | Go | [Make epic link selector pull from epics search API](https://github.com/mattermost/mattermost-plugin-jira/issues/978) | 4 |
| mattermost/mattermost-plugin-nps | Go | [Fix for: EnablePermalinkPreviews kills nps plugin](https://github.com/mattermost/mattermost-plugin-nps/issues/85) | 4 |
| mattermost/mattermost-plugin-github | Go | [Only channel admins should be able to create subscription](https://github.com/mattermost/mattermost-plugin-github/issues/488) | 4 |
| mattermost/mattermost-plugin-jira | Go | [Jira's autolink should support issue links that contain a comment link in the URL](https://github.com/mattermost/mattermost-plugin-jira/issues/773) | 4 |
| mattermost/mattermost-plugin-github | Go | [Validate syntax when a subscription has an invalid label](https://github.com/mattermost/mattermost-plugin-github/issues/385) | 4 |
| mattermost/mattermost-plugin-github | Go | [Select types of events to subscribe to in a dialog box](https://github.com/mattermost/mattermost-plugin-github/issues/381) | 4 |
| mattermost/mattermost-plugin-demo | Go | [Perform config validation in its own function, rather than using `OnConfigurationChange` to check](https://github.com/mattermost/mattermost-plugin-demo/issues/110) | 4 |
| mattermost/mattermost-plugin-github | Go | [Handle case where sidebar API endpoints return null](https://github.com/mattermost/mattermost-plugin-github/issues/235) | 4 |
| kubernetes/autoscaler | Go | [Document VPA Helm chart on Kubernetes website](https://github.com/kubernetes/autoscaler/issues/9407) | 5 |
| kubernetes/kube-openapi | Go | [Having the same type embedded more than once breaks generation](https://github.com/kubernetes/kube-openapi/issues/129) | 5 |
| hashicorp/terraform-provider-aws | Go | [[New Resource]: aws_datazone_policy_grant](https://github.com/hashicorp/terraform-provider-aws/issues/46764) | 5 |
| hashicorp/nomad | Go | [option to run template.change_script on first render](https://github.com/hashicorp/nomad/issues/27429) | 5 |
| hashicorp/nomad | Go | [Provide output formatting options for Nomad job plan CLI](https://github.com/hashicorp/nomad/issues/27369) | 5 |
| hashicorp/terraform-provider-aws | Go | [[Bug]: Route 53 Resolver rule resource defines bad defaults for target configuration](https://github.com/hashicorp/terraform-provider-aws/issues/41523) | 5 |
| hashicorp/terraform-provider-aws | Go | [[Documentation]: Add example for specifying p12 certificate with `aws_sns_platform_application`](https://github.com/hashicorp/terraform-provider-aws/issues/40803) | 5 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: aws_dms_endpoint add additional redshift_settings parameters](https://github.com/hashicorp/terraform-provider-aws/issues/38814) | 5 |
| hashicorp/terraform-provider-aws | Go | [[Docs]: Import existing trail using ARN doesn't work, but it does if the trail name is used](https://github.com/hashicorp/terraform-provider-aws/issues/37179) | 5 |
| hashicorp/terraform-provider-aws | Go | [aws_redshiftserverless_namespace restore from snapshot](https://github.com/hashicorp/terraform-provider-aws/issues/35138) | 5 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: aws_acm_certificate should guide how to import certificates including transparency logging](https://github.com/hashicorp/terraform-provider-aws/issues/35093) | 5 |
| hashicorp/terraform-provider-aws | Go | [[Bug]: Resource aws_s3_bucket_versioning can't be created for s3 outpost bucket](https://github.com/hashicorp/terraform-provider-aws/issues/33119) | 5 |
| hashicorp/nomad | Go | [Scale job API endpoint documentation is inconsistent with observed behavior](https://github.com/hashicorp/nomad/issues/13056) | 5 |
| mattermost/mattermost-plugin-mscalendar | Go | [Re-implement autorespond feature](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/227) | 5 |
| mattermost/mattermost-plugin-github | Go | ["Someone replied to your comment thread" feature](https://github.com/mattermost/mattermost-plugin-github/issues/328) | 5 |
| mattermost/mattermost-plugin-confluence | Go | [Handle React warnings regarding non-DOM properties](https://github.com/mattermost/mattermost-plugin-confluence/issues/46) | 5 |
| mattermost/mattermost-plugin-github | Go | [Add alternative sorting functionality for RHS view](https://github.com/mattermost/mattermost-plugin-github/issues/242) | 5 |
| kubernetes/kube-state-metrics | Go | [Parse Nested Arrays does not work](https://github.com/kubernetes/kube-state-metrics/issues/2368) | 6 |
| hashicorp/terraform-provider-aws | Go | [Route53 Resolver Endpoint Hash Function Prevents Multiple IPs per Subnet When IP Address is Auto-Assigned](https://github.com/hashicorp/terraform-provider-aws/issues/43724) | 6 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: aws_athena_prepared_statement: Allow multiline (EOT) query strings to preserve comments and line breaks without update-in-place](https://github.com/hashicorp/terraform-provider-aws/issues/41469) | 6 |
| hashicorp/terraform-provider-aws | Go | [[Docs]: `aws_rds_cluster` add section for Major version upgrades and parameter `db_instance_parameter_group_name`](https://github.com/hashicorp/terraform-provider-aws/issues/27617) | 6 |
| hashicorp/vault-csi-provider | Go | [feat: Enable json logging format](https://github.com/hashicorp/vault-csi-provider/issues/177) | 6 |
| hashicorp/terraform-provider-aws | Go | [aws_iam_openid_connect_provider rejects valid "url"s](https://github.com/hashicorp/terraform-provider-aws/issues/26483) | 6 |
| hashicorp/waypoint | Go | [Registry insecure flag](https://github.com/hashicorp/waypoint/issues/3333) | 6 |
| mattermost/mattermost-plugin-jira | Go | [When an issue's assignee changes, the plugin should use the connected user's MM handle in the resulting post](https://github.com/mattermost/mattermost-plugin-jira/issues/943) | 6 |
| mattermost/mattermost-plugin-github | Go | [Make new events for assigning](https://github.com/mattermost/mattermost-plugin-github/issues/340) | 6 |
| mattermost/mattermost-plugin-starter-template | Go | [Include stubs for all hooks to get going quickly](https://github.com/mattermost/mattermost-plugin-starter-template/issues/110) | 6 |
| mattermost/mattermost-plugin-mscalendar | Go | [Make the OAuth2 landing page](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/94) | 6 |
| kubernetes/minikube | Go | [minikube should not warn you to NOT use virtualbox if it auto-selected it](https://github.com/kubernetes/minikube/issues/15456) | 7 |
| kubernetes/perf-tests | Go | [Check watch terminations from clusters loader tests](https://github.com/kubernetes/perf-tests/issues/2054) | 7 |
| kubernetes/minikube | Go | [Wrong error message on minikube tunnel without Administrator privilege on Windows](https://github.com/kubernetes/minikube/issues/9589) | 7 |
| hashicorp/terraform-provider-aws | Go | [Error: Unsupported argument: blue_green_update](https://github.com/hashicorp/terraform-provider-aws/issues/44488) | 7 |
| hashicorp/terraform-provider-aws | Go | [`aws_elasticache_serverless_cache` Security Group Ids are incorrectly optional.](https://github.com/hashicorp/terraform-provider-aws/issues/43027) | 7 |
| hashicorp/terraform-provider-aws | Go | [[Bug]: aws_kinesis_firehose_delivery_stream continually applies cloudwatch_logging_options](https://github.com/hashicorp/terraform-provider-aws/issues/40446) | 7 |
| hashicorp/nomad | Go | [retry_join to support digitalocean provider](https://github.com/hashicorp/nomad/issues/18587) | 7 |
| hashicorp/consul | Go | [Metrics missing from documentation](https://github.com/hashicorp/consul/issues/13364) | 7 |
| mattermost/mattermost-plugin-github | Go | [Notification numbers are not properly aligned](https://github.com/mattermost/mattermost-plugin-github/issues/398) | 7 |
| mattermost/mattermost-plugin-github | Go | [In RHS, display whether there are linked pull requests to issues, and if there are linked issues for pull requests](https://github.com/mattermost/mattermost-plugin-github/issues/271) | 7 |
| layer5io/getnighthawk | Go | [[SITE] Nav Bar is missing on the mobile view of the page](https://github.com/layer5io/getnighthawk/issues/258) | 8 |
| kubernetes/autoscaler | Go | [VPA: document behavior for Requests & Limits](https://github.com/kubernetes/autoscaler/issues/7895) | 8 |
| kubernetes/kube-state-metrics | Go | [CustomResourceDefinitions status fields cause spam of errors that cannot be fixed](https://github.com/kubernetes/kube-state-metrics/issues/2482) | 8 |
| kubernetes/kops | Go | [Better output from kops rolling-update cluster command](https://github.com/kubernetes/kops/issues/14122) | 8 |
| hashicorp/nomad | Go | [Support optional object type attributes in Nomad HCL variables](https://github.com/hashicorp/nomad/issues/25317) | 8 |
| hashicorp/vault-k8s | Go | [Configurable default log_level and log_format for injected Vault Agent containers](https://github.com/hashicorp/vault-k8s/issues/417) | 8 |
| hashicorp/nomad | Go | [add  `-json` and `-t` options to inspection related cmds](https://github.com/hashicorp/nomad/issues/15894) | 8 |
| mattermost/mattermost-plugin-mscalendar | Go | [Support different time format preferences for the user](https://github.com/mattermost/mattermost-plugin-mscalendar/issues/358) | 8 |
| kubernetes/sig-security | Go | [tooling: run tests and linters with prow for srctl](https://github.com/kubernetes/sig-security/issues/175) | 9 |
| kubernetes/kube-state-metrics | Go | [Promote experimental metrics](https://github.com/kubernetes/kube-state-metrics/issues/1792) | 9 |
| kubernetes/perf-tests | Go | [Pod startup time phases are inaccurate in longer tests.](https://github.com/kubernetes/perf-tests/issues/2006) | 9 |
| hashicorp/terraform-provider-kubernetes | Go | [Init container doesn't support restart_policy option (to transform it in a sidecar container)](https://github.com/hashicorp/terraform-provider-kubernetes/issues/2446) | 9 |
| hashicorp/nomad | Go | [allow `raw_exec` tasks to drop client environment variables](https://github.com/hashicorp/nomad/issues/17650) | 9 |
| hashicorp/nomad | Go | [Nomad config validate does not check for missing host_volume directories and daemon fails to start](https://github.com/hashicorp/nomad/issues/16968) | 9 |
| kubernetes/minikube | Go | [test: Remove duplicate kubernetes versions in tests](https://github.com/kubernetes/minikube/issues/21483) | 10 |
| kubernetes/kube-state-metrics | Go | [[regression] /metrics port down when not existing CRD are listed in config file](https://github.com/kubernetes/kube-state-metrics/issues/2354) | 10 |
| kubernetes/perf-tests | Go | [clusterloader2 should be covered with unit tests](https://github.com/kubernetes/perf-tests/issues/572) | 10 |
| hashicorp/waypoint | Go | [Improve error message if docker desktop is not running](https://github.com/hashicorp/waypoint/issues/3471) | 10 |
| kubernetes/cloud-provider-openstack | Go | [[cinder-csi-plugin] Allow StorageClass parameters to be set in Helm chart](https://github.com/kubernetes/cloud-provider-openstack/issues/1980) | 11 |
| kubernetes/perf-tests | Go | [Make PV tests work on kubemark clusters](https://github.com/kubernetes/perf-tests/issues/803) | 11 |
| hashicorp/terraform-provider-azurerm | Go | [azurerm_postgresql_flexible_server SKU name validation mismatch between Terraform provider and Azure API](https://github.com/hashicorp/terraform-provider-azurerm/issues/21522) | 11 |
| hashicorp/terraform-provider-aws | Go | [Timeout for every account destroy with `close_on_deletion`](https://github.com/hashicorp/terraform-provider-aws/issues/46284) | 12 |
| kubernetes/kops | Go | [AWS: Cluster requires designating subnets by both ID and containing AZ](https://github.com/kubernetes/kops/issues/14710) | 13 |
| kubernetes/minikube | Go | [minikube should allow 1 cpu --no-kubernetes](https://github.com/kubernetes/minikube/issues/22152) | 14 |
| kubernetes/minikube | Go | [Minikube tunnel is not working on Windows (endessly trying to add a route)](https://github.com/kubernetes/minikube/issues/11645) | 14 |
| kubernetes/minikube | Go | [--host-only-cidr: invalid CIDR address: '192.168.99.1/24'](https://github.com/kubernetes/minikube/issues/7063) | 14 |
| kubernetes/minikube | Go | [registry-creds addon: secrets stored with different name to defaults](https://github.com/kubernetes/minikube/issues/2805) | 14 |
| hashicorp/terraform-provider-helm | Go | [the provider continues to reveal sensitive variables during destroy or update in-place](https://github.com/hashicorp/terraform-provider-helm/issues/1287) | 14 |
| kubernetes/autoscaler | Go | [Add Comprehensive VPA Documentation to Kubernetes Website](https://github.com/kubernetes/autoscaler/issues/8839) | 15 |
| kubernetes/autoscaler | Go | [Cluster autoscaler should remove unused "node-autoprovisioning-enabled" flag and the related metrics](https://github.com/kubernetes/autoscaler/issues/6228) | 15 |
| kubernetes/ingress-nginx | Go | [Support standard Forwarded header](https://github.com/kubernetes/ingress-nginx/issues/10263) | 15 |
| hashicorp/terraform-provider-aws | Go | [[Enhancement]: Support updateToLatestImageVersion in aws_batch_compute_environment.compute_resources](https://github.com/hashicorp/terraform-provider-aws/issues/39978) | 15 |
| hashicorp/terraform-provider-aws | Go | [ Lifecycle configuration for S3 Bucket failing with time out issue for AWS Provider 4.21.0](https://github.com/hashicorp/terraform-provider-aws/issues/25939) | 15 |
| kubernetes/minikube | Go | [add detailed info about what each integration test is doing to the site](https://github.com/kubernetes/minikube/issues/11571) | 16 |
| kubernetes/minikube | Go | [Feature: enable the structured logging for kubernetes components by default](https://github.com/kubernetes/minikube/issues/9268) | 16 |
| kubernetes/ingress-nginx | Go | [Feature Request: Allow disabling custom-http-errors per ingress](https://github.com/kubernetes/ingress-nginx/issues/8384) | 17 |
| kubernetes/autoscaler | Go | [Autoscaler 1.25 or later: If a node fails to be deleted, the lastScaleDownFailTime is not refresh.](https://github.com/kubernetes/autoscaler/issues/6313) | 18 |
| kubernetes/minikube | Go | [improve UI advice when user needs to delete the cluster](https://github.com/kubernetes/minikube/issues/10460) | 18 |
| kubernetes/perf-tests | Go | [ClusterLoader: HA cluster support](https://github.com/kubernetes/perf-tests/issues/246) | 18 |
| kubernetes/kubernetes | Go | [DRA: measure and track performance of "experimental" allocator](https://github.com/kubernetes/kubernetes/issues/135058) | 19 |
| kubernetes/kube-state-metrics | Go | [Address lint reports](https://github.com/kubernetes/kube-state-metrics/issues/1887) | 19 |
| kubernetes/perf-tests | Go | [NodeKiller seems to be not working in 100 node 1.17 / master performance tests](https://github.com/kubernetes/perf-tests/issues/1005) | 19 |
| kubernetes/minikube | Go | [ci: Ensure workflow timeouts - runs can get stuck for hours](https://github.com/kubernetes/minikube/issues/23041) | 20 |
| kubernetes/perf-tests | Go | [Run more linters with golangci-lint](https://github.com/kubernetes/perf-tests/issues/1244) | 20 |
| kubernetes/cloud-provider-openstack | Go | [[occm] - add annotation for custom octavia listener tags](https://github.com/kubernetes/cloud-provider-openstack/issues/2327) | 21 |
| kubernetes/kubernetes | Go | [Give an indication in container events for probe failure as to whether the failure was ignored due to FailureThreshold](https://github.com/kubernetes/kubernetes/issues/115823) | 22 |
| kubernetes/minikube | Go | [get ETCD version from kubernetes constants](https://github.com/kubernetes/minikube/issues/11290) | 22 |
| kubernetes/minikube | Go | [make it obvious in terminal for user if using docker-env](https://github.com/kubernetes/minikube/issues/6489) | 22 |
| kubernetes/minikube | Go | [Document how to run minikube in China](https://github.com/kubernetes/minikube/issues/5020) | 25 |
| kubernetes/kubernetes | Go | [Node lifecycle controller does not `markPodsNotReady` when the node `Ready` state changes from `false` to `unknown`](https://github.com/kubernetes/kubernetes/issues/112733) | 30 |
| kubernetes/ingress-nginx | Go | [Distinguish wait-shutdown command from standard k8s SIGTERM](https://github.com/kubernetes/ingress-nginx/issues/6287) | 32 |
| kubernetes/kubernetes | Go | [add and use alternative APIs which support contextual logging](https://github.com/kubernetes/kubernetes/issues/126379) | 35 |
| kubernetes/kubernetes | Go | [NetworkPolicy tests for blocking north/south traffic](https://github.com/kubernetes/kubernetes/issues/114369) | 35 |
| kubernetes/kubernetes | Go | [kubelet parameter(eviction-max-pod-grace-period ), not work as expected like officical comment.](https://github.com/kubernetes/kubernetes/issues/118172) | 37 |
| kubernetes/kubernetes | Go | [Write the stress test for gRPC, http, and tcp probes](https://github.com/kubernetes/kubernetes/issues/115782) | 37 |
| kubernetes/perf-tests | Go | [Create api-availability measurement](https://github.com/kubernetes/perf-tests/issues/1096) | 38 |
| kubernetes/kube-state-metrics | Go | [Missing replacement config for VPA collector in CRM](https://github.com/kubernetes/kube-state-metrics/issues/2041) | 41 |
| kubernetes/kubernetes | Go | [Reuse the http request object for http probes](https://github.com/kubernetes/kubernetes/issues/115939) | 43 |
| kubernetes/kubernetes | Go | [tracker: improve the kubelet test coverage](https://github.com/kubernetes/kubernetes/issues/109717) | 49 |
| kubernetes/minikube | Go | [add documentation for WSL2](https://github.com/kubernetes/minikube/issues/7879) | 53 |
| kubernetes/kubernetes | Go | [Migrate DRA components to support granular authorization on status updates](https://github.com/kubernetes/kubernetes/issues/138149) | 63 |
| microsoft/edge-ai | HCL | [docs(testing): add regression test tracking policy](https://github.com/microsoft/edge-ai/issues/176) | 0 |
| microsoft/edge-ai | HCL | [chore(python): add pip lock files for reproducible builds](https://github.com/microsoft/edge-ai/issues/167) | 0 |
| microsoft/edge-ai | HCL | [docs(testing): update testing-validation.md to reflect actual test frameworks](https://github.com/microsoft/edge-ai/issues/144) | 1 |
| microsoft/edge-ai | HCL | [docs(changelog): add CHANGELOG.md generation](https://github.com/microsoft/edge-ai/issues/143) | 1 |
| microsoft/edge-ai | HCL | [chore(rust): standardize strip = true across all Rust crates](https://github.com/microsoft/edge-ai/issues/177) | 2 |
| kubernetes/k8s.io | HCL | [[Umbrella Issue] Migrate CNCF Ecosystem projects from k8s.gcr.io to registry.k8s.io](https://github.com/kubernetes/k8s.io/issues/4780) | 37 |
| cncf/glossary | HTML | [[es] A report to track and reflect updates of English content](https://github.com/cncf/glossary/issues/3222) | 0 |
| cncf/tag-app-delivery | HTML | [Document how we use GitHub labels](https://github.com/cncf/tag-app-delivery/issues/405) | 0 |
| cncf/tag-contributor-strategy | HTML | [Charter link is 404](https://github.com/cncf/tag-contributor-strategy/issues/762) | 1 |
| cncf/glossary | HTML | [[ru] Localize `Portability`](https://github.com/cncf/glossary/issues/3265) | 1 |
| kubernetes/website | HTML | [Certificates page renders %!s(<nil>) instead of ClusterTrustBundle API reference link](https://github.com/kubernetes/website/issues/56092) | 2 |
| cncf/glossary | HTML | [[ru] Localize `Service` into Russian](https://github.com/cncf/glossary/issues/3334) | 2 |
| cncf/tag-app-delivery | HTML | [Automation of tag-app-delivery repo](https://github.com/cncf/tag-app-delivery/issues/566) | 3 |
| cncf/tag-security | HTML | [[Suggestion] Working Group Landing Page](https://github.com/cncf/tag-security/issues/1354) | 4 |
| kubernetes/website | HTML | [[hi] Localize Network Policy Provider page](https://github.com/kubernetes/website/issues/47439) | 7 |
| cncf/tag-observability | HTML | [WG: Create GitHub Pages site for TAG Observability](https://github.com/cncf/tag-observability/issues/39) | 7 |
| kubernetes/website | HTML | [[hi] Localize concepts/scheduling-eviction page ](https://github.com/kubernetes/website/issues/48989) | 8 |
| kubernetes/website | HTML | [[hi] Localize concepts/extend-kubernetes page](https://github.com/kubernetes/website/issues/48991) | 9 |
| kubernetes/website | HTML | [[hi] Localize /concepts/cluster-administration page](https://github.com/kubernetes/website/issues/48990) | 9 |
| kubernetes/website | HTML | [[hi] Localize concepts/Security page](https://github.com/kubernetes/website/issues/47463) | 9 |
| kubernetes/website | HTML | [[hi] Localize concepts/Storage page](https://github.com/kubernetes/website/issues/47462) | 9 |
| kubernetes/website | HTML | [[hi] Localize concepts/Workloads page ](https://github.com/kubernetes/website/issues/47442) | 11 |
| kubernetes/website | HTML | [[hi] Localize tasks/configure-pod-container page ](https://github.com/kubernetes/website/issues/48992) | 14 |
| kubernetes/website | HTML | [[hi] Localize en/docs/contribute/style/page-content-types.md](https://github.com/kubernetes/website/issues/36594) | 18 |
| kubernetes/website | HTML | [Add Etcd Version Skew to Kubernetes Docs](https://github.com/kubernetes/website/issues/53355) | 19 |
| kubernetes/website | HTML | [[hi] Localize en/docs/contribute/participate/_index.md](https://github.com/kubernetes/website/issues/36471) | 19 |
| kubernetes/website | HTML | [[de] Localize content/de/setup/production-environment/_index.md](https://github.com/kubernetes/website/issues/50286) | 23 |
| kubernetes/website | HTML | [[hi] Localize /en/docs/reference/glossary/admission-controller.md](https://github.com/kubernetes/website/issues/35935) | 25 |
| kubernetes/website | HTML | [[hi] Localize en/docs/contribute/review/for-approvers.md](https://github.com/kubernetes/website/issues/36474) | 26 |
| kubernetes/website | HTML | [[hi] Enhance README file to improve readability and user-friendliness](https://github.com/kubernetes/website/issues/41989) | 30 |
| microsoft/copilot-for-eclipse | Java | [The Copilot Chat view retains file context even after the file is closed](https://github.com/microsoft/copilot-for-eclipse/issues/277) | 0 |
| microsoft/copilot-for-eclipse | Java | [Detailed model information on dropdown hover is cropped on Linux](https://github.com/microsoft/copilot-for-eclipse/issues/113) | 2 |
| microsoft/copilot-for-eclipse | Java | [Please integrate copilot into eclipse quickfix feature - Enhancement Request](https://github.com/microsoft/copilot-for-eclipse/issues/70) | 3 |
| microsoft/copilot-for-eclipse | Java | [Unable to use the Java source file corresponding to the class file as context](https://github.com/microsoft/copilot-for-eclipse/issues/117) | 6 |
| mattermost/mattermost-plugin-gitlab | JavaScript | [Convert link_tooltip component to typescript](https://github.com/mattermost/mattermost-plugin-gitlab/issues/424) | 1 |
| freeCodeCamp/classroom | JavaScript | [Bug: Classrooms can be created with no certifications](https://github.com/freeCodeCamp/classroom/issues/551) | 1 |
| layer5io/docs | JavaScript | [[Docs] Add missing actions to comment history panel](https://github.com/layer5io/docs/issues/549) | 2 |
| huggingface/transformers.js | JavaScript | [Is 'aggregation_strategy' parameter available for token classification pipeline?](https://github.com/huggingface/transformers.js/issues/633) | 2 |
| huggingface/transformers.js | JavaScript | [[Feature request] Return offset mapping using tokenizer](https://github.com/huggingface/transformers.js/issues/425) | 2 |
| EddieHubCommunity/RepoRater | JavaScript | [[BUG] Update the preview in the readme](https://github.com/EddieHubCommunity/RepoRater/issues/152) | 2 |
| freeCodeCamp/classroom | JavaScript | [Bug: /classes page crashes if the mock-fcc-data endpoint is not running](https://github.com/freeCodeCamp/classroom/issues/533) | 2 |
| layer5io/docs | JavaScript | [[Docs] Convert Static Image to Meshery Design - 4](https://github.com/layer5io/docs/issues/794) | 3 |
| layer5io/docs | JavaScript | [Screen capture includes Grammarly](https://github.com/layer5io/docs/issues/543) | 3 |
| freeCodeCamp/100DaysOfCode-twitter-bot | JavaScript | [Contributing needs work](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/issues/112) | 4 |
| layer5io/docs | JavaScript | [[Docs] Improve Related Docs Links in Pinning Models to Dock Page](https://github.com/layer5io/docs/issues/1028) | 5 |
| layer5io/docs | JavaScript | [[Docs] Convert Static Image to Meshery Design - 3](https://github.com/layer5io/docs/issues/793) | 5 |
| layer5io/layer5 | JavaScript | [[Screenshots] Citrix Service Mesh under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4880) | 5 |
| freeCodeCamp/100DaysOfCode-twitter-bot | JavaScript | [Welcome bot! Respond to the user when committing to 100DaysOfCode](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/issues/96) | 5 |
| layer5io/docs | JavaScript | [Convert Images into Meshery Design.](https://github.com/layer5io/docs/issues/646) | 6 |
| layer5io/layer5 | JavaScript | [[CI] Create or add to existing workflow: a broken link checker](https://github.com/layer5io/layer5/issues/6407) | 6 |
| layer5io/layer5 | JavaScript | [Relocate partner logos to appropriate directory in static folder.](https://github.com/layer5io/layer5/issues/7256) | 7 |
| layer5io/layer5 | JavaScript | [[Screenshots] Chaos Mesh under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4867) | 7 |
| huggingface/transformers.js | JavaScript | [[Doc request] Add an example guide of how to use it in Svelte (and deploy to HF Spaces)](https://github.com/huggingface/transformers.js/issues/171) | 7 |
| EddieHubCommunity/EddieHubCommunity.github.io | JavaScript | [Add Issue Templates](https://github.com/EddieHubCommunity/EddieHubCommunity.github.io/issues/211) | 7 |
| layer5io/layer5 | JavaScript | [Mobile navigation menu contains invalid nesting](https://github.com/layer5io/layer5/issues/7484) | 8 |
| layer5io/layer5 | JavaScript | [[Screenshots] Fluentbit Operator under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/5333) | 8 |
| layer5io/layer5 | JavaScript | [[Screenshots] Flagger under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/5331) | 8 |
| EddieHubCommunity/HealthCheck | JavaScript | [Update the preview image in the site](https://github.com/EddieHubCommunity/HealthCheck/issues/151) | 8 |
| decentraland/land | JavaScript | [docs needed](https://github.com/decentraland/land/issues/154) | 8 |
| freeCodeCamp/100DaysOfCode-twitter-bot | JavaScript | [Update docs to the KCD README pattern](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/issues/131) | 9 |
| layer5io/layer5 | JavaScript | [Improve styling of categories of models](https://github.com/layer5io/layer5/issues/7593) | 10 |
| layer5io/layer5 | JavaScript | [[Screenshots] Containerssh under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4876) | 10 |
| layer5io/layer5 | JavaScript | [[Screenshots] Cert Manager Crds under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4865) | 10 |
| layer5io/layer5 | JavaScript | [[Animation] Animate Meshery Architecture](https://github.com/layer5io/layer5/issues/7661) | 11 |
| layer5io/layer5 | JavaScript | [[Screenshots] AWS Elastic Kubernetes Service under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/5322) | 11 |
| layer5io/layer5 | JavaScript | [Update the structure of pages based on the latest sitemap revision available in Figma](https://github.com/layer5io/layer5/issues/5359) | 13 |
| layer5io/layer5 | JavaScript | [[Screenshots] Cloudevents under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4869) | 13 |
| layer5io/layer5 | JavaScript | [[Screenshots] Cilium under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4868) | 13 |
| mattermost/mattermost-plugin-gitlab | JavaScript | [Support config variable to disable project access check for incoming webhook event](https://github.com/mattermost/mattermost-plugin-gitlab/issues/463) | 13 |
| layer5io/layer5 | JavaScript | [Update resources and hands-on labs with latest content](https://github.com/layer5io/layer5/issues/6387) | 14 |
| layer5io/layer5 | JavaScript | [[Screenshots] Fabedge under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/5330) | 14 |
| EddieHubCommunity/BioDrop | JavaScript | [[BUG] Duplicate sortable package present](https://github.com/EddieHubCommunity/BioDrop/issues/10139) | 14 |
| layer5io/layer5 | JavaScript | [Pricing: subscription plans as a sticky row](https://github.com/layer5io/layer5/issues/7665) | 15 |
| layer5io/layer5 | JavaScript | [[SEO] First Contentful Paint (FCP): gatsby-plugin-webpack-bundle-analyser-v2](https://github.com/layer5io/layer5/issues/6449) | 17 |
| layer5io/layer5 | JavaScript | [[Visual Design] New Recognition Badge: Event Evangelist Badge](https://github.com/layer5io/layer5/issues/4809) | 17 |
| layer5io/layer5-academy | JavaScript | [[Docs] Convert meshery design image to embedded meshery design](https://github.com/layer5io/layer5-academy/issues/32) | 18 |
| layer5io/layer5 | JavaScript | [[Learn] Learning Paths need enhanced with Meshery/MeshMap walk-throughs](https://github.com/layer5io/layer5/issues/4899) | 18 |
| layer5io/layer5 | JavaScript | [add animated card](https://github.com/layer5io/layer5/issues/6521) | 20 |
| layer5io/layer5 | JavaScript | [The text and layout need to be adjusted for better readability and usability across different screen sizes.](https://github.com/layer5io/layer5/issues/5640) | 31 |
| layer5io/layer5 | JavaScript | [[Screenshots] Devstream under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4887) | 31 |
| layer5io/layer5 | JavaScript | [[Screenshots] Container Network Interface (CNI) under 'How it Works See It in Action' section](https://github.com/layer5io/layer5/issues/4874) | 31 |
| layer5io/layer5 | JavaScript | [[Screenshots] Old Screenshots of Meshery Playground needs to be updated](https://github.com/layer5io/layer5/issues/5342) | 35 |
| layer5io/layer5 | JavaScript | [[UX] Visual Design needed for incorporation of Writing Program into Internship Programs page](https://github.com/layer5io/layer5/issues/4918) | 39 |
| cncf/landscape-graph | Jupyter Notebook | [Create full-text indices (Lucene) for relationships' properties](https://github.com/cncf/landscape-graph/issues/20) | 0 |
| cncf/landscape-graph | Jupyter Notebook | [Docs: list jetbrains graph db plugin in dev setup](https://github.com/cncf/landscape-graph/issues/82) | 1 |
| cncf/landscape-graph | Jupyter Notebook | [Spike: Visualization Tools & Libraries](https://github.com/cncf/landscape-graph/issues/72) | 1 |
| cncf/landscape-graph | Jupyter Notebook | [create apps/landscape-introspector (introspector docs, example)](https://github.com/cncf/landscape-graph/issues/51) | 1 |
| cncf/landscape-graph | Jupyter Notebook | [Create gource visualizations for all cncf project related repos](https://github.com/cncf/landscape-graph/issues/21) | 1 |
| huggingface/optimum-intel | Jupyter Notebook | [Fix conversion of ltx_video models in bf16 format](https://github.com/huggingface/optimum-intel/issues/1614) | 2 |
| cncf/landscape-graph | Jupyter Notebook | [Automatically generate GH Issue Labels for all Sub-Graph Modules](https://github.com/cncf/landscape-graph/issues/84) | 2 |
| microsoft/presidio-research | Jupyter Notebook | [Enforce locale for fake entities](https://github.com/microsoft/presidio-research/issues/123) | 3 |
| huggingface/optimum-intel | Jupyter Notebook | [Add tests which check, that required transformations are applied](https://github.com/huggingface/optimum-intel/issues/1645) | 4 |
| cncf/landscape-graph | Jupyter Notebook | [Implement autogenerated mocks for GraphQL API from schema](https://github.com/cncf/landscape-graph/issues/103) | 4 |
| cncf/landscape-graph | Jupyter Notebook | [Create documentation site (GitHub Pages or Netlify) using Docusaurus](https://github.com/cncf/landscape-graph/issues/97) | 7 |
| huggingface/huggingface-gemma-recipes | Jupyter Notebook | [📣 Call for contributions!](https://github.com/huggingface/huggingface-gemma-recipes/issues/4) | 11 |
| huggingface/huggingface-llama-recipes | Jupyter Notebook | [Call for contributions](https://github.com/huggingface/huggingface-llama-recipes/issues/43) | 20 |
| huggingface/agents-course | MDX | [Improve diagrams in unit 2.1](https://github.com/huggingface/agents-course/issues/233) | 6 |
| layer5io/.github | Makefile | [Add the Sistent project to this readme.md](https://github.com/layer5io/.github/issues/54) | 1 |
| layer5io/academy-example | Makefile | [[Docs] deprecated: .Site.AllPages](https://github.com/layer5io/academy-example/issues/108) | 1 |
| layer5io/academy-build | Makefile | [Replace generic favicon with Layer5 logo](https://github.com/layer5io/academy-build/issues/2) | 3 |
| huggingface/awesome-huggingface | Other | [[hacktoberfest] Hugging Face Collections Hacktoberfest challenge](https://github.com/huggingface/awesome-huggingface/issues/28) | 0 |
| decentraland/dapps-issues | Other | [[Events] Update the Share link to use the new `jump-in` site.](https://github.com/decentraland/dapps-issues/issues/247) | 0 |
| decentraland/dapps-issues | Other | [Add a banner to communicate possible downtimes of our/thirdparty services](https://github.com/decentraland/dapps-issues/issues/20) | 0 |
| decentraland/sdk | Other | [Remove the mandatory `?v=` from the renderer fetch](https://github.com/decentraland/sdk/issues/201) | 1 |
| godotengine/godot-asset-library | PHP | [Categories need a description (tooltip?) when hovered/selected](https://github.com/godotengine/godot-asset-library/issues/74) | 1 |
| godotengine/godot-asset-library | PHP | [keep the content of the submition form when its not validated, or try some ajax realtime pre-validation](https://github.com/godotengine/godot-asset-library/issues/61) | 1 |
| godotengine/godot-asset-library | PHP | [A way to cancel edit requests](https://github.com/godotengine/godot-asset-library/issues/149) | 3 |
| godotengine/godot-asset-library | PHP | [Sanitize inputs for Asset data/fields, like URLs](https://github.com/godotengine/godot-asset-library/issues/204) | 5 |
| microsoft/hve-core | PowerShell | [Standardize maturity field across all collection YAML manifests](https://github.com/microsoft/hve-core/issues/1319) | 0 |
| huggingface/optimum-executorch | Python | [Add benchmarking numbers for more models](https://github.com/huggingface/optimum-executorch/issues/131) | 0 |
| huggingface/lighteval | Python | [[BUG]  Optimize tokenization](https://github.com/huggingface/lighteval/issues/732) | 0 |
| huggingface/lighteval | Python | [[FT]  Add tests for `VLLMModel` base methods](https://github.com/huggingface/lighteval/issues/724) | 0 |
| huggingface/nanotron | Python | [[Feature] Use CUDA event for measuring elasped time](https://github.com/huggingface/nanotron/issues/88) | 0 |
| huggingface/nanotron | Python | [[Feature] Refactor `ParallelContext.world_rank_matrix`](https://github.com/huggingface/nanotron/issues/77) | 0 |
| microsoft/winml-cli | Python | [Minor refactor: reuse _compute_case_signature to compute failed model file name](https://github.com/microsoft/winml-cli/issues/56) | 0 |
| microsoft/physical-ai-toolchain | Python | [chore(ci): remove JaCoCo parser config from codecov.yml](https://github.com/microsoft/physical-ai-toolchain/issues/140) | 0 |
| huggingface/lighteval | Python | [[EVAL] Add kyrgyzLLM benchmark](https://github.com/huggingface/lighteval/issues/1036) | 1 |
| huggingface/lerobot | Python | [Ensure the teleoperators module passes MyPy type checks](https://github.com/huggingface/lerobot/issues/1726) | 1 |
| huggingface/lighteval | Python | [[FT] Build in a way to specify specific IDs/Lines in Dataset to use as few-shot examples in the same split](https://github.com/huggingface/lighteval/issues/634) | 1 |
| huggingface/lighteval | Python | [[FT] LiteLLM concurrency parameters hard-coded](https://github.com/huggingface/lighteval/issues/567) | 1 |
| huggingface/diffusers | Python | [Do we have any script covert from hf format to orginal format?](https://github.com/huggingface/diffusers/issues/10076) | 1 |
| huggingface/nanotron | Python | [Add Debug utility to be able to preview first samples used for training](https://github.com/huggingface/nanotron/issues/184) | 1 |
| huggingface/nanotron | Python | [We don't save checkpoint after training ends](https://github.com/huggingface/nanotron/issues/163) | 1 |
| huggingface/nanotron | Python | [FEAT: Support 1.58-bit LLMs training](https://github.com/huggingface/nanotron/issues/114) | 1 |
| huggingface/dataset-viewer | Python | [Use `revision_exists` (hfh)](https://github.com/huggingface/dataset-viewer/issues/2562) | 1 |
| huggingface/nanotron | Python | [[Feature Request] Add simple communications benchmarks to the repo](https://github.com/huggingface/nanotron/issues/43) | 1 |
| microsoft/winml-cli | Python | [Add test cases for sysinfo/](https://github.com/microsoft/winml-cli/issues/54) | 1 |
| microsoft/physical-ai-toolchain | Python | [docs(ci): document GHSA allowlist in dependency-review.yml](https://github.com/microsoft/physical-ai-toolchain/issues/142) | 1 |
| microsoft/physical-ai-toolchain | Python | [fix(scripts): remove unused instance_type variable in submit-azureml-lerobot-inference.sh](https://github.com/microsoft/physical-ai-toolchain/issues/137) | 1 |
| microsoft/onnxscript | Python | [[Optimizer] Fold Shape -> {Slice, Gather} -> Concat -> Reshape](https://github.com/microsoft/onnxscript/issues/2736) | 1 |
| microsoft/onnxscript | Python | [[torchlib] Add op test to torch.unique_consecutive](https://github.com/microsoft/onnxscript/issues/2695) | 1 |
| microsoft/onnxscript | Python | [Constant-Folding Registry](https://github.com/microsoft/onnxscript/issues/2507) | 1 |
| microsoft/presidio | Python | [More elaborate description how to build custom Docker images for Presidio](https://github.com/microsoft/presidio/issues/1663) | 1 |
| huggingface/lerobot | Python | [Question regarding downsampling and resizing dataset](https://github.com/huggingface/lerobot/issues/2124) | 2 |
| huggingface/lighteval | Python | [[FT] Manage script and language in the Language enum](https://github.com/huggingface/lighteval/issues/745) | 2 |
| huggingface/lighteval | Python | [Call for contributions: Translate lighteval's doc into Chinese](https://github.com/huggingface/lighteval/issues/716) | 2 |
| huggingface/dataset-viewer | Python | [use the `ROW_IDX_COLUMN` constant name instead of copying the value everywhere](https://github.com/huggingface/dataset-viewer/issues/2798) | 2 |
| huggingface/nanotron | Python | [[Feature] Asyncronous Serialization](https://github.com/huggingface/nanotron/issues/87) | 2 |
| huggingface/dataset-viewer | Python | [Use "Sign-In with HF" instead of token in admin-UI](https://github.com/huggingface/dataset-viewer/issues/2373) | 2 |
| huggingface/nanotron | Python | [[Feature Request] Support Data Streaming for faster training of large models](https://github.com/huggingface/nanotron/issues/45) | 2 |
| microsoft/winml-cli | Python | [bug: winml build shows misleading ValueError (opset domain) when disk is full during quantize step](https://github.com/microsoft/winml-cli/issues/259) | 2 |
| microsoft/winml-cli | Python | [winml perf --op-tracing: ANSI color codes garbled on Windows cp1252 terminal](https://github.com/microsoft/winml-cli/issues/218) | 2 |
| microsoft/physical-ai-toolchain | Python | [chore(scripts): remove redundant shellcheck disable directives](https://github.com/microsoft/physical-ai-toolchain/issues/138) | 2 |
| microsoft/onnxscript | Python | [Missing converter for OpOverload(op='aten._grouped_mm', overload='default')](https://github.com/microsoft/onnxscript/issues/2795) | 2 |
| microsoft/OpenAIWorkshop | Python | [Fix eslint warnings](https://github.com/microsoft/OpenAIWorkshop/issues/292) | 2 |
| microsoft/onnxscript | Python | [[torchlib] slice_scatter does not support start and end to be None](https://github.com/microsoft/onnxscript/issues/2372) | 2 |
| microsoft/vscode-black-formatter | Python | [black is using cached pyproject.toml instead of the actual one](https://github.com/microsoft/vscode-black-formatter/issues/569) | 2 |
| huggingface/diffusers | Python | [[Anima] Add img2img capability](https://github.com/huggingface/diffusers/issues/13903) | 3 |
| huggingface/lerobot | Python | [Finetune smolvla with vision encoder](https://github.com/huggingface/lerobot/issues/1774) | 3 |
| huggingface/lighteval | Python | [[FT] showing count in Markdown summary table](https://github.com/huggingface/lighteval/issues/804) | 3 |
| huggingface/lighteval | Python | [[FT]  Add tests for nanotron](https://github.com/huggingface/lighteval/issues/765) | 3 |
| huggingface/lighteval | Python | [[EVAL] Big-Bench Extra Hard (BBEH)](https://github.com/huggingface/lighteval/issues/600) | 3 |
| huggingface/optimum-habana | Python | [Add support for max_length in run_generation](https://github.com/huggingface/optimum-habana/issues/472) | 3 |
| huggingface/dataset-viewer | Python | [Use `CONSTANT_LIST.copy` in list config fieds](https://github.com/huggingface/dataset-viewer/issues/1522) | 3 |
| huggingface/optimum | Python | [Add all available ONNX models to ORTConfigManager](https://github.com/huggingface/optimum/issues/351) | 3 |
| huggingface/transfer-learning-conv-ai | Python | [RuntimeError: shape '[-1, 2, 34]' is invalid for input of size 61710](https://github.com/huggingface/transfer-learning-conv-ai/issues/12) | 3 |
| godotengine/godot-blender-exporter | Python | [Blender object with negative scale](https://github.com/godotengine/godot-blender-exporter/issues/24) | 3 |
| huggingface/lerobot | Python | [How can I change the task name of already recorded episodes?](https://github.com/huggingface/lerobot/issues/2096) | 4 |
| huggingface/lerobot | Python | [Ensure the utilities module passes MyPy type checks](https://github.com/huggingface/lerobot/issues/1727) | 4 |
| huggingface/lighteval | Python | [[EVAL]: Add more African Benchmarks](https://github.com/huggingface/lighteval/issues/373) | 4 |
| huggingface/accelerate | Python | [[Community Contributions] examples on distributed inference using 🤗 Accelerate](https://github.com/huggingface/accelerate/issues/3078) | 4 |
| huggingface/dataset-viewer | Python | [Cache/Queue metrics should not be negative](https://github.com/huggingface/dataset-viewer/issues/2495) | 4 |
| microsoft/onnxscript | Python | [Constant Folding removes 'axes' initializer form Squeeze layer, resulting in incorrect ONNX model](https://github.com/microsoft/onnxscript/issues/2810) | 4 |
| huggingface/lighteval | Python | [[BUG] custom model docs don't run: missing imports](https://github.com/huggingface/lighteval/issues/760) | 5 |
| huggingface/nanotron | Python | [Avoid nested `InheritFromOtherOptimizer`](https://github.com/huggingface/nanotron/issues/267) | 5 |
| huggingface/nanotron | Python | [[Bug] Missing `_is_using_mup` when resume checkpoint](https://github.com/huggingface/nanotron/issues/198) | 5 |
| huggingface/nanotron | Python | [[Unit Test] Add unit tests for DistributedTrainer](https://github.com/huggingface/nanotron/issues/90) | 5 |
| huggingface/lighteval | Python | [Append revision to filepath in `--output_dir`?](https://github.com/huggingface/lighteval/issues/56) | 5 |
| huggingface/optimum-benchmark | Python | [Evaluators for specific tasks](https://github.com/huggingface/optimum-benchmark/issues/34) | 5 |
| huggingface/lighteval | Python | [[FT] Improve Documentation and Examples](https://github.com/huggingface/lighteval/issues/682) | 6 |
| huggingface/lighteval | Python | [[EVAL] Long Horizon Execution](https://github.com/huggingface/lighteval/issues/1056) | 7 |
| microsoft/onnxscript | Python | [Attention fusion (SDPA/MHA) broken for BART decoder with/wo past🐛](https://github.com/microsoft/onnxscript/issues/2424) | 7 |
| microsoft/autogen | Python | [Get current message thread from a group chat team.](https://github.com/microsoft/autogen/issues/6085) | 7 |
| huggingface/lerobot | Python | [Select the VLM backbone for SmolVLA](https://github.com/huggingface/lerobot/issues/2104) | 8 |
| huggingface/lighteval | Python | [[EVAL] Adding PHARE](https://github.com/huggingface/lighteval/issues/696) | 8 |
| huggingface/diffusers | Python | [Make `FlaxLMSDiscreteScheduler` jittable](https://github.com/huggingface/diffusers/issues/2180) | 8 |
| microsoft/presidio | Python | [Can multiple GLiNERRecognizer instances be configured via YAML?](https://github.com/microsoft/presidio/issues/1760) | 8 |
| microsoft/autogen | Python | [open needs encoding='utf-8' for non-english environment, error in playwright_controller.py](https://github.com/microsoft/autogen/issues/5566) | 8 |
| huggingface/diffusers | Python | [Support multiple control nets in the `StableDiffusionControlNetXSPipeline`/`StableDiffusionXLControlNetXSPipeline`](https://github.com/huggingface/diffusers/issues/8434) | 9 |
| huggingface/lerobot | Python | [Distributed v2.1 -> v3.0 conversion](https://github.com/huggingface/lerobot/issues/1998) | 10 |
| huggingface/lighteval | Python | [[EVAL] Add TUMLU benchmark](https://github.com/huggingface/lighteval/issues/577) | 10 |
| huggingface/datasets | Python | [WMT21 & WMT22](https://github.com/huggingface/datasets/issues/4709) | 10 |
| microsoft/onnxscript | Python | [[torchlib] Inefficient implementations](https://github.com/microsoft/onnxscript/issues/2489) | 10 |
| huggingface/diffusers | Python | [[Flux ControlNet] Add support for de-distilled models with CFG](https://github.com/huggingface/diffusers/issues/9635) | 11 |
| huggingface/diffusers | Python | [[Pipeline] AnimateDiff + SparseControl + ControlNet](https://github.com/huggingface/diffusers/issues/9329) | 14 |
| huggingface/lerobot | Python | [Make policies compatible with torch.compile](https://github.com/huggingface/lerobot/issues/2061) | 18 |
| huggingface/huggingface_hub | Python | [[Community event] Translate documentation to your own langage](https://github.com/huggingface/huggingface_hub/issues/1700) | 18 |
| huggingface/datasets | Python | [Consider using "Sequence" instead of "List"](https://github.com/huggingface/datasets/issues/5354) | 18 |
| huggingface/datasets | Python | [Return the name of the currently loaded file in the load_dataset function.](https://github.com/huggingface/datasets/issues/5806) | 19 |
| huggingface/diffusers | Python | [Expanded init fields in StableDiffusionPipeline cause incompatibilities with many/most inherited pipelines](https://github.com/huggingface/diffusers/issues/6969) | 22 |
| huggingface/optimum | Python | [Community contribution - `BetterTransformer` integration for more models!](https://github.com/huggingface/optimum/issues/488) | 26 |
| huggingface/peft | Python | [Comparison of Different Fine-Tuning Techniques for Conversational AI](https://github.com/huggingface/peft/issues/2310) | 76 |
| huggingface/ratchet | Rust | [Reduce dependencies! 🗡️](https://github.com/huggingface/ratchet/issues/170) | 0 |
| microsoft/openvmm | Rust | [remove usages of futures::select! in the repo with futures_concurrency](https://github.com/microsoft/openvmm/issues/1246) | 0 |
| microsoft/windows-drivers-rs | Rust | [Migrate from fs4 to std::File flocks](https://github.com/microsoft/windows-drivers-rs/issues/300) | 0 |
| microsoft/openvmm | Rust | [fdt/builder: enforce BE datatypes on add_prop_array](https://github.com/microsoft/openvmm/issues/777) | 0 |
| decentraland/godot-explorer | Rust | [[Bug]: Interaction Feedback Doesn't Trigger when holding one Control (E.g Joystick)](https://github.com/decentraland/godot-explorer/issues/1170) | 0 |
| microsoft/openvmm | Rust | [BaseChipsetBuilder should accept VmChipsetResult directly instead of piecemeal fields](https://github.com/microsoft/openvmm/issues/3463) | 1 |
| microsoft/webui | Rust | [contact book example: Make search great](https://github.com/microsoft/webui/issues/191) | 1 |
| microsoft/openvmm | Rust | [repo: move no_std custom error types over to thiserror](https://github.com/microsoft/openvmm/issues/1811) | 1 |
| microsoft/openvmm | Rust | [Clean up our windows API dependencies](https://github.com/microsoft/openvmm/issues/1061) | 1 |
| microsoft/openvmm | Rust | [openvmm: emulated nvme configuration](https://github.com/microsoft/openvmm/issues/1534) | 2 |
| microsoft/windows-drivers-rs | Rust | [HID hidport.h headers missing for UMDF build](https://github.com/microsoft/windows-drivers-rs/issues/355) | 3 |
| godotengine/discourse-theme | SCSS | [Change default `green` to our own green for the Solved questions](https://github.com/godotengine/discourse-theme/issues/14) | 0 |
| godotengine/discourse-theme | SCSS | [Make tag and tag count more distinct](https://github.com/godotengine/discourse-theme/issues/11) | 0 |
| godotengine/discourse-theme | SCSS | [Categories are not rounded on mobile](https://github.com/godotengine/discourse-theme/issues/3) | 0 |
| godotengine/discourse-theme | SCSS | [Search bar should not cover full width on mobile](https://github.com/godotengine/discourse-theme/issues/2) | 0 |
| godotengine/discourse-theme | SCSS | [Remove the "Sign Up" button from navbar](https://github.com/godotengine/discourse-theme/issues/15) | 2 |
| mattermost/mattermost-gitpod-config | Shell | [If a the workspace repo doesn't define `.gitpod/*.sh` files, we shouldn't try to run them](https://github.com/mattermost/mattermost-gitpod-config/issues/50) | 0 |
| mattermost/mattermost-gitpod-config | Shell | [Improve development flow of opening the Mattermost webapp automatically](https://github.com/mattermost/mattermost-gitpod-config/issues/49) | 0 |
| layer5io/exoscale-academy | Shell | [Convert Images into Meshery Design [ Kubernetes Workshop]](https://github.com/layer5io/exoscale-academy/issues/45) | 4 |
| layer5io/trigger-remote-provider-action | Shell | [to fix error in "Slack Notify on Star" Job under GitHub Actions ](https://github.com/layer5io/trigger-remote-provider-action/issues/12) | 4 |
| layer5io/exoscale-academy | Shell | [Kubernetes Workshop Image-8](https://github.com/layer5io/exoscale-academy/issues/53) | 9 |
| hashicorp/waypoint-helm | Smarty | [An ability to define Tolerations for Server and Runner StatefulSets](https://github.com/hashicorp/waypoint-helm/issues/42) | 1 |
| huggingface/sam2-studio | Swift | [Model download selector](https://github.com/huggingface/sam2-studio/issues/28) | 1 |
| huggingface/chat-macOS | Swift | [[Feature Request] System Prompt Support](https://github.com/huggingface/chat-macOS/issues/35) | 2 |
| huggingface/chat-macOS | Swift | [Asking "what time is it?" will always return the local time of Paris, regardless of your location (⌘R+)](https://github.com/huggingface/chat-macOS/issues/7) | 2 |
| huggingface/chat-macOS | Swift | [Add custom LLM API ](https://github.com/huggingface/chat-macOS/issues/18) | 5 |
| huggingface/sam2-studio | Swift | [Video support estimated release date?](https://github.com/huggingface/sam2-studio/issues/25) | 26 |
| microsoft/Power-CAT-Copilot-Studio-Kit | TypeScript | [Bug: Conversation KPIs dashboard is blank even though all the related flows are enabled and prerequisites are met](https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/issues/746) | 0 |
| microsoft/compose-language-service | TypeScript | [Hover link on `image:` field in compose.yaml always points to Docker Hub, even for private registries](https://github.com/microsoft/compose-language-service/issues/179) | 0 |
| microsoft/vscode-containers | TypeScript | ["Compose Logs" command in extension settings](https://github.com/microsoft/vscode-containers/issues/323) | 0 |
| microsoft/Agent365-nodejs | TypeScript | [Convert "test-agents" into E2E tests](https://github.com/microsoft/Agent365-nodejs/issues/15) | 0 |
| microsoft/vscode-jupyter | TypeScript | [Add magic line comments regex pattern as configuration for uncommentMagicCommands](https://github.com/microsoft/vscode-jupyter/issues/16499) | 0 |
| microsoft/Game-Control-Puzzle-Event-Administration-Tools | TypeScript | [Per team and per puzzle activity feeds](https://github.com/microsoft/Game-Control-Puzzle-Event-Administration-Tools/issues/81) | 0 |
| mattermost/mattermost-test-management | TypeScript | [feat: add validation to custom field's "Location"](https://github.com/mattermost/mattermost-test-management/issues/25) | 0 |
| decentraland/creator-hub | TypeScript | [Name tooltip too high when searching](https://github.com/decentraland/creator-hub/issues/1010) | 0 |
| decentraland/auth | TypeScript | [Migrate getAnalytics to useAnalytics Hook](https://github.com/decentraland/auth/issues/198) | 0 |
| decentraland/ui2 | TypeScript | [Change JumpIn component behavior](https://github.com/decentraland/ui2/issues/284) | 0 |
| decentraland/catalyst-client | TypeScript | [Add missing endpoints to Lambdas Client (review the other clients) to keep it up to date](https://github.com/decentraland/catalyst-client/issues/479) | 0 |
| decentraland/creator-hub | TypeScript | [Option to rename folder](https://github.com/decentraland/creator-hub/issues/791) | 0 |
| decentraland/ui2 | TypeScript | [UI issues in notifications](https://github.com/decentraland/ui2/issues/281) | 0 |
| decentraland/creator-hub | TypeScript | [Missing owner property on Worlds deployment](https://github.com/decentraland/creator-hub/issues/774) | 0 |
| decentraland/creator-hub | TypeScript | [Change selected item highlight effect](https://github.com/decentraland/creator-hub/issues/768) | 0 |
| decentraland/jump-site | TypeScript | [[Jump Site] - Fix the thumbnails for the scenes and events are not correctly scaled.](https://github.com/decentraland/jump-site/issues/53) | 0 |
| decentraland/asset-packs | TypeScript | [Fix hide image action](https://github.com/decentraland/asset-packs/issues/170) | 0 |
| decentraland/creator-hub | TypeScript | [Reorder scene list on landing](https://github.com/decentraland/creator-hub/issues/437) | 0 |
| decentraland/creator-hub | TypeScript | [Separate search results by category](https://github.com/decentraland/creator-hub/issues/430) | 0 |
| decentraland/creator-hub | TypeScript | [Row spacing in asset packs stretches in ugly way](https://github.com/decentraland/creator-hub/issues/429) | 0 |
| decentraland/creator-hub | TypeScript | [Publish status/history improvements](https://github.com/decentraland/creator-hub/issues/338) | 0 |
| decentraland/creator-hub | TypeScript | [Field width wide as longest option, not current value](https://github.com/decentraland/creator-hub/issues/200) | 0 |
| decentraland/profile | TypeScript | [User FTU to interact with avatar](https://github.com/decentraland/profile/issues/114) | 0 |
| decentraland/builder | TypeScript | [Item badges have broken styles in the Third Party Collections detail page](https://github.com/decentraland/builder/issues/2733) | 0 |
| decentraland/decentraland-connect | TypeScript | [Remove unussed network rpc urls](https://github.com/decentraland/decentraland-connect/issues/59) | 0 |
| decentraland/account | TypeScript | [The withdrawal from Polygon modal styles are broken](https://github.com/decentraland/account/issues/277) | 0 |
| decentraland/marketplace | TypeScript | [Wait until all the profiles are loaded before showing the modal with list of users that picks the item](https://github.com/decentraland/marketplace/issues/1620) | 0 |
| decentraland/account | TypeScript | [Change alias is shown when the user has no names](https://github.com/decentraland/account/issues/264) | 0 |
| decentraland/builder | TypeScript | [Wrong items left to curate for third parties without items to curate](https://github.com/decentraland/builder/issues/2573) | 0 |
| decentraland/builder | TypeScript | [Third party checkboxes being grayed out but functional](https://github.com/decentraland/builder/issues/2572) | 0 |
| decentraland/governance | TypeScript | [Formatting within comments is not displayed correctly](https://github.com/decentraland/governance/issues/776) | 0 |
| decentraland/marketplace | TypeScript | [Move the view listing button from the rental box to the top card in the land management page](https://github.com/decentraland/marketplace/issues/1393) | 0 |
| decentraland/marketplace | TypeScript | [Add a message explaining how bids are going to be affected in the confirm rental listing modal](https://github.com/decentraland/marketplace/issues/1390) | 0 |
| decentraland/builder | TypeScript | [Avoid letting the user click the Enable collection button if the enabling process is pending](https://github.com/decentraland/builder/issues/2489) | 0 |
| decentraland/builder | TypeScript | [I can sign the approve collection transaction and close the modal a few seconds after](https://github.com/decentraland/builder/issues/2488) | 0 |
| decentraland/builder | TypeScript | [[Names] Show error messages when setting a name as an alias or a link fails](https://github.com/decentraland/builder/issues/2455) | 0 |
| decentraland/marketplace | TypeScript | [Add a link to the documentation in the confirm listing modal](https://github.com/decentraland/marketplace/issues/1078) | 0 |
| decentraland/marketplace | TypeScript | [Add a link to the operator's documentation in the confirm rent modal](https://github.com/decentraland/marketplace/issues/1045) | 0 |
| decentraland/marketplace | TypeScript | [Add a tooltip to the proceed button if the price is not set in the confirm rent modal](https://github.com/decentraland/marketplace/issues/1037) | 0 |
| decentraland/decentraland-connect | TypeScript | [Unhandled PollingBlockTracker error crashes the explorer](https://github.com/decentraland/decentraland-connect/issues/41) | 0 |
| decentraland/builder | TypeScript | [The Editor pagination component redirects to the wrong page](https://github.com/decentraland/builder/issues/2410) | 0 |
| decentraland/builder | TypeScript | [Make the Catalyst deployment of non third party wearables queued](https://github.com/decentraland/builder/issues/2389) | 0 |
| decentraland/builder | TypeScript | [Add tests for ens module sagas ](https://github.com/decentraland/builder/issues/2274) | 0 |
| decentraland/marketplace | TypeScript | [[Browse Page] Add Rarities + Collections filters](https://github.com/decentraland/marketplace/issues/737) | 0 |
| decentraland/builder-server | TypeScript | [Stop accepting isPublished, isApproved, minters and managers properties](https://github.com/decentraland/builder-server/issues/553) | 0 |
| decentraland/builder-server | TypeScript | [Stop accepting the id field for Collections on Collections creation](https://github.com/decentraland/builder-server/issues/552) | 0 |
| decentraland/builder | TypeScript | [The item search bar in the third party collection view doesn't work](https://github.com/decentraland/builder/issues/2110) | 0 |
| decentraland/builder | TypeScript | [The loading slots icon breaks the header style while loading](https://github.com/decentraland/builder/issues/1970) | 0 |
| decentraland/builder | TypeScript | [Refactor the ConfirmDelete modal to be used everywhere a delete confirmation is needed](https://github.com/decentraland/builder/issues/1959) | 0 |
| decentraland/builder | TypeScript | [Curation table columns don't have enough padding](https://github.com/decentraland/builder/issues/1944) | 0 |
| decentraland/builder | TypeScript | [Rejecting the transaction in the approval modal shows an unreadable error](https://github.com/decentraland/builder/issues/1924) | 0 |
| decentraland/builder | TypeScript | [Closing the Metamask window when signing the TP approval doesn't show an error](https://github.com/decentraland/builder/issues/1923) | 0 |
| decentraland/builder | TypeScript | [Render the Merkle Tree root in the approval flow modal](https://github.com/decentraland/builder/issues/1865) | 0 |
| decentraland/builder | TypeScript | [Use the builder client to fetch the approval data](https://github.com/decentraland/builder/issues/1855) | 0 |
| decentraland/builder-server | TypeScript | [Replace isomorphic-fetch with node-fetch](https://github.com/decentraland/builder-server/issues/434) | 0 |
| decentraland/marketplace | TypeScript | [Check why 2 requests to fetch the store are sent at the same time](https://github.com/decentraland/marketplace/issues/575) | 0 |
| decentraland/decentraland-dapps | TypeScript | [Support Trezor for meta txs](https://github.com/decentraland/decentraland-dapps/issues/220) | 0 |
| decentraland/builder | TypeScript | [Fix disabled Dropdown Items not showing Popup component](https://github.com/decentraland/builder/issues/1810) | 0 |
| decentraland/builder | TypeScript | [Update TAC for publishing wearables](https://github.com/decentraland/builder/issues/1789) | 0 |
| decentraland/marketplace | TypeScript | [Move Mint Item functionality to the marketplace](https://github.com/decentraland/marketplace/issues/543) | 0 |
| decentraland/builder | TypeScript | [Add a search bar to the /collections list](https://github.com/decentraland/builder/issues/1742) | 0 |
| decentraland/builder | TypeScript | [Order items by blockchain Id in the builder](https://github.com/decentraland/builder/issues/1735) | 0 |
| decentraland/decentraland-connect | TypeScript | [Remove unused files from the public release](https://github.com/decentraland/decentraland-connect/issues/28) | 0 |
| decentraland/builder | TypeScript | [Multiple mints set invalid values](https://github.com/decentraland/builder/issues/1690) | 0 |
| decentraland/account | TypeScript | [Enhance transaction modals](https://github.com/decentraland/account/issues/167) | 0 |
| decentraland/builder | TypeScript | [Show progress bar on Upload Files modal](https://github.com/decentraland/builder/issues/1614) | 0 |
| decentraland/builder | TypeScript | [Broken link on publish collection Content Policy](https://github.com/decentraland/builder/issues/1588) | 0 |
| decentraland/kernel | TypeScript | [Move empty parcels to their own repository](https://github.com/decentraland/kernel/issues/794) | 0 |
| decentraland/builder | TypeScript | [Add a tooltip to the publish button to explain the user what is needed to publish a collection](https://github.com/decentraland/builder/issues/1485) | 0 |
| decentraland/builder | TypeScript | [Show collection/item name/description errors onChange](https://github.com/decentraland/builder/issues/1461) | 0 |
| decentraland/builder | TypeScript | [Refactor: The sagas for collaborators and minters are almost identical](https://github.com/decentraland/builder/issues/1451) | 0 |
| decentraland/builder | TypeScript | [Show a more detailed view of the changes to collaborators/minters](https://github.com/decentraland/builder/issues/1450) | 0 |
| decentraland/decentraland-dapps | TypeScript | [Make the track function `add` generic so we can type the action it supplies](https://github.com/decentraland/decentraland-dapps/issues/143) | 0 |
| decentraland/decentraland-connect | TypeScript | [Consider tracking provider method usage](https://github.com/decentraland/decentraland-connect/issues/13) | 0 |
| decentraland/builder | TypeScript | [[ENS] There's no name check before authorising MANA which can lead to a loss of funds](https://github.com/decentraland/builder/issues/1246) | 0 |
| decentraland/explorer | TypeScript | [Add new AvatarModifier: Force camera mode](https://github.com/decentraland/explorer/issues/1948) | 0 |
| decentraland/atlas-server | TypeScript | [Add a redirect or message with a link to the documentation at /](https://github.com/decentraland/atlas-server/issues/3) | 0 |
| decentraland/builder | TypeScript | [Add a way to de-assign a Name from a Land (Parcel/Estate) from the table](https://github.com/decentraland/builder/issues/1203) | 0 |
| microsoft/genaiscript | TypeScript | [Open Telemetry](https://github.com/microsoft/genaiscript/issues/1323) | 1 |
| microsoft/vscode-python-debugger | TypeScript | [Add a `debugpy.sh` for the no-config debugging](https://github.com/microsoft/vscode-python-debugger/issues/651) | 1 |
| hashicorp/terraform-cdk | TypeScript | [CLI UX: Nicer output for `cdktf synth` if there are no stacks in an app](https://github.com/hashicorp/terraform-cdk/issues/2793) | 1 |
| hashicorp/terraform-cdk | TypeScript | [Support `local-exec` `quiet` attribute](https://github.com/hashicorp/terraform-cdk/issues/2702) | 1 |
| mattermost/mattermost-test-management | TypeScript | [Display Errors and Files name in which they occurr](https://github.com/mattermost/mattermost-test-management/issues/20) | 1 |
| freeCodeCamp/chapter | TypeScript | [Updating Different Users section in contribution guide](https://github.com/freeCodeCamp/chapter/issues/1914) | 1 |
| decentraland/builder | TypeScript | [Add a search bar to NAMEs list](https://github.com/decentraland/builder/issues/3330) | 1 |
| decentraland/creator-hub | TypeScript | [Need to click twice on "Create Scene" button to create the scene](https://github.com/decentraland/creator-hub/issues/832) | 1 |
| decentraland/creator-hub | TypeScript | [Duplicated items appear at the bottom of the list](https://github.com/decentraland/creator-hub/issues/595) | 1 |
| decentraland/marketplace | TypeScript | [Capitalize land filter words](https://github.com/decentraland/marketplace/issues/1395) | 1 |
| decentraland/builder | TypeScript | [Create auto-assign button on mint items from collection modal](https://github.com/decentraland/builder/issues/2442) | 1 |
| decentraland/builder | TypeScript | [Add +- buttons to number input in mint items from collection](https://github.com/decentraland/builder/issues/2443) | 1 |
| decentraland/marketplace | TypeScript | [Inject `title` and description for each page](https://github.com/decentraland/marketplace/issues/603) | 1 |
| decentraland/builder | TypeScript | [Add link to documentation in the id field when creating TP collections](https://github.com/decentraland/builder/issues/1844) | 1 |
| decentraland/decentraland-dapps | TypeScript | [Always show metamask button enable](https://github.com/decentraland/decentraland-dapps/issues/186) | 1 |
| decentraland/builder | TypeScript | [Assigned Parcel Name dissapears after changing language](https://github.com/decentraland/builder/issues/1540) | 1 |
| decentraland/builder | TypeScript | [Rarity dropdown appears when editing representation of published item](https://github.com/decentraland/builder/issues/1465) | 1 |
| decentraland/builder | TypeScript | [Loading indicator in activity overlaps with Menu](https://github.com/decentraland/builder/issues/1399) | 1 |
| decentraland/explorer | TypeScript | [Switch to `?x=1&y=2` instead of `?position=1%C02`](https://github.com/decentraland/explorer/issues/1430) | 1 |
| decentraland/explorer | TypeScript | [Blocking error on console: "Warning: Unsupported graphics API WebGL 2.0"](https://github.com/decentraland/explorer/issues/1333) | 1 |
| huggingface/huggingface.js | TypeScript | [Maximize button not working properly on Hosted inference API block](https://github.com/huggingface/huggingface.js/issues/335) | 2 |
| microsoft/vscode-containers | TypeScript | [Add “Compose Pull / Update All Images” command for Docker Compose projects](https://github.com/microsoft/vscode-containers/issues/414) | 2 |
| hashicorp/terraform-cdk | TypeScript | [Typo in Tokenizer code?](https://github.com/hashicorp/terraform-cdk/issues/2709) | 2 |
| decentraland/marketplace | TypeScript | [It's hard to detect when the kebab menu of the ListCard is clickable](https://github.com/decentraland/marketplace/issues/1866) | 2 |
| decentraland/marketplace | TypeScript | [Show full name when hovering over Lands and Wearables](https://github.com/decentraland/marketplace/issues/590) | 2 |
| huggingface/chat-ui | TypeScript | [Load past conversations using the most recent leaf to determine the visible conversation tree.](https://github.com/huggingface/chat-ui/issues/1208) | 3 |
| huggingface/chat-ui | TypeScript | [System prompt not taken into account when web browsing.](https://github.com/huggingface/chat-ui/issues/1159) | 3 |
| microsoft/vscode-containers | TypeScript | [Add presentation options to Docker extension's compose commands](https://github.com/microsoft/vscode-containers/issues/350) | 3 |
| microsoft/teams.ts | TypeScript | [[cards] support lowercase and Capitalized JSON values](https://github.com/microsoft/teams.ts/issues/132) | 3 |
| microsoft/data-formulator | TypeScript | [Docker Support](https://github.com/microsoft/data-formulator/issues/85) | 3 |
| mattermost/mattermost | TypeScript | [Help Wanted: BitBucket README > Split out admin content to child pages](https://github.com/mattermost/mattermost/issues/25176) | 3 |
| huggingface/chat-ui | TypeScript | [Add option for users to customize search engines in settings page](https://github.com/huggingface/chat-ui/issues/1756) | 4 |
| huggingface/chat-ui | TypeScript | [Chrome app icon on macOS](https://github.com/huggingface/chat-ui/issues/1439) | 4 |
| microsoft/AI-Engineering-Coach | TypeScript | [feat: Context Files](https://github.com/microsoft/AI-Engineering-Coach/issues/60) | 4 |
| microsoft/Power-CAT-Copilot-Studio-Kit | TypeScript | [Bug: Agent Debugger listing only Default Environment from the dropdown](https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/issues/710) | 4 |
| mattermost/mattermost | TypeScript | [[RN] Change "Join" button on sign in page keyboard to "Go"](https://github.com/mattermost/mattermost/issues/26590) | 4 |
| freeCodeCamp/chapter | TypeScript | [Consolidate email templates](https://github.com/freeCodeCamp/chapter/issues/2071) | 4 |
| decentraland/marketplace | TypeScript | [Create a high order component that redirects to the Sign In Page if the user is not connected](https://github.com/decentraland/marketplace/issues/1522) | 4 |
| layer5io/sistent | TypeScript | [[Docs] update readme to include instructions to use npm link](https://github.com/layer5io/sistent/issues/999) | 5 |
| huggingface/chat-ui | TypeScript | [Disabling Reasoning Summary as an Env Option](https://github.com/huggingface/chat-ui/issues/1720) | 5 |
| microsoft/vscode-python-debugger | TypeScript | [Add support for no-config debugging using nushell](https://github.com/microsoft/vscode-python-debugger/issues/647) | 5 |
| mattermost/mattermost | TypeScript | [Help Wanted: Channel Export README > Split out admin content to child pages](https://github.com/mattermost/mattermost/issues/25173) | 5 |
| microsoft/data-formulator | TypeScript | [Expand chart type supports](https://github.com/microsoft/data-formulator/issues/193) | 6 |
| microsoft/teams.ts | TypeScript | [Automatically parse feedback value](https://github.com/microsoft/teams.ts/issues/184) | 7 |
| huggingface/huggingface.js | TypeScript | [Tracking integration for Video Classification](https://github.com/huggingface/huggingface.js/issues/332) | 8 |
| microsoft/Power-CAT-Copilot-Studio-Kit | TypeScript | [Error trying to run Agent Inventory](https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/issues/706) | 8 |
| mattermost/mattermost | TypeScript | [Help Wanted: CircleCI README > Split out admin content to child pages](https://github.com/mattermost/mattermost/issues/25175) | 8 |
| layer5io/sistent | TypeScript | [[Feature] Add Support for Table Variants](https://github.com/layer5io/sistent/issues/992) | 10 |
| mattermost/mattermost | TypeScript | [Bitbucket plugin: Support for bitbucket Datacenter/server](https://github.com/mattermost/mattermost/issues/24188) | 10 |
| mattermost/mattermost | TypeScript | [Create config setting to always have the team sidebar visible](https://github.com/mattermost/mattermost/issues/18010) | 13 |
| mattermost/mattermost | TypeScript | [Interactive Dialogs timeout forbiddingly short in slash command integrations ](https://github.com/mattermost/mattermost/issues/21901) | 14 |
| microsoft/data-formulator | TypeScript | [Create new data loaders to different resources](https://github.com/microsoft/data-formulator/issues/156) | 15 |
| mattermost/mattermost | TypeScript | [Mobile \| Inconsistant channel updated info message on web and mobile](https://github.com/mattermost/mattermost/issues/26917) | 15 |
| mattermost/mattermost | TypeScript | [Mobile Web View: Text is cut off in channel dropdown > channel actions](https://github.com/mattermost/mattermost/issues/25165) | 18 |
| freeCodeCamp/chapter | TypeScript | [Good first issues](https://github.com/freeCodeCamp/chapter/issues/691) | 18 |
| mattermost/mattermost | TypeScript | [Increase max height of the Find Channels modal](https://github.com/mattermost/mattermost/issues/21558) | 20 |
| microsoft/vscode | TypeScript | [Review AsyncIterableObject usage: potential memory leaks and migration to AsyncIterableProducer](https://github.com/microsoft/vscode/issues/256854) | 21 |
| mattermost/mattermost | TypeScript | [Improve the grammar on Account Creation Screen if the email address you entered does not belong to the accepted domain](https://github.com/mattermost/mattermost/issues/15927) | 21 |
| microsoft/vscode | TypeScript | [Disabled and enabled (workspace) extension Disable button dropdown contains both "Disable" and "Disable (Workspace)" items](https://github.com/microsoft/vscode/issues/244138) | 27 |
| mattermost/mattermost | TypeScript | [`Unable to find manifest for extracted plugin` when using `make deploy`](https://github.com/mattermost/mattermost/issues/22614) | 27 |
| mattermost/mattermost | TypeScript | [Fix all initialism errors in the codebase](https://github.com/mattermost/mattermost/issues/16623) | 27 |
| mattermost/mattermost | TypeScript | [Mobile: Slight horizontal indent difference after first line](https://github.com/mattermost/mattermost/issues/27377) | 33 |
| godotengine/godot-docs | reStructuredText | [make_canvas_position_local](https://github.com/godotengine/godot-docs/issues/8313) | 1 |
| godotengine/godot-docs | reStructuredText | [Inconsistent code example between PhysicsShapeQueryParameters3D and PhysicsServer3D](https://github.com/godotengine/godot-docs/issues/8305) | 1 |
| godotengine/godot-docs | reStructuredText | [Physics2DDirectSpaceState does not specify local or global coordinates](https://github.com/godotengine/godot-docs/issues/3299) | 2 |

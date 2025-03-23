# Goood First Issues :palm_tree:

This page contains open issues tagged with the label *good first issue*. It gathers issues from some famous libraries(at least for me).
Let me knowif there are others you would like to see here :pizza:

`update_issues.py` can  be modified to  return the data in json or to csv. 
To run the script locally:
* create an `.env` file in the root directory, and add
```
ACCESS_TOKEN=<YOUR_ACCESS_TOKEN>
USERNAMES=<REPO_OWNER1>,<REPO_OWNER2>,<REPO_OWNER3>,...
```
* How to create and  manage GitHub API access tokens in [this article](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).


If you are wondering where to begin in the  journey contributing to open-source projects, these are good articles to get you started! :sailboat:

* [First Contributions Repository](https://github.com/firstcontributions/first-contributions)
* [A Beginner's Guide to Contributing to Open Source Projects](https://blog.ossph.org/a-beginners-guide-to-contributing-to-open-source-projects/)

## List of Good First Issues to start Collaborating! :surfer: <sub><sub>Last run: 2025-03-23</sub></sub>

### Batchfile

| Repo | Title | Comments |
| --- | --- | --- |
| pytorch/csprng | [Clone torchvision .circleci/regenerate.py framework to automate config.yml generation](https://github.com/pytorch/csprng/issues/97) | 0 |
| pytorch/csprng | [Add clang-format to CircleCI config](https://github.com/pytorch/csprng/issues/41) | 0 |
| pytorch/csprng | [Setup CMake build](https://github.com/pytorch/csprng/issues/38) | 0 |
| pytorch/csprng | [Improve test_geometric](https://github.com/pytorch/csprng/issues/7) | 0 |
| pytorch/csprng | [Delete OffsetCalculator.cuh and THCIntegerDivider.cuh and replace them with PyTorch headers](https://github.com/pytorch/csprng/issues/39) | 1 |
| pytorch/csprng | [ZeroDivisionError: float division by zero in test_cpu_parallel](https://github.com/pytorch/csprng/issues/88) | 3 |

### C++

| Repo | Title | Comments |
| --- | --- | --- |
| pytorch/executorch | [Python apis for loading and saving .ptd from dictionaries](https://github.com/pytorch/executorch/issues/8542) | 0 |
| pytorch/executorch | [insert_write_back_for_buffers_pass should inject copy_ nodes at the earliest possible spot.](https://github.com/pytorch/executorch/issues/7345) | 0 |
| pytorch/glow | [[TensorLayout] Add a way to specify canonical layout propagation to NodeGen](https://github.com/pytorch/glow/issues/3834) | 0 |
| pytorch/glow | [[Runtime] Expand Yaml DeviceConfig loading to include HostConfig](https://github.com/pytorch/glow/issues/3079) | 0 |
| pytorch/glow | [[runtime] add device memory size configuration to the DeviceConfig::parameters map on all backends](https://github.com/pytorch/glow/issues/2899) | 0 |
| pytorch/glow | [resnet-* example code should reuse Tensor memory for images](https://github.com/pytorch/glow/issues/2898) | 0 |
| pytorch/glow | [Example binaries should handle HostManager active request limit](https://github.com/pytorch/glow/issues/2816) | 0 |
| pytorch/glow | [[ONNXIFI] Add additional precondition checks to model loaders](https://github.com/pytorch/glow/issues/2188) | 0 |
| pytorch/glow | [[ONNXIFI][GraphAPI] Add "orErr" methods for graph creation api](https://github.com/pytorch/glow/issues/2187) | 0 |
| pytorch/glow | [ConvBench should use the layers of ResNet](https://github.com/pytorch/glow/issues/1887) | 0 |
| pytorch/glow | [ConvBench should use libjit_convolution_D8KKC8](https://github.com/pytorch/glow/issues/1886) | 0 |
| pytorch/multipy | [Create a Contributing.md](https://github.com/pytorch/multipy/issues/252) | 0 |
| pytorch/executorch | [Remove EXECUTORCH_BUILD_HOST_TARGETS](https://github.com/pytorch/executorch/issues/9404) | 1 |
| pytorch/executorch | [Refactor binary op partitioner configs under binary op config class](https://github.com/pytorch/executorch/issues/9024) | 1 |
| pytorch/executorch | [Partitioner to not delegate mixed dtype operators](https://github.com/pytorch/executorch/issues/9023) | 1 |
| pytorch/glow | [[CPU] Remove the need for Rescale for the CPUMaxSplat](https://github.com/pytorch/glow/issues/4656) | 1 |
| pytorch/multipy | [Add Poetry build to multipy](https://github.com/pytorch/multipy/issues/211) | 1 |
| pytorch/glow | [New files added under glow/test/models/ don't get copied to build folder until clean build is performed.](https://github.com/pytorch/glow/issues/4647) | 2 |
| pytorch/glow | [Make all useful data structures in Glow easy to dump in a textual form](https://github.com/pytorch/glow/issues/2831) | 2 |
| pytorch/glow | [[Importers] Move "run and compare" tests from importer tests to operator tests](https://github.com/pytorch/glow/issues/1909) | 2 |
| pytorch/glow | [Need to canonicalize or optimize high-dim concat to concat+transpose](https://github.com/pytorch/glow/issues/1296) | 2 |
| godotengine/godot | [`_OnTreeItemSelected()` signal receiver method using C# doesn't allow adding of items](https://github.com/godotengine/godot/issues/103101) | 2 |
| tensorflow/minigo | [Support more GTP commands](https://github.com/tensorflow/minigo/issues/46) | 3 |
| pytorch/executorch | [Optimized linear op doesn't support bias](https://github.com/pytorch/executorch/issues/8234) | 3 |
| pytorch/glow | [Move layout information from nodes constructor' to their Glow types](https://github.com/pytorch/glow/issues/3790) | 3 |
| pytorch/glow | [[habana] Implement backend specific verifications](https://github.com/pytorch/glow/issues/3480) | 3 |
| pytorch/executorch | [_load_for_executorch pybinding cannot load model for training](https://github.com/pytorch/executorch/issues/4908) | 4 |
| pytorch/glow | [[GraphOptz] Sink Quantize below Reshape](https://github.com/pytorch/glow/issues/4629) | 4 |
| godotengine/godot | [Image.FORMAT_R8 uses Alpha in GLES2 instead of Red channel, this is not reflected in docs](https://github.com/godotengine/godot/issues/38974) | 4 |
| pytorch/glow | [Fuse RescaleQuantized in the ChannelwiseQuantizedConv](https://github.com/pytorch/glow/issues/4928) | 5 |
| pytorch/glow | [Bring back the sinking RELU below Pool optimization](https://github.com/pytorch/glow/issues/3247) | 5 |
| pytorch/glow | [Use gtest-parallel](https://github.com/pytorch/glow/issues/2412) | 5 |
| godotengine/godot | [[Godot v4.4] Gizmos exponentially increasing Draw Calls and Objects when turned on](https://github.com/godotengine/godot/issues/103676) | 5 |
| pytorch/glow | [Glow should provide its own implementation of a random number generator to ensure deterministic testing and avoid platform-dependent differences](https://github.com/pytorch/glow/issues/1556) | 6 |
| xbmc/xbmc | [Make sorting locale-aware on Android](https://github.com/xbmc/xbmc/issues/15125) | 7 |
| godotengine/godot | [ERROR: The InputMap action "spatial_editor/viewport_pan_modifier_1" doesn't exist](https://github.com/godotengine/godot/issues/103539) | 8 |
| godotengine/godot | [AnimationPlayerEditor inserts markers and keys at the mouse cursor position, not at the timeline cursor](https://github.com/godotengine/godot/issues/103272) | 8 |
| pytorch/glow | [Make the execution of the Glow compiler more deterministic between multiple runs](https://github.com/pytorch/glow/issues/1948) | 9 |
| opencv/opencv_contrib | [reg: broken python sample](https://github.com/opencv/opencv_contrib/issues/1935) | 9 |
| godotengine/godot | [OS.get_stdin_type() returns 0 (invalid) on Windows [v4.4]](https://github.com/godotengine/godot/issues/103086) | 9 |
| godotengine/godot | [Improve error reporting when rcedit fails to change icon / set PE data](https://github.com/godotengine/godot/issues/27765) | 9 |
| opencv/opencv_contrib | [selectROI pointer almost invisible on certain colours](https://github.com/opencv/opencv_contrib/issues/1719) | 14 |
| pytorch/glow | [[ONNXModelLoader] Support for LogSoftmax operator is missing](https://github.com/pytorch/glow/issues/4399) | 16 |
| pytorch/glow | [Use explicit std::string conversions instead of implicit llvm::StringRef->std::string conversions to prepare Glow for builds using LLVM >=11](https://github.com/pytorch/glow/issues/5068) | 18 |
| godotengine/godot | [LightOccluder2D polygons cause editor slowdowns](https://github.com/godotengine/godot/issues/52703) | 18 |
| opencv/opencv | [HDR tutorial result is different from the code running.](https://github.com/opencv/opencv/issues/22219) | 21 |
| godotengine/godot | [Using the RenderingServer to add a texture to the scene, the texture appears at bad position during one frame](https://github.com/godotengine/godot/issues/94988) | 24 |
| godotengine/godot | [You're breathtaking!](https://github.com/godotengine/godot/issues/100000) | 28 |
| godotengine/godot | [PointLight2D doesn't respect Nearest texture filter for normal-maps or shadows](https://github.com/godotengine/godot/issues/76266) | 28 |
| tensorflow/tensorflow | [Feature Request: GPUOptions for Go binding](https://github.com/tensorflow/tensorflow/issues/22926) | 106 |
| godotengine/godot | [[TRACKER] Unit tests to add or improve](https://github.com/godotengine/godot/issues/43440) | 222 |

### Cython

| Repo | Title | Comments |
| --- | --- | --- |
| ansible/pylibssh | [[BUG] Flaky `tests/unit/sftp_test.py::test_put`](https://github.com/ansible/pylibssh/issues/351) | 3 |

### Emacs Lisp

| Repo | Title | Comments |
| --- | --- | --- |
| godotengine/emacs-gdscript-mode | [Rewrite gdscript-imenu to provide GDScript-specific tables](https://github.com/godotengine/emacs-gdscript-mode/issues/89) | 0 |
| godotengine/emacs-gdscript-mode | [Buffer does not revert or update instantly after formatting buffer](https://github.com/godotengine/emacs-gdscript-mode/issues/88) | 3 |
| godotengine/emacs-gdscript-mode | [Address compile warnings](https://github.com/godotengine/emacs-gdscript-mode/issues/87) | 6 |

### GDScript

| Repo | Title | Comments |
| --- | --- | --- |
| godotengine/godot-demo-projects | [Update plugins demo to use custom Resources](https://github.com/godotengine/godot-demo-projects/issues/1061) | 0 |
| godotengine/godot-benchmarks | [[Call to Action] Benchmarks for the benchmark server](https://github.com/godotengine/godot-benchmarks/issues/36) | 5 |
| godotengine/godot-benchmarks | [[TRACKER] Benchmarks to create](https://github.com/godotengine/godot-benchmarks/issues/11) | 11 |

### Go

| Repo | Title | Comments |
| --- | --- | --- |
| ansible/receptor | [append conntype string representation in status output](https://github.com/ansible/receptor/issues/423) | 0 |
| ansible/receptor | [add work status command to receptorctl](https://github.com/ansible/receptor/issues/374) | 1 |
| ansible/receptor | [quality of life -- order work list output based on most recent work units](https://github.com/ansible/receptor/issues/425) | 2 |

### Java

| Repo | Title | Comments |
| --- | --- | --- |
| pytorch/serve | [The captum for bert notebook needs update](https://github.com/pytorch/serve/issues/1317) | 0 |
| pytorch/serve | [Enable naked DIR test case for windows environment](https://github.com/pytorch/serve/issues/882) | 0 |
| pytorch/serve | [[Educational] Typing `.py` files iteratively with mypy](https://github.com/pytorch/serve/issues/1512) | 1 |
| pytorch/serve | [Built-in handler for regression](https://github.com/pytorch/serve/issues/987) | 1 |
| pytorch/serve | [permission error while trying to remove previous artifact files in `/tmp/`](https://github.com/pytorch/serve/issues/1532) | 3 |
| pytorch/serve | [Torchserve M1 support detailed plan](https://github.com/pytorch/serve/issues/2555) | 4 |
| pytorch/serve | [add support for SeTFiT models](https://github.com/pytorch/serve/issues/2107) | 4 |
| pytorch/serve | [[BUG] Dockerfile with nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04 gives ascii codec error](https://github.com/pytorch/serve/issues/821) | 4 |
| pytorch/serve | [how does `default_response_timeout` work?](https://github.com/pytorch/serve/issues/2452) | 6 |
| pytorch/serve | [[Suggestion] Loading torch-model-archiver arguments from YAML](https://github.com/pytorch/serve/issues/780) | 6 |
| pytorch/serve | [Handle invalid input intelligently ！](https://github.com/pytorch/serve/issues/2459) | 7 |

### JavaScript

| Repo | Title | Comments |
| --- | --- | --- |
| huggingface/transformers.js | [Is 'aggregation_strategy' parameter available for token classification pipeline?](https://github.com/huggingface/transformers.js/issues/633) | 2 |
| huggingface/transformers.js | [[Feature request] Return offset mapping using tokenizer](https://github.com/huggingface/transformers.js/issues/425) | 2 |
| pytorch/ci-hud | [Restore "Show service jobs" checkbox to GitHubStatusDisplay.js ](https://github.com/pytorch/ci-hud/issues/110) | 2 |
| huggingface/transformers.js | [[Doc request] Add an example guide of how to use it in Svelte (and deploy to HF Spaces)](https://github.com/huggingface/transformers.js/issues/171) | 7 |
| huggingface/transformers.js | [[Feature request] Logging Level and Progress Bar for Model Downloads](https://github.com/huggingface/transformers.js/issues/117) | 9 |

### Jinja

| Repo | Title | Comments |
| --- | --- | --- |
| ansible/galaxy_collection | [Replace order of roles](https://github.com/ansible/galaxy_collection/issues/396) | 0 |
| ansible/galaxy_collection | [infra.ah_configuration.publish leaves clone dirs behind](https://github.com/ansible/galaxy_collection/issues/377) | 0 |
| ansible/awx-operator | [Add multi-arch build target](https://github.com/ansible/awx-operator/issues/1680) | 1 |
| ansible/product-demos | [Add teardown template/workflow for "Deploy Cloud Stack in AWS" workflow](https://github.com/ansible/product-demos/issues/192) | 1 |
| ansible/awx-operator | [annotations not applied to postgres statefulset](https://github.com/ansible/awx-operator/issues/1624) | 2 |
| ansible/awx-operator | [Inflated Total Host Count on Dashboard when Using Constructed Inventory with Existing Inventories](https://github.com/ansible/awx-operator/issues/1459) | 2 |
| ansible/awx-operator | [Extend README with external logging examples](https://github.com/ansible/awx-operator/issues/1086) | 2 |
| ansible/receptor-collection | [Support for Debian 12](https://github.com/ansible/receptor-collection/issues/63) | 2 |
| ansible/awx-operator | [Inability to overwrite namespace when using awx-operator chart](https://github.com/ansible/awx-operator/issues/999) | 3 |
| ansible/awx-operator | [Password set via UI gets overwritten by initialize_django playbook](https://github.com/ansible/awx-operator/issues/869) | 5 |

### Jupyter Notebook

| Repo | Title | Comments |
| --- | --- | --- |
| tensorflow/probability | [providing sample weights to glm.fit() and glm.fit.sparse()](https://github.com/tensorflow/probability/issues/252) | 0 |
| tensorflow/probability | [Sigmoid belief network example/tutorial](https://github.com/tensorflow/probability/issues/70) | 0 |
| tensorflow/probability | [Logistic factorial analysis example/tutorial](https://github.com/tensorflow/probability/issues/68) | 0 |
| tensorflow/swift-models | [Add documentation to the Gym models to specify additional dependencies for DQN](https://github.com/tensorflow/swift-models/issues/657) | 0 |
| tensorflow/swift-models | [[BERT-CoLA]: Use common file extraction functions](https://github.com/tensorflow/swift-models/issues/489) | 0 |
| tensorflow/swift-models | [Verify BERT variants](https://github.com/tensorflow/swift-models/issues/433) | 0 |
| pytorch/botorch | [[Feature Request] Allow negative indices to fixed_features in optimizers](https://github.com/pytorch/botorch/issues/2605) | 0 |
| pytorch/opacus | [Update grad sample algorithm for Convolution](https://github.com/pytorch/opacus/issues/145) | 0 |
| tensorflow/probability | [Feature Request: Add crps method to tfp.distributions](https://github.com/tensorflow/probability/issues/1340) | 1 |
| tensorflow/probability | [Keyword argument overload (?) in tfb.real_nvp_default_template](https://github.com/tensorflow/probability/issues/350) | 1 |
| tensorflow/probability | [Item response theory model example/tutorial](https://github.com/tensorflow/probability/issues/69) | 1 |
| tensorflow/probability | [Bayesian neural network tutorial](https://github.com/tensorflow/probability/issues/66) | 1 |
| tensorflow/swift-models | [Add logging callbacks for training statistics ](https://github.com/tensorflow/swift-models/issues/663) | 1 |
| pytorch/botorch | [[Bug] [relatively easy fix] `gen_one_shot_kg_initial_conditions` should error when provided inter-point constraints](https://github.com/pytorch/botorch/issues/1851) | 1 |
| tensorflow/probability | [Support for SeparableConv1DFlipout](https://github.com/tensorflow/probability/issues/745) | 2 |
| tensorflow/probability | [NotImplementedError: mean is not implemented: Categorical](https://github.com/tensorflow/probability/issues/685) | 2 |
| tensorflow/probability | [Always-on dropout layer](https://github.com/tensorflow/probability/issues/420) | 2 |
| tensorflow/probability | [DenseFlipOut layer](https://github.com/tensorflow/probability/issues/88) | 2 |
| tensorflow/probability | [Categorical autoregressive distribution with LSTM example/tutorial](https://github.com/tensorflow/probability/issues/73) | 2 |
| tensorflow/swift-models | [Better error message on unzip failure](https://github.com/tensorflow/swift-models/issues/675) | 2 |
| tensorflow/swift-models | [Find a more descriptive word for `numericalized`](https://github.com/tensorflow/swift-models/issues/598) | 2 |
| tensorflow/swift-models | [Rewrite long nested `Sequential` types using `Sequential{N}` typealiases](https://github.com/tensorflow/swift-models/issues/492) | 2 |
| tensorflow/swift-models | [[BERT-CoLA] Data source resolution](https://github.com/tensorflow/swift-models/issues/488) | 2 |
| tensorflow/swift-models | [Object detection examples](https://github.com/tensorflow/swift-models/issues/149) | 2 |
| pytorch/functorch | [Add vmap support for PyTorch operators](https://github.com/pytorch/functorch/issues/1088) | 2 |
| pytorch/opacus | [Double-charging privacy in DC-GAN example](https://github.com/pytorch/opacus/issues/418) | 2 |
| huggingface/agents-course | [Improve diagrams in unit 2.1](https://github.com/huggingface/agents-course/issues/233) | 3 |
| tensorflow/adanet | [Allow one to forward features to predictions](https://github.com/tensorflow/adanet/issues/114) | 3 |
| tensorflow/probability | [Feature Request: Alternative Horseshoe Parameterization as tfp distribution](https://github.com/tensorflow/probability/issues/1465) | 3 |
| tensorflow/probability | [Please add example on NUTS sampling from posterior for Bayesian Logistic Regression](https://github.com/tensorflow/probability/issues/588) | 3 |
| tensorflow/probability | [Feature request: Tweedie distribution](https://github.com/tensorflow/probability/issues/529) | 3 |
| tensorflow/probability | [CholeskyWishart distribution](https://github.com/tensorflow/probability/issues/527) | 3 |
| tensorflow/probability | [improve text and visuals in Bayesian Gaussian mixture model tutorial](https://github.com/tensorflow/probability/issues/74) | 3 |
| tensorflow/swift | [Installation verification tool](https://github.com/tensorflow/swift/issues/479) | 3 |
| tensorflow/probability | [A question about target_log_prob_fn](https://github.com/tensorflow/probability/issues/611) | 4 |
| tensorflow/probability | [Provide a resimulation Metropolis TransitionKernel](https://github.com/tensorflow/probability/issues/218) | 4 |
| tensorflow/swift-models | [Translation example](https://github.com/tensorflow/swift-models/issues/148) | 4 |
| pytorch/botorch | [[Feature Request] InputDataWarnings are are confusing](https://github.com/pytorch/botorch/issues/1847) | 4 |
| tensorflow/probability | [Laplace approximation](https://github.com/tensorflow/probability/issues/570) | 5 |
| tensorflow/probability | [Missing Inverse Wishart - redefine Wishart?](https://github.com/tensorflow/probability/issues/247) | 5 |
| tensorflow/probability | [Categorical features in logistic regression](https://github.com/tensorflow/probability/issues/94) | 5 |
| tensorflow/probability | [Stochastic block model example/tutorial](https://github.com/tensorflow/probability/issues/71) | 5 |
| tensorflow/probability | [BFGS user should be able to pass parameters to the line search](https://github.com/tensorflow/probability/issues/1043) | 6 |
| tensorflow/probability | [Tutorial on Variational Inference](https://github.com/tensorflow/probability/issues/149) | 6 |
| tensorflow/swift-models | [Speech to text example](https://github.com/tensorflow/swift-models/issues/147) | 7 |
| tensorflow/probability | [Any plans to update the examples to TensorFlow 2?](https://github.com/tensorflow/probability/issues/607) | 8 |
| tensorflow/probability | [Sample different weights for examples within a  batch](https://github.com/tensorflow/probability/issues/153) | 9 |
| tensorflow/probability | [[Feature Request] tensorflow_probability.distributions.GeneralizedGamma](https://github.com/tensorflow/probability/issues/1081) | 11 |
| tensorflow/probability | [Feature Request: Efficient Poisson Binomial PMF/CDF in tfp](https://github.com/tensorflow/probability/issues/1453) | 13 |
| tensorflow/probability | [[Feature Request] Zero-Inflated Poisson and Negative Binomial distributions](https://github.com/tensorflow/probability/issues/1134) | 13 |
| tensorflow/swift-models | [UNet Example](https://github.com/tensorflow/swift-models/issues/35) | 15 |
| huggingface/huggingface-llama-recipes | [Call for contributions](https://github.com/huggingface/huggingface-llama-recipes/issues/43) | 20 |

### PHP

| Repo | Title | Comments |
| --- | --- | --- |
| zeromicro/goctl-swagger | [support for openapi 3.0 ](https://github.com/zeromicro/goctl-swagger/issues/52) | 0 |
| godotengine/godot-asset-library | [Categories need a description (tooltip?) when hovered/selected](https://github.com/godotengine/godot-asset-library/issues/74) | 1 |
| godotengine/godot-asset-library | [keep the content of the submition form when its not validated, or try some ajax realtime pre-validation](https://github.com/godotengine/godot-asset-library/issues/61) | 1 |
| godotengine/godot-asset-library | [A way to cancel edit requests](https://github.com/godotengine/godot-asset-library/issues/149) | 3 |
| godotengine/godot-asset-library | [Sanitize inputs for Asset data/fields, like URLs](https://github.com/godotengine/godot-asset-library/issues/204) | 5 |

### PostScript

| Repo | Title | Comments |
| --- | --- | --- |
| django/djangoproject.com | [Github login doesn't work for community pages](https://github.com/django/djangoproject.com/issues/835) | 3 |
| django/djangoproject.com | [Badges page and badges themselves](https://github.com/django/djangoproject.com/issues/126) | 3 |
| django/djangoproject.com | [Documentation table of contents is hard to reach on mobile devices](https://github.com/django/djangoproject.com/issues/494) | 4 |
| django/djangoproject.com | [Remove non-canonical docs versions from sitemap.xml](https://github.com/django/djangoproject.com/issues/878) | 5 |
| django/djangoproject.com | [fundraising: 'customer.subscription.deleted' webhook event always gets 404 response](https://github.com/django/djangoproject.com/issues/764) | 5 |
| django/djangoproject.com | [Docs for old supported versions should indicate that a newer version is available](https://github.com/django/djangoproject.com/issues/1122) | 6 |
| django/djangoproject.com | [Support switching languages on non-docs sites](https://github.com/django/djangoproject.com/issues/883) | 6 |
| django/djangoproject.com | [Improvements to the Corporate Sponsor Experience](https://github.com/django/djangoproject.com/issues/1171) | 7 |
| django/djangoproject.com | [Improve Documentation by having list of topics fixed on the left and table of contents on the right ](https://github.com/django/djangoproject.com/issues/1129) | 7 |
| django/djangoproject.com | [Use noindex meta tag or header, not robots.txt, to block untranslated docs pages](https://github.com/django/djangoproject.com/issues/877) | 7 |
| django/djangoproject.com | [Improve 404 page](https://github.com/django/djangoproject.com/issues/1347) | 10 |
| django/djangoproject.com | [Make right sidebar independent from main content](https://github.com/django/djangoproject.com/issues/1366) | 12 |
| django/djangoproject.com | [Localize the fundraising app](https://github.com/django/djangoproject.com/issues/377) | 17 |
| django/djangoproject.com | [Add Click to copy text for commands present in the official Django website.](https://github.com/django/djangoproject.com/issues/1276) | 19 |

### Python

| Repo | Title | Comments |
| --- | --- | --- |
| huggingface/dataset-viewer | [Use `revision_exists` (hfh)](https://github.com/huggingface/dataset-viewer/issues/2562) | 0 |
| huggingface/dataset-viewer | [Cache/Queue metrics should not be negative](https://github.com/huggingface/dataset-viewer/issues/2495) | 0 |
| huggingface/nanotron | [Add Debug utility to be able to preview first samples used for training](https://github.com/huggingface/nanotron/issues/184) | 0 |
| huggingface/nanotron | [[Feature] Use CUDA event for measuring elasped time](https://github.com/huggingface/nanotron/issues/88) | 0 |
| huggingface/nanotron | [[Feature] Refactor `ParallelContext.world_rank_matrix`](https://github.com/huggingface/nanotron/issues/77) | 0 |
| ansible/ansible-dev-tools | [Ensure tests are passing with devspaces container](https://github.com/ansible/ansible-dev-tools/issues/467) | 0 |
| ansible/ansible-jupyter-kernel | [Add support for handlers](https://github.com/ansible/ansible-jupyter-kernel/issues/53) | 0 |
| ansible/ansible-jupyter-kernel | [Add a #library cell type](https://github.com/ansible/ansible-jupyter-kernel/issues/26) | 0 |
| ansible/awx | [[ui_next] Add All/Any workflow viz indication to Workflow Viz Legend/Key](https://github.com/ansible/awx/issues/9791) | 0 |
| ansible/dispatcherd | [Enforce UUID format, add "origin" information in message data](https://github.com/ansible/dispatcherd/issues/96) | 0 |
| ansible/dispatcherd | [Do some minor linting of test files](https://github.com/ansible/dispatcherd/issues/73) | 0 |
| ansible/django-ansible-base | [`ansible_base.lib.utils.models.diff` takes unused `sanitize_encrypted` param and has outdated return docstring](https://github.com/ansible/django-ansible-base/issues/688) | 0 |
| tensorflow/moonlight | [Follow the MusicXML schema](https://github.com/tensorflow/moonlight/issues/65) | 0 |
| tensorflow/moonlight | [Export stem directions in MusicXML](https://github.com/tensorflow/moonlight/issues/25) | 0 |
| tensorflow/moonlight | [Chord duration correction](https://github.com/tensorflow/moonlight/issues/2) | 0 |
| tensorflow/moonlight | [Export the key signature to MusicXML](https://github.com/tensorflow/moonlight/issues/1) | 0 |
| pytorch/ao | [Accelerate activation sparsity with activation compression](https://github.com/pytorch/ao/issues/1920) | 0 |
| pytorch/ao | [Unittests Migration Progress](https://github.com/pytorch/ao/issues/1621) | 0 |
| pytorch/ao | [Learned fake quantize for QAT](https://github.com/pytorch/ao/issues/545) | 0 |
| pytorch/ao | [Remove docstring duplications](https://github.com/pytorch/ao/issues/407) | 0 |
| pytorch/examples | [imagenet benchmark measure elapsed time function issue](https://github.com/pytorch/examples/issues/741) | 0 |
| pytorch/examples | [Why there is no tanh activation at the end of TransformerNet?](https://github.com/pytorch/examples/issues/570) | 0 |
| pytorch/examples | [Distributed doesn't work with env:// init_method](https://github.com/pytorch/examples/issues/458) | 0 |
| pytorch/examples | [Is the loss of the first word covered during the language model evaluation?](https://github.com/pytorch/examples/issues/453) | 0 |
| pytorch/examples | [The casting problem on the result of the model.](https://github.com/pytorch/examples/issues/433) | 0 |
| pytorch/examples | [Example code (mnist) does not work under torch.utils.bottleneck](https://github.com/pytorch/examples/issues/391) | 0 |
| pytorch/PiPPy | [Support Segformer models in HF tests](https://github.com/pytorch/PiPPy/issues/592) | 0 |
| pytorch/PiPPy | [Support ConvNext models in HF tests](https://github.com/pytorch/PiPPy/issues/486) | 0 |
| pytorch/PiPPy | [Support Wav2Vec2 models in HF tests](https://github.com/pytorch/PiPPy/issues/485) | 0 |
| pytorch/PiPPy | [Support ResNet models in HF tests](https://github.com/pytorch/PiPPy/issues/484) | 0 |
| pytorch/PiPPy | [[spmd] DistributedTensor doesn't implement is_pinned](https://github.com/pytorch/PiPPy/issues/418) | 0 |
| pytorch/PiPPy | [Support Donut SWIN models in HF tests](https://github.com/pytorch/PiPPy/issues/361) | 0 |
| pytorch/PiPPy | [Create mypy.ini](https://github.com/pytorch/PiPPy/issues/348) | 0 |
| pytorch/PiPPy | [Support DistilBert models in HF tests ](https://github.com/pytorch/PiPPy/issues/272) | 0 |
| pytorch/PiPPy | [Support Deberta models in HF tests](https://github.com/pytorch/PiPPy/issues/261) | 0 |
| pytorch/PiPPy | [Support HubertForSequenceClassification models in HF tests](https://github.com/pytorch/PiPPy/issues/254) | 0 |
| pytorch/PiPPy | [Support LxmertForPreTraining models in HF tests](https://github.com/pytorch/PiPPy/issues/253) | 0 |
| pytorch/PiPPy | [Support Speech2Text models in HF tests](https://github.com/pytorch/PiPPy/issues/249) | 0 |
| pytorch/PiPPy | [Support CLIP models in HF tests](https://github.com/pytorch/PiPPy/issues/248) | 0 |
| pytorch/PiPPy | [Support SWIN models in HF tests](https://github.com/pytorch/PiPPy/issues/243) | 0 |
| pytorch/pytorch | [Cleanup ctx manager state management](https://github.com/pytorch/pytorch/issues/149572) | 0 |
| pytorch/rl | [[DO NOT CLOSE] Call for contributions](https://github.com/pytorch/rl/issues/509) | 0 |
| pytorch/tensordict | [[Feature Request] Deprecate `_run_checks` in favour of `TensorDict._checked`](https://github.com/pytorch/tensordict/issues/182) | 0 |
| pytorch/torcharrow | [Making BaseColumn::genericUnaryUDF and the family free functions](https://github.com/pytorch/torcharrow/issues/197) | 0 |
| pytorch/torcharrow | [Call type inferring in interop.from_pylist](https://github.com/pytorch/torcharrow/issues/80) | 0 |
| pytorch/torcharrow | [Move `torcharrow/test` to `test`](https://github.com/pytorch/torcharrow/issues/24) | 0 |
| pytorch/torchchat | [GeneratorArgs.is_torchtune_model is a misnomer](https://github.com/pytorch/torchchat/issues/1273) | 0 |
| pytorch/torchft | [add option to skip initial sync in Manager](https://github.com/pytorch/torchft/issues/117) | 0 |
| pytorch/torchtune | [Add add_end_token to the Qwen Models](https://github.com/pytorch/torchtune/issues/2481) | 0 |
| pytorch/torchtune | [Add add_end_token to Phi tokenizers](https://github.com/pytorch/torchtune/issues/2480) | 0 |
| pytorch/torchtune | [Add add_end_token to the Gemma Tokenizer](https://github.com/pytorch/torchtune/issues/2478) | 0 |
| pytorch/torchtune | [[Docs] Recipe documentation tracker](https://github.com/pytorch/torchtune/issues/1408) | 0 |
| pytorch/torchtune | [Validate all paths before doing any expensive work](https://github.com/pytorch/torchtune/issues/861) | 0 |
| pytorch/xla | [Confusion between xla_model.xla_device() and runtime.xla_device()](https://github.com/pytorch/xla/issues/7831) | 0 |
| pytorch/xla | [Op info test for `bmm .. ceil`](https://github.com/pytorch/xla/issues/7546) | 0 |
| pytorch/xla | [Op info test for `rsub .. searchsorted`](https://github.com/pytorch/xla/issues/7532) | 0 |
| pytorch/xla | [Op info test for `norm .. pca_lowrank`](https://github.com/pytorch/xla/issues/7528) | 0 |
| pytorch/xla | [Op info test for `nn.functional.softmin .. nonzero_static`](https://github.com/pytorch/xla/issues/7527) | 0 |
| pytorch/xla | [Op info test for `nn.functional.group_norm .. nn.functional.layer_norm`](https://github.com/pytorch/xla/issues/7522) | 0 |
| pytorch/xla | [Op info test for `nn.functional.conv_transpose3d .. nn.functional.ctc_loss`](https://github.com/pytorch/xla/issues/7519) | 0 |
| pytorch/xla | [Op info test for `linalg.ldl_factor_ex`](https://github.com/pytorch/xla/issues/7487) | 0 |
| pytorch/xla | [Op info test for `linalg.householder_product`](https://github.com/pytorch/xla/issues/7483) | 0 |
| pytorch/xla | [Op info test for `linalg.cholesky_ex`](https://github.com/pytorch/xla/issues/7463) | 0 |
| pytorch/xla | [Op info test for `linalg.cholesky`](https://github.com/pytorch/xla/issues/7462) | 0 |
| huggingface/dataset-viewer | [Simplify test code where a dataset is set as gated](https://github.com/huggingface/dataset-viewer/issues/3063) | 1 |
| huggingface/dataset-viewer | [Use "Sign-In with HF" instead of token in admin-UI](https://github.com/huggingface/dataset-viewer/issues/2373) | 1 |
| huggingface/dataset-viewer | [Use `CONSTANT_LIST.copy` in list config fieds](https://github.com/huggingface/dataset-viewer/issues/1522) | 1 |
| huggingface/diffusers | [`prepare_image` in Kandinsky pipelines doesn't support `torch.Tensor`](https://github.com/huggingface/diffusers/issues/11060) | 1 |
| huggingface/diffusers | [Do we have any script covert from hf format to orginal format?](https://github.com/huggingface/diffusers/issues/10076) | 1 |
| huggingface/nanotron | [[Bug] Missing `_is_using_mup` when resume checkpoint](https://github.com/huggingface/nanotron/issues/198) | 1 |
| huggingface/nanotron | [We don't save checkpoint after training ends](https://github.com/huggingface/nanotron/issues/163) | 1 |
| huggingface/nanotron | [FEAT: Support 1.58-bit LLMs training](https://github.com/huggingface/nanotron/issues/114) | 1 |
| huggingface/nanotron | [[Feature Request] Add simple communications benchmarks to the repo](https://github.com/huggingface/nanotron/issues/43) | 1 |
| ansible/ansible-lint | [Linter should consider the same paths that `ansible.builtin.import_tasks` uses to import relative paths](https://github.com/ansible/ansible-lint/issues/4474) | 1 |
| ansible/ansible-navigator | [Many params missing change after initial = False](https://github.com/ansible/ansible-navigator/issues/423) | 1 |
| ansible/awx | [Scheduled Job prompted extra_vars overwritten by JT extra_vars](https://github.com/ansible/awx/issues/14445) | 1 |
| ansible/awx | [Inaccurate error handling on Input Group Integer fields (i.e. Org Max Hosts field)](https://github.com/ansible/awx/issues/8556) | 1 |
| ansible/awx | ["Playbook not found for project" error when the playbook exist but is invalid ](https://github.com/ansible/awx/issues/6842) | 1 |
| ansible/django-ansible-base | [Several unordered querysets](https://github.com/ansible/django-ansible-base/issues/178) | 1 |
| tensorflow/agents | [Tutorial 1: Train a Deep Q Network with TF-Agents and the use of a driver](https://github.com/tensorflow/agents/issues/554) | 1 |
| pytorch/ao | [[QAT] Low-bit FSDP all-gather for QAT](https://github.com/pytorch/ao/issues/1224) | 1 |
| pytorch/ao | [[MX | Triton] Create MX matmul op using new `scaled_dot` op in Triton](https://github.com/pytorch/ao/issues/1084) | 1 |
| pytorch/ao | [Add weight tensor-wise scaling for INT8 quantized and mixed-precision training](https://github.com/pytorch/ao/issues/1010) | 1 |
| pytorch/ao | [MoE example ](https://github.com/pytorch/ao/issues/729) | 1 |
| pytorch/ao | [Self compressing neural networks](https://github.com/pytorch/ao/issues/658) | 1 |
| pytorch/data | [Modify `IterKeyZipper` to accept any number (2+) of `IterDataPipe`](https://github.com/pytorch/data/issues/334) | 1 |
| pytorch/examples | [Update all examples to latest versions of pytorch](https://github.com/pytorch/examples/issues/976) | 1 |
| pytorch/examples | [Video classification example](https://github.com/pytorch/examples/issues/895) | 1 |
| pytorch/examples | [Resume will override learning rate on command line.](https://github.com/pytorch/examples/issues/816) | 1 |
| pytorch/examples | [Add nn.SyncBatchNorm in ImageNet example](https://github.com/pytorch/examples/issues/793) | 1 |
| pytorch/examples | [mnist example contains bad practices leading to wrongful results](https://github.com/pytorch/examples/issues/623) | 1 |
| pytorch/examples | [A question about weight initialization of embedding layer.](https://github.com/pytorch/examples/issues/595) | 1 |
| pytorch/examples | [Changes needed to run DCGAN 32x32 ](https://github.com/pytorch/examples/issues/486) | 1 |
| pytorch/examples | [ImageFolder doc should clarify 1. order that images returned in 2. that all classes are concatenated into a single list](https://github.com/pytorch/examples/issues/400) | 1 |
| pytorch/PiPPy | [Support LayoutLM models in HF tests](https://github.com/pytorch/PiPPy/issues/247) | 1 |
| pytorch/text | [torchtext main branch doesn't support pytorch2.0](https://github.com/pytorch/text/issues/2052) | 1 |
| pytorch/torcharrow | [Default aggregation functions delegates to Arrow Compute ](https://github.com/pytorch/torcharrow/issues/53) | 1 |
| pytorch/torchcodec | [Use `TORCH_CHECK` instead of `throw`](https://github.com/pytorch/torchcodec/issues/537) | 1 |
| pytorch/torchtitan | [Ability to train based on epoch](https://github.com/pytorch/torchtitan/issues/613) | 1 |
| pytorch/torchtune | [Make ocrvqa default in the_cauldron_dataset](https://github.com/pytorch/torchtune/issues/1703) | 1 |
| pytorch/xla | [[hard] Op info test for `special.airy_ai`](https://github.com/pytorch/xla/issues/7926) | 1 |
| pytorch/xla | [Op info test for `triangular_solve .. unfold`](https://github.com/pytorch/xla/issues/7541) | 1 |
| pytorch/xla | [Op info test for `nn.functional.pixel_shuffle .. nn.functional.scaled_dot_product_attention`](https://github.com/pytorch/xla/issues/7526) | 1 |
| pytorch/xla | [Op info test for `linalg.matrix_norm`](https://github.com/pytorch/xla/issues/7494) | 1 |
| pytorch/xla | [Op info test for `linalg.lu_factor_ex`](https://github.com/pytorch/xla/issues/7492) | 1 |
| pytorch/xla | [Op info test for `linalg.lu_factor`](https://github.com/pytorch/xla/issues/7491) | 1 |
| pytorch/xla | [Op info test for `kthvalue`](https://github.com/pytorch/xla/issues/7458) | 1 |
| pytorch/xla | [Op info test for `index_reduce`](https://github.com/pytorch/xla/issues/7453) | 1 |
| huggingface/dataset-viewer | [use the `ROW_IDX_COLUMN` constant name instead of copying the value everywhere](https://github.com/huggingface/dataset-viewer/issues/2798) | 2 |
| huggingface/nanotron | [Avoid nested `InheritFromOtherOptimizer`](https://github.com/huggingface/nanotron/issues/267) | 2 |
| huggingface/nanotron | [[Feature] Asyncronous Serialization](https://github.com/huggingface/nanotron/issues/87) | 2 |
| huggingface/nanotron | [[Feature Request] Support Data Streaming for faster training of large models](https://github.com/huggingface/nanotron/issues/45) | 2 |
| huggingface/optimum | [Add all available ONNX models to ORTConfigManager](https://github.com/huggingface/optimum/issues/351) | 2 |
| huggingface/transformers | [[Performance] Tracking open Issues and PRs (pytorch transformers)](https://github.com/huggingface/transformers/issues/12126) | 2 |
| ansible/ansible-documentation | [Link to devel in the various roadmaps](https://github.com/ansible/ansible-documentation/issues/1865) | 2 |
| ansible/ansible-documentation | [Link "see also" sections as recommended in the forum](https://github.com/ansible/ansible-documentation/issues/1200) | 2 |
| ansible/ansible-documentation | [D&I working group Docs Hackfest for inclusive language](https://github.com/ansible/ansible-documentation/issues/812) | 2 |
| ansible/ansible-navigator | [Switch to the use of `pathlib` where possible](https://github.com/ansible/ansible-navigator/issues/697) | 2 |
| ansible/awx | [Add option to force the user to reset its password at first login](https://github.com/ansible/awx/issues/15766) | 2 |
| ansible/awx | [cancelled vs canceled - standardize spelling in codebase](https://github.com/ansible/awx/issues/15177) | 2 |
| ansible/awx | [Empty value in execution_environment should remove selections (ansible.controller.job_template)](https://github.com/ansible/awx/issues/14841) | 2 |
| ansible/awx | [Issue label for incompliance with Ansible](https://github.com/ansible/awx/issues/13272) | 2 |
| ansible/awx | [New credentials type to provide VAULT_ADDR and VAULT_TOKEN env vars](https://github.com/ansible/awx/issues/13117) | 2 |
| ansible/awx | [Expose the value of "Execution Node" as a variable when running a job from Ansible Tower.](https://github.com/ansible/awx/issues/8122) | 2 |
| ansible/awx | [Jobs canceled before starting should not show a "finished" time](https://github.com/ansible/awx/issues/3988) | 2 |
| ansible/awx | [Make Info Metrics more easy to query](https://github.com/ansible/awx/issues/3781) | 2 |
| ansible/awx | [weekly dashboard view does not have sufficient granularity](https://github.com/ansible/awx/issues/3060) | 2 |
| tensorflow/graphics | [Tangential camera distortion/undistortion](https://github.com/tensorflow/graphics/issues/334) | 2 |
| pytorch/ao | [Support for GrokAdamW](https://github.com/pytorch/ao/issues/1032) | 2 |
| pytorch/ao | [Tensor subclass boilerplate can be consolidated](https://github.com/pytorch/ao/issues/710) | 2 |
| pytorch/ao | [[RFC] Intx Tensor Subclasses Quantization](https://github.com/pytorch/ao/issues/439) | 2 |
| pytorch/examples | [word_language_model with torch.nn.modules.transformer](https://github.com/pytorch/examples/issues/1112) | 2 |
| pytorch/examples | [Warning: an output with one or more elements was resized since it had shape[xxxx],]](https://github.com/pytorch/examples/issues/937) | 2 |
| pytorch/examples | [Input type and weight type should be the same](https://github.com/pytorch/examples/issues/599) | 2 |
| pytorch/examples | [please use longer names for variables than 2-3 letter acronyms](https://github.com/pytorch/examples/issues/487) | 2 |
| pytorch/examples | [VAE reconstruction loss (BCE) ](https://github.com/pytorch/examples/issues/460) | 2 |
| pytorch/examples | [Imagenet training extremely low gpu utilization](https://github.com/pytorch/examples/issues/387) | 2 |
| pytorch/PiPPy | [Make RemoteInterpreter use the full implementation of `Interpreter.run`](https://github.com/pytorch/PiPPy/issues/25) | 2 |
| pytorch/pytorch | [torch.fx.Tracer.record_stack_traces is broken in torch 2.4.0](https://github.com/pytorch/pytorch/issues/130861) | 2 |
| pytorch/rl | [[Feature Request] Make sure that all losses work with tensorclasses and regular tensors](https://github.com/pytorch/rl/issues/1062) | 2 |
| pytorch/rl | [[Feature Request] TensorSpec is_in methods should check the dtype of val](https://github.com/pytorch/rl/issues/793) | 2 |
| pytorch/text | [Convert iterator-style raw datasets to map-style raw datasets](https://github.com/pytorch/text/issues/1296) | 2 |
| pytorch/torchchat | [convert_hf_checkpoint only relies on model_name to resolve TransformerArgs](https://github.com/pytorch/torchchat/issues/1179) | 2 |
| pytorch/torchchat | [Slimming down torchchat: Replace replace_attention_with_custom_sdpa_attention() with ET's implementation](https://github.com/pytorch/torchchat/issues/1058) | 2 |
| pytorch/torchtune | [[RFC] Additional chat loss masking strategies](https://github.com/pytorch/torchtune/issues/2261) | 2 |
| pytorch/torchtune | [Move `modules/tokenizers` to be a subdir of `modules/transforms`](https://github.com/pytorch/torchtune/issues/1301) | 2 |
| pytorch/xla | [Op info test for `special.scaled_modified_bessel_k0 .. squeeze`](https://github.com/pytorch/xla/issues/7538) | 2 |
| pytorch/xla | [Op info test for `nn.functional.feature_alpha_dropout .. nn.functional.grid_sample`](https://github.com/pytorch/xla/issues/7521) | 2 |
| pytorch/xla | [Op info test for `linalg.matrix_power`](https://github.com/pytorch/xla/issues/7495) | 2 |
| pytorch/xla | [Op info test for `linalg.ldl_solve`](https://github.com/pytorch/xla/issues/7488) | 2 |
| huggingface/accelerate | [[Community Contributions] examples on distributed inference using 🤗 Accelerate](https://github.com/huggingface/accelerate/issues/3078) | 3 |
| huggingface/huggingface_hub | [Add options to the "delete-cache" command](https://github.com/huggingface/huggingface_hub/issues/1065) | 3 |
| huggingface/optimum-habana | [Add support for max_length in run_generation](https://github.com/huggingface/optimum-habana/issues/472) | 3 |
| huggingface/transfer-learning-conv-ai | [RuntimeError: shape '[-1, 2, 34]' is invalid for input of size 61710](https://github.com/huggingface/transfer-learning-conv-ai/issues/12) | 3 |
| ansible/ansible-documentation | [Incorporate 'shared snippets' for the collection docs into the main rst files](https://github.com/ansible/ansible-documentation/issues/1382) | 3 |
| ansible/awx | [Fix Delinea imports and import test](https://github.com/ansible/awx/issues/14703) | 3 |
| ansible/awx | [Cleanup Job Details. Configure days retention for the particular job entities. ](https://github.com/ansible/awx/issues/14384) | 3 |
| ansible/awx | [Improve user experience of copy pasting FQDNs from jobs](https://github.com/ansible/awx/issues/14354) | 3 |
| ansible/awx | [Non descriptive error when podman is missing](https://github.com/ansible/awx/issues/14341) | 3 |
| ansible/awx | [AWX Credential Create: ssh_key_data fails to detect/sanitize newlines in keys and 500's with no useable output](https://github.com/ansible/awx/issues/14219) | 3 |
| ansible/awx | [Add "nodes" to "Relaunch on" when relaunching jobs after failure - users think it relates to failed tasks and not nodes](https://github.com/ansible/awx/issues/12438) | 3 |
| ansible/awx | [Worker failed to run task awx.main.tasks.system.purge_old_stdout_files](https://github.com/ansible/awx/issues/11903) | 3 |
| ansible/awx | [System Auditors can check list items](https://github.com/ansible/awx/issues/10841) | 3 |
| ansible/awx | [Show more host information in host filter lookup list ](https://github.com/ansible/awx/issues/7853) | 3 |
| ansible/awx | [Inconsistent capitalization across ui-next ](https://github.com/ansible/awx/issues/7037) | 3 |
| ansible/dispatcherd | [Add correct type hinting to @task decorated objects](https://github.com/ansible/dispatcherd/issues/83) | 3 |
| tensorflow/addons | [Benchmark test for rrelu fails on windows](https://github.com/tensorflow/addons/issues/839) | 3 |
| tensorflow/graphics | [Add skew to projective camera](https://github.com/tensorflow/graphics/issues/335) | 3 |
| tensorflow/model-card-toolkit | [Prefer single quote strings model-card-toolkit](https://github.com/tensorflow/model-card-toolkit/issues/279) | 3 |
| tensorflow/similarity | [Add a ranking example](https://github.com/tensorflow/similarity/issues/199) | 3 |
| pytorch/ao | [[sparse] Add GPTQ support for sparse-marlin](https://github.com/pytorch/ao/issues/1134) | 3 |
| pytorch/ao | [Tensor Parallelism Support for AffineQuantizedTensor](https://github.com/pytorch/ao/issues/988) | 3 |
| pytorch/ao | [[llama] Use horizontal fusion trick from Attention for FeedForward](https://github.com/pytorch/ao/issues/606) | 3 |
| pytorch/data | [`scan` support](https://github.com/pytorch/data/issues/1110) | 3 |
| pytorch/examples | [OSError: [Errno 22] Invalid argument:](https://github.com/pytorch/examples/issues/887) | 3 |
| pytorch/examples | [MNIST test_loader not being used as intended (wrong)!](https://github.com/pytorch/examples/issues/756) | 3 |
| pytorch/examples | [Actor critic example not using discount rate properly](https://github.com/pytorch/examples/issues/744) | 3 |
| pytorch/examples | ["omit freeze_support"](https://github.com/pytorch/examples/issues/323) | 3 |
| pytorch/pytorch | [Remove tensor variable default method fallthrough](https://github.com/pytorch/pytorch/issues/140591) | 3 |
| pytorch/pytorch | [[export] Schematize nn_module_stack serialization](https://github.com/pytorch/pytorch/issues/131941) | 3 |
| pytorch/pytorch | [Expand Tag Set: views & reductions](https://github.com/pytorch/pytorch/issues/129020) | 3 |
| pytorch/torchchat | [[UX] We are too quiet about errors - in particular missing HF authentication...](https://github.com/pytorch/torchchat/issues/782) | 3 |
| pytorch/torchdistx | [Documentation for AnyPrecisionOptimizer](https://github.com/pytorch/torchdistx/issues/61) | 3 |
| pytorch/torchtune | [Add add_end_token to Mistral tokenizer](https://github.com/pytorch/torchtune/issues/2479) | 3 |
| pytorch/torchtune | [implement activation offloading and opt_in_bwd in knowledge_distillation recipes](https://github.com/pytorch/torchtune/issues/1959) | 3 |
| pytorch/xla | [[scan] Avoid re-tracing the combine function on every call](https://github.com/pytorch/xla/issues/8632) | 3 |
| pytorch/xla | [Op info test for `pinverse .. put`](https://github.com/pytorch/xla/issues/7529) | 3 |
| pytorch/xla | [Op info test for `nn.functional.leaky_relu .. nn.functional.max_pool1d`](https://github.com/pytorch/xla/issues/7523) | 3 |
| xbmc/addon-check | [Correct the mentioned pylint errors to get perfect 10. (missing-docstring)](https://github.com/xbmc/addon-check/issues/179) | 3 |
| godotengine/godot-blender-exporter | [Blender object with negative scale](https://github.com/godotengine/godot-blender-exporter/issues/24) | 3 |
| huggingface/accelerate | [Barebones dataloader to allow for any type of iterable dataloader-like object to be used. Should just handle device placement](https://github.com/huggingface/accelerate/issues/2975) | 4 |
| huggingface/lighteval | [[EVAL]: Add more African Benchmarks](https://github.com/huggingface/lighteval/issues/373) | 4 |
| huggingface/lighteval | [Append revision to filepath in `--output_dir`?](https://github.com/huggingface/lighteval/issues/56) | 4 |
| huggingface/transformers | [OWL-VIT Vision Foundation Model deployment in the edge cases - Need SDPA support for OWL-ViT Model optimization for Edge Deployment](https://github.com/huggingface/transformers/issues/28103) | 4 |
| huggingface/transformers | [GeneratorExp aren't supported by torch.jit.script when I try to export a previously trained model  'google/vit-base-patch16-224-in21k'.](https://github.com/huggingface/transformers/issues/15354) | 4 |
| pandas-dev/pandas-stubs | [Type checking with `converters=` on `read_excel`](https://github.com/pandas-dev/pandas-stubs/issues/849) | 4 |
| ansible/awx | [ visualizer info field ](https://github.com/ansible/awx/issues/14597) | 4 |
| ansible/awx | [Remove some of the eslint-disable comments](https://github.com/ansible/awx/issues/11707) | 4 |
| ansible/awx | [Docker install instructions do not mention how to add awx-logos](https://github.com/ansible/awx/issues/11593) | 4 |
| tensorflow/graphics | [Add ScanNet dataset](https://github.com/tensorflow/graphics/issues/307) | 4 |
| pytorch/ao | [Quantized Training](https://github.com/pytorch/ao/issues/554) | 4 |
| pytorch/examples | [Please change dcgan to load truncated images.](https://github.com/pytorch/examples/issues/835) | 4 |
| pytorch/examples | [No matching function call  error in custom_dataset example ](https://github.com/pytorch/examples/issues/680) | 4 |
| pytorch/examples | [Add Siamese Network example](https://github.com/pytorch/examples/issues/645) | 4 |
| pytorch/pytorch | [[Inductor] Inference failed with the compiled model with aminmax operator](https://github.com/pytorch/pytorch/issues/148808) | 4 |
| pytorch/pytorch | [Improve error message for wrong number of arguments in CachingAutotuner](https://github.com/pytorch/pytorch/issues/146018) | 4 |
| pytorch/pytorch | [If mark_dynamic fails (Not all values of RelaxedUnspecConstraint are valid) due to specialization, error message should print where specialization came from](https://github.com/pytorch/pytorch/issues/136002) | 4 |
| pytorch/pytorch | [Dead link in `torch.compile` docs](https://github.com/pytorch/pytorch/issues/119272) | 4 |
| pytorch/rl | [[Feature Request] Missing ActionScaling and FlattenAction ](https://github.com/pytorch/rl/issues/1209) | 4 |
| pytorch/torchft | [Use bucketized model averaging for LocalSGD](https://github.com/pytorch/torchft/issues/66) | 4 |
| pytorch/xla | [Op info test for `nn.functional.avg_pool1d .. nn.functional.bilinear`](https://github.com/pytorch/xla/issues/7517) | 4 |
| pytorch/xla | [Op info test for `linalg.lu_solve`](https://github.com/pytorch/xla/issues/7493) | 4 |
| pytorch/xla | [[HARD] Op info test for `linalg.det`](https://github.com/pytorch/xla/issues/7478) | 4 |
| huggingface/huggingface_hub | [Implement a `FlaxModelHubMixin`](https://github.com/huggingface/huggingface_hub/issues/1709) | 5 |
| huggingface/nanotron | [[Unit Test] Add unit tests for DistributedTrainer](https://github.com/huggingface/nanotron/issues/90) | 5 |
| huggingface/optimum-benchmark | [Evaluators for specific tasks](https://github.com/huggingface/optimum-benchmark/issues/34) | 5 |
| huggingface/transformers | [Add argument to set number of eval steps in Trainer](https://github.com/huggingface/transformers/issues/31561) | 5 |
| pandas-dev/pandas-stubs | [Addition of a Series[int] with a complex returns Series[unknown]](https://github.com/pandas-dev/pandas-stubs/issues/1098) | 5 |
| ansible/awx | [ adhoc jobs block other jobs from being processed in the queue](https://github.com/ansible/awx/issues/14645) | 5 |
| ansible/awx | [all cluster nodes in development environment have the same UUID](https://github.com/ansible/awx/issues/13029) | 5 |
| tensorflow/graphics | [Not detecting TF Nightly when installing from whl.](https://github.com/tensorflow/graphics/issues/305) | 5 |
| tensorflow/similarity | [Implement multi-siam for segmentation](https://github.com/tensorflow/similarity/issues/179) | 5 |
| pytorch/ao | [[low-bit optim] Add COAT optimizer](https://github.com/pytorch/ao/issues/1190) | 5 |
| pytorch/ao | [The next tutorials](https://github.com/pytorch/ao/issues/426) | 5 |
| pytorch/audio | [read mp3 file fail](https://github.com/pytorch/audio/issues/2867) | 5 |
| pytorch/pytorch | [torch._dynamo.exc.Unsupported: builtin: bool [<class 'torch._dynamo.variables.tensor.SymNodeVariable'>] False](https://github.com/pytorch/pytorch/issues/136075) | 5 |
| pytorch/pytorch | [dynamo (re)compilation issues: shape (1,1), nn.Parameter, mark_dynamic](https://github.com/pytorch/pytorch/issues/135011) | 5 |
| pytorch/pytorch | [AOTAutograd: functionalization should emit foreach_copy_() instead of copy_() when possible](https://github.com/pytorch/pytorch/issues/119191) | 5 |
| pytorch/torchft | [[CheckpointServer] use streaming transfers](https://github.com/pytorch/torchft/issues/36) | 5 |
| pytorch/xla | [xb.Op.scalar maps unsigned int to torch signed int](https://github.com/pytorch/xla/issues/8798) | 5 |
| huggingface/transformers | [FSDP Torch XLA vs. FSDPv2 (SMPD) Torch XLA checkpoint saving bug](https://github.com/huggingface/transformers/issues/36004) | 6 |
| huggingface/transformers | [oom when using adafactor optimizer in deepspeed](https://github.com/huggingface/transformers/issues/33290) | 6 |
| huggingface/transformers | [Add TableTransformerImageProcessor](https://github.com/huggingface/transformers/issues/30718) | 6 |
| pandas-dev/pandas | [startingMonth ignored on non-unitary Quarter periods](https://github.com/pandas-dev/pandas/issues/29576) | 6 |
| pandas-dev/pandas | [BUG: Creating Index name using `names` names argument, doesn't set index name](https://github.com/pandas-dev/pandas/issues/19082) | 6 |
| ansible/ansible-navigator | [Allow to set ansible-runner artifacts dir ID ](https://github.com/ansible/ansible-navigator/issues/521) | 6 |
| ansible/awx | [AWX Collection Credential Delete](https://github.com/ansible/awx/issues/14209) | 6 |
| tensorflow/similarity | [Create a colab for single shot to demonstrate how augmenters works](https://github.com/tensorflow/similarity/issues/74) | 6 |
| pytorch/examples | [DCGAN C++ warning after PyTorch update](https://github.com/pytorch/examples/issues/819) | 6 |
| pytorch/ignite | [Improve metrics tests](https://github.com/pytorch/ignite/issues/3335) | 6 |
| pytorch/pytorch | [torch.nn.InstanceNorm2d throws "mixed dtype" error with track_running_stats set to True](https://github.com/pytorch/pytorch/issues/139140) | 6 |
| pytorch/pytorch | [Docs are little bit outdated for torch logs](https://github.com/pytorch/pytorch/issues/137285) | 6 |
| huggingface/datasets | [Identical keywords in build_kwargs and config_kwargs lead to TypeError in load_dataset_builder()](https://github.com/huggingface/datasets/issues/4910) | 7 |
| huggingface/datasets | [WMT21 & WMT22](https://github.com/huggingface/datasets/issues/4709) | 7 |
| huggingface/diffusers | [Use of requests call without `timeout` parameter](https://github.com/huggingface/diffusers/issues/7730) | 7 |
| huggingface/huggingface_hub | [[Community event] Translate documentation to your own langage](https://github.com/huggingface/huggingface_hub/issues/1700) | 7 |
| pandas-dev/pandas | [DOC: `.str.cat` output in case of `Index` object](https://github.com/pandas-dev/pandas/issues/35556) | 7 |
| tensorflow/similarity | [Implement SwAV for self-supervised learning](https://github.com/tensorflow/similarity/issues/208) | 7 |
| pytorch/audio | [Use non-persistent buffers](https://github.com/pytorch/audio/issues/3059) | 7 |
| pytorch/examples | [Why don't we use MSE as a reconstruction loss for VAE ?](https://github.com/pytorch/examples/issues/399) | 7 |
| pytorch/pytorch | [[BUG][PyTorch 2.0 Export][quant]:get_source_partitions() may return different matches with same input graph](https://github.com/pytorch/pytorch/issues/147170) | 7 |
| pytorch/pytorch | [`_amp_foreach_non_finite_check_and_unscale_` can be torch.compiled inside torch.amp, but not in identical code outside it](https://github.com/pytorch/pytorch/issues/138412) | 7 |
| pytorch/pytorch | [bmm, topk, cholesky, linalg.norm, max with out variants set causing recompilations in torch.compile](https://github.com/pytorch/pytorch/issues/135859) | 7 |
| pytorch/pytorch | [[Dynamo] Support tracing through _get_current_dispatch_mode_stack](https://github.com/pytorch/pytorch/issues/125694) | 7 |
| pytorch/pytorch | [Obscure error: Expected a value of type 'List[int]' for argument 'sizes' but instead found type 'immutable_list'](https://github.com/pytorch/pytorch/issues/122129) | 7 |
| huggingface/diffusers | [[Flux ControlNet] Add support for de-distilled models with CFG](https://github.com/huggingface/diffusers/issues/9635) | 8 |
| huggingface/diffusers | [Support multiple control nets in the `StableDiffusionControlNetXSPipeline`/`StableDiffusionXLControlNetXSPipeline`](https://github.com/huggingface/diffusers/issues/8434) | 8 |
| huggingface/diffusers | [Make `FlaxLMSDiscreteScheduler` jittable](https://github.com/huggingface/diffusers/issues/2180) | 8 |
| huggingface/transformers | [Custom 4D tensor caused shape mismatch error](https://github.com/huggingface/transformers/issues/35290) | 8 |
| pandas-dev/pandas | [TST: Make test_sql.py parallelizable](https://github.com/pandas-dev/pandas/issues/60378) | 8 |
| pandas-dev/pandas | [DOC: Reindexing behaviour of dataframe column-assignment missing](https://github.com/pandas-dev/pandas/issues/39845) | 8 |
| ansible/awx | [Display SAML login icon for /api/login page](https://github.com/ansible/awx/issues/12905) | 8 |
| pytorch/pytorch | [Device check missing in torch.linalg.solve_triangular leading to hard crash](https://github.com/pytorch/pytorch/issues/142048) | 8 |
| pytorch/pytorch | [Dump bytecode of resumption frames in tlparse](https://github.com/pytorch/pytorch/issues/136038) | 8 |
| pytorch/pytorch | [Triton tl.reinterpret is not Dynamo traceable](https://github.com/pytorch/pytorch/issues/133253) | 8 |
| pytorch/pytorch | [Using an empty tensor and `torch.int64` or `torch.bool` for `dtype` of `nanmean()` works while a non-empty tensor doesn't work](https://github.com/pytorch/pytorch/issues/131043) | 8 |
| huggingface/huggingface_hub | [Allow dry_run for snapshot_download](https://github.com/huggingface/huggingface_hub/issues/1023) | 9 |
| pandas-dev/pandas | [Information for new contributors](https://github.com/pandas-dev/pandas/issues/49275) | 9 |
| pandas-dev/pandas | [DOC: Fix formatting errors in docstrings](https://github.com/pandas-dev/pandas/issues/27977) | 9 |
| fastapi/fastapi | [Dependency Models created from Form input data are loosing metadata(field set) and are enforcing validation on default values.](https://github.com/fastapi/fastapi/issues/13399) | 9 |
| tensorflow/similarity | [Lifted Structured loss](https://github.com/tensorflow/similarity/issues/102) | 9 |
| pytorch/pytorch | [[inductor] `torch.slice_scatter` throws `AssertionError` when meeting internal `float32`](https://github.com/pytorch/pytorch/issues/147842) | 9 |
| pytorch/pytorch | [broken `torch.compile` with `"meta"` device tensors](https://github.com/pytorch/pytorch/issues/144607) | 9 |
| pytorch/pytorch | [Use expecttest in test_compiled_optimizers.py](https://github.com/pytorch/pytorch/issues/141262) | 9 |
| huggingface/datasets | [Consider using "Sequence" instead of "List"](https://github.com/huggingface/datasets/issues/5354) | 10 |
| huggingface/diffusers | [flux img2img controlnet channels error](https://github.com/huggingface/diffusers/issues/9979) | 10 |
| huggingface/transformers | [MultiTask Classification and label_names on Trainer](https://github.com/huggingface/transformers/issues/33193) | 10 |
| huggingface/transformers | [Tapas tokenization Different from Tensorflow Code](https://github.com/huggingface/transformers/issues/13244) | 10 |
| pandas-dev/pandas | [DOC: Simplify pandas theme footer](https://github.com/pandas-dev/pandas/issues/51536) | 10 |
| pandas-dev/pandas | [DOC: use shared_docs for isna/notna & isnull/notnull](https://github.com/pandas-dev/pandas/issues/17096) | 10 |
| pytorch/ao | [[MPS] torchao low-bit-precision optim does not expose 'backend' argument to torch.compile](https://github.com/pytorch/ao/issues/955) | 10 |
| pytorch/pytorch | [Improve typing of args and kwargs with ParamSpec](https://github.com/pytorch/pytorch/issues/142306) | 10 |
| pytorch/pytorch | [Logging when executing fx.Interpreter](https://github.com/pytorch/pytorch/issues/117351) | 10 |
| huggingface/transformers | [[trainer] figuring out why eval with `--fp16_full_eval` is 25% slower](https://github.com/huggingface/transformers/issues/10816) | 11 |
| pandas-dev/pandas | [BUG: CustomBusinessDay not respecting calendar](https://github.com/pandas-dev/pandas/issues/60647) | 11 |
| pandas-dev/pandas | [BUG: read_sql no longer works simply with SqlAlchemy selectables and a quick fix](https://github.com/pandas-dev/pandas/issues/35484) | 11 |
| pandas-dev/pandas-stubs | [type annotation for Index/MultiIndex.names is incorrect](https://github.com/pandas-dev/pandas-stubs/issues/804) | 11 |
| tensorflow/quantum | [[Performance] Boost tfq.convert_to_tensor speed](https://github.com/tensorflow/quantum/issues/336) | 11 |
| pytorch/ao | [Named Symbol not found (torchchat #1298)](https://github.com/pytorch/ao/issues/1110) | 11 |
| pytorch/data | [Improve the warning message regarding local function not supported by pickle](https://github.com/pytorch/data/issues/947) | 11 |
| huggingface/transformers | [Verify interpolation of image processors](https://github.com/huggingface/transformers/issues/28180) | 12 |
| pandas-dev/pandas | [Updating value of a single row of a column using loc or at fails](https://github.com/pandas-dev/pandas/issues/22040) | 12 |
| pandas-dev/pandas | [issue when shifting with Timedelta in a groupby](https://github.com/pandas-dev/pandas/issues/20492) | 12 |
| huggingface/diffusers | [[Pipeline] AnimateDiff + SparseControl + ControlNet](https://github.com/huggingface/diffusers/issues/9329) | 13 |
| huggingface/transformers | [IsADirectoryError when training with tqdm enabled for trainer](https://github.com/huggingface/transformers/issues/34766) | 13 |
| huggingface/transformers | [Object Detection Pipeline only outputs first element when batching](https://github.com/huggingface/transformers/issues/31356) | 13 |
| pandas-dev/pandas | [ENH/API: allow different values for labels/index in DF.reindex __OR__ raise error](https://github.com/pandas-dev/pandas/issues/21685) | 13 |
| pytorch/pytorch | [Update triton_heuristics.py](https://github.com/pytorch/pytorch/pull/147690) | 13 |
| huggingface/peft | [Comparison of Different Fine-Tuning Techniques for Conversational AI](https://github.com/huggingface/peft/issues/2310) | 14 |
| huggingface/datasets | [FolderBase Dataset automatically resolves under current directory when data_dir is not specified](https://github.com/huggingface/datasets/issues/6152) | 15 |
| huggingface/datasets | [Return the name of the currently loaded file in the load_dataset function.](https://github.com/huggingface/datasets/issues/5806) | 15 |
| pandas-dev/pandas | [BUG: `DataFrame.to_parquet` doesn't round-trip pyarrow StringDtype](https://github.com/pandas-dev/pandas/issues/42664) | 15 |
| pandas-dev/pandas | [DOC: improve docs for broadcasting behavior](https://github.com/pandas-dev/pandas/issues/18857) | 15 |
| huggingface/diffusers | [refactors pipelines inheriting from `StableDiffusionPipeline`](https://github.com/huggingface/diffusers/issues/6984) | 16 |
| huggingface/transformers | [Follow ups to DocumentQuestionAnswering Pipeline](https://github.com/huggingface/transformers/issues/18926) | 16 |
| pandas-dev/pandas | [DOC: add button to edit on GitHub](https://github.com/pandas-dev/pandas/issues/39859) | 16 |
| pandas-dev/pandas | [WEB: Multiple "Getting Started" on pandas.io leads to different links](https://github.com/pandas-dev/pandas/issues/32307) | 16 |
| pandas-dev/pandas | [Indexing on series where index is output from pd.cut ](https://github.com/pandas-dev/pandas/issues/27437) | 16 |
| fastapi/fastapi | [Will FastAPI support QUERY http method? "app.query"](https://github.com/fastapi/fastapi/issues/12965) | 16 |
| pytorch/pytorch | [Supporting custom attributes with `__torch_function__` tensor subclasses](https://github.com/pytorch/pytorch/issues/117806) | 16 |
| pytorch/torchtune | [[Clean up] Move evaluation configs under model directories ](https://github.com/pytorch/torchtune/issues/1810) | 16 |
| pandas-dev/pandas | [DOC: Generating docs doesn't work if path has whitespaces](https://github.com/pandas-dev/pandas/issues/22836) | 17 |
| pytorch/ao | [Replace flash_4 with FlexAttention](https://github.com/pytorch/ao/issues/639) | 17 |
| huggingface/transformers | [Update no_trainer scripts to include gradient accumulation](https://github.com/huggingface/transformers/issues/18436) | 18 |
| pytorch/ao | [Add codebook (look up table based) quantization flow in torchao](https://github.com/pytorch/ao/issues/1195) | 18 |
| pytorch/audio | [Add Stereo to Mono Convertions](https://github.com/pytorch/audio/issues/877) | 18 |
| huggingface/diffusers | [Expanded init fields in StableDiffusionPipeline cause incompatibilities with many/most inherited pipelines](https://github.com/huggingface/diffusers/issues/6969) | 19 |
| huggingface/transformers | [trainer resume from checkpoint，the learning rate is not the same as retraining,learning rate is discontinuous](https://github.com/huggingface/transformers/issues/34053) | 19 |
| huggingface/transformers | [Accelerate x Trainer issue tracker:](https://github.com/huggingface/transformers/issues/33345) | 19 |
| huggingface/transformers | [Improve EncoderDecoderModel docs](https://github.com/huggingface/transformers/issues/16135) | 19 |
| huggingface/transformers | [how to use EncoderDecoderModel to do en-de translation?](https://github.com/huggingface/transformers/issues/8944) | 19 |
| pandas-dev/pandas | [TST: mixed_int_string Index](https://github.com/pandas-dev/pandas/issues/54072) | 19 |
| pandas-dev/pandas | [Fix PR02 issues in docstrings](https://github.com/pandas-dev/pandas/issues/27976) | 19 |
| ansible/ansible-documentation | [add documentation for fallible](https://github.com/ansible/ansible-documentation/issues/1868) | 19 |
| pandas-dev/pandas | [Raise ValueError for read_json and orient='table' With Numeric Column Names](https://github.com/pandas-dev/pandas/issues/19129) | 20 |
| pandas-dev/pandas | [BUG: groupby.sum() is inconsistent with df.sum() for large integers](https://github.com/pandas-dev/pandas/issues/34681) | 21 |
| pandas-dev/pandas | [DOC: Single Document For Code Guidelines](https://github.com/pandas-dev/pandas/issues/33851) | 21 |
| huggingface/transformers | [Export LayoutLMv2 to onnx ](https://github.com/huggingface/transformers/issues/14368) | 24 |
| huggingface/optimum | [Community contribution - `BetterTransformer` integration for more models!](https://github.com/huggingface/optimum/issues/488) | 25 |
| huggingface/transformers | [Add support for BLIP and GIT in image-to-text and VQA pipelines](https://github.com/huggingface/transformers/issues/21110) | 25 |
| huggingface/transformers | [Getting time offsets of beginning and end of each word in Wav2Vec2](https://github.com/huggingface/transformers/issues/11307) | 25 |
| pandas-dev/pandas | [CLN: Use dedup_names in all instances where duplicate column names are renamed](https://github.com/pandas-dev/pandas/issues/50371) | 26 |
| pytorch/torchchat | [Multimodal Eval Enablement (Looking for Developer to Implement Design)](https://github.com/pytorch/torchchat/issues/1334) | 26 |
| huggingface/diffusers | [[Community Pipelines]](https://github.com/huggingface/diffusers/issues/841) | 27 |
| pandas-dev/pandas | [DOC: fix docstring validation errors for `pandas.Timestamp`](https://github.com/pandas-dev/pandas/issues/59458) | 28 |
| pytorch/ignite | [🥇 Everyone is welcome to contribute 💯 ](https://github.com/pytorch/ignite/issues/2026) | 28 |
| pandas-dev/pandas | [DOC: Fix docs for various offset constructors](https://github.com/pandas-dev/pandas/issues/52431) | 29 |
| huggingface/transformers | [Trying to add support for GPT2 as decoder in EncoderDecoder model](https://github.com/huggingface/transformers/issues/4483) | 31 |
| pandas-dev/pandas | [DOC: Additional items for the cheat sheet](https://github.com/pandas-dev/pandas/issues/40680) | 39 |
| huggingface/transformers | [Community contribution: enable dynamic resolution input for more vision models.](https://github.com/huggingface/transformers/issues/30579) | 40 |
| pandas-dev/pandas | [Various methods don't call call __finalize__](https://github.com/pandas-dev/pandas/issues/28283) | 48 |
| pytorch/examples | [New examples requested](https://github.com/pytorch/examples/issues/1131) | 48 |
| fastapi/fastapi | [ApiKey Header documentation](https://github.com/fastapi/fastapi/issues/142) | 52 |
| huggingface/transformers | [[Community Event] Doc Tests Sprint](https://github.com/huggingface/transformers/issues/16292) | 104 |

### Rust

| Repo | Title | Comments |
| --- | --- | --- |
| huggingface/ratchet | [Reduce dependencies! 🗡️](https://github.com/huggingface/ratchet/issues/170) | 0 |
| tensorflow/rust | [Add Scope::with_kernel_label and with_xla_cluster](https://github.com/tensorflow/rust/issues/288) | 3 |
| tensorflow/rust | [Add OpArgDef::default_value and allowed_values](https://github.com/tensorflow/rust/issues/290) | 7 |

### SCSS

| Repo | Title | Comments |
| --- | --- | --- |
| godotengine/discourse-theme | [Change default `green` to our own green for the Solved questions](https://github.com/godotengine/discourse-theme/issues/14) | 0 |
| godotengine/discourse-theme | [Make tag and tag count more distinct](https://github.com/godotengine/discourse-theme/issues/11) | 0 |
| godotengine/discourse-theme | [Categories are not rounded on mobile](https://github.com/godotengine/discourse-theme/issues/3) | 0 |
| godotengine/discourse-theme | [Search bar should not cover full width on mobile](https://github.com/godotengine/discourse-theme/issues/2) | 0 |
| godotengine/discourse-theme | [Remove the "Sign Up" button from navbar](https://github.com/godotengine/discourse-theme/issues/15) | 2 |

### Swift

| Repo | Title | Comments |
| --- | --- | --- |

| tensorflow/swift-apis | [[summary] Better formatting](https://github.com/tensorflow/swift-apis/issues/1075) | 0 |
| tensorflow/swift-apis | [Lift Tensor.dimensionGathering() out of swift-models and into swift-apis](https://github.com/tensorflow/swift-apis/issues/1058) | 0 |
| tensorflow/swift-apis | [Investigate size/performance tradeoffs for `-sil-inline-generics` and `-sil-partial-specialization`](https://github.com/tensorflow/swift-apis/issues/628) | 0 |
| tensorflow/swift-apis | [Update doc comments on non-mutating API to use proper wording.](https://github.com/tensorflow/swift-apis/issues/160) | 0 |
| huggingface/sam2-studio | [Model download selector](https://github.com/huggingface/sam2-studio/issues/28) | 1 |
| huggingface/chat-macOS | [[Feature Request] System Prompt Support](https://github.com/huggingface/chat-macOS/issues/35) | 2 |
| huggingface/chat-macOS | [Asking "what time is it?" will always return the local time of Paris, regardless of your location (⌘R+)](https://github.com/huggingface/chat-macOS/issues/7) | 2 |
| tensorflow/swift-apis | [Recursive Neural Networks (structured data/trees)](https://github.com/tensorflow/swift-apis/issues/68) | 3 |
| huggingface/chat-macOS | [Add custom LLM API ](https://github.com/huggingface/chat-macOS/issues/18) | 5 |
| huggingface/swift-transformers | [Tokenizers: additional Normalizers, PreTokenizers, PostProcessors](https://github.com/huggingface/swift-transformers/issues/4) | 5 |
| tensorflow/swift-apis | [Implement Recurrent Layers](https://github.com/tensorflow/swift-apis/issues/52) | 5 |
| tensorflow/swift-apis | [some mutating tensor operations are not @differentiable](https://github.com/tensorflow/swift-apis/issues/1048) | 7 |
| tensorflow/swift-apis | [Add derivative tests for layers](https://github.com/tensorflow/swift-apis/issues/402) | 7 |
| tensorflow/swift-apis | [Adding Test Cases for Layers in Layer.swift file](https://github.com/tensorflow/swift-apis/issues/77) | 7 |
| tensorflow/swift-apis | [Support Advanced Layers](https://github.com/tensorflow/swift-apis/issues/685) | 8 |
| tensorflow/swift-apis | [Swifty API discovery via '@available' on raw APIs.](https://github.com/tensorflow/swift-apis/issues/483) | 8 |
| tensorflow/swift-apis | [Add preconditions](https://github.com/tensorflow/swift-apis/issues/517) | 10 |
| huggingface/swift-transformers | [Support for embedding models (BGE, GTE etc)](https://github.com/huggingface/swift-transformers/issues/22) | 12 |
| tensorflow/swift-apis | [Add more optimizers and losses](https://github.com/tensorflow/swift-apis/issues/127) | 16 |
| huggingface/swift-transformers | [Convert OpenELM to float16 Core ML](https://github.com/huggingface/swift-transformers/issues/95) | 17 |
| huggingface/sam2-studio | [Video support estimated release date?](https://github.com/huggingface/sam2-studio/issues/25) | 21 |

### TypeScript

| Repo | Title | Comments |
| --- | --- | --- |

| ansible/vscode-ansible | [Add option to prefix all shell commands the plugin executes](https://github.com/ansible/vscode-ansible/issues/429) | 0 |
| tensorflow/tfjs-tsne | [Implement tensorToDataTexture in the GPU](https://github.com/tensorflow/tfjs-tsne/issues/10) | 0 |
| pytorch/test-infra | [Better highlight scheme for force merges](https://github.com/pytorch/test-infra/issues/5229) | 0 |
| huggingface/chat-ui | [Chrome app icon on macOS](https://github.com/huggingface/chat-ui/issues/1439) | 1 |
| huggingface/chat-ui | [Add support for non streaming TGI endpoints](https://github.com/huggingface/chat-ui/issues/339) | 1 |
| pytorch/probot | [deprecation of `number` for octokit](https://github.com/pytorch/probot/issues/62) | 1 |
| huggingface/chat-ui | [Add option for users to customize search engines in settings page](https://github.com/huggingface/chat-ui/issues/1756) | 2 |
| huggingface/huggingface.js | [Maximize button not working properly on Hosted inference API block](https://github.com/huggingface/huggingface.js/issues/335) | 2 |
| huggingface/Mongoku | [Auto-link ObjectIds to their referenced elements in the same DB](https://github.com/huggingface/Mongoku/issues/86) | 2 |
| huggingface/chat-ui | [Load past conversations using the most recent leaf to determine the visible conversation tree.](https://github.com/huggingface/chat-ui/issues/1208) | 3 |
| huggingface/chat-ui | [System prompt not taken into account when web browsing.](https://github.com/huggingface/chat-ui/issues/1159) | 3 |
| ansible/vscode-ansible | [Option to completely disable autocomplete](https://github.com/ansible/vscode-ansible/issues/837) | 3 |
| huggingface/chat-ui | [Disabling Reasoning Summary as an Env Option](https://github.com/huggingface/chat-ui/issues/1720) | 4 |
| huggingface/chat-ui | [Explore the possibility for chat-ui to use OpenAI assistants API structure.](https://github.com/huggingface/chat-ui/issues/838) | 4 |
| pytorch/test-infra | [A better HUD menu for PyTorch repos family](https://github.com/pytorch/test-infra/issues/5226) | 4 |
| huggingface/chat-ui | [Support text-generation-webui](https://github.com/huggingface/chat-ui/issues/316) | 5 |
| huggingface/huggingface.js | [Add threshold parameter for object detection widget](https://github.com/huggingface/huggingface.js/issues/322) | 5 |
| tensorflow/profiler | [Tensorboard profiler not working well with data from gcs bucket?](https://github.com/tensorflow/profiler/issues/372) | 5 |
| pytorch/test-infra | [Mergebot merged a PR even though a review had been re-requested](https://github.com/pytorch/test-infra/issues/5543) | 5 |
| huggingface/chat-ui | [Have embedded prompts configurable in private secrets](https://github.com/huggingface/chat-ui/issues/346) | 7 |
| huggingface/huggingface.js | [Tracking integration for Video Classification](https://github.com/huggingface/huggingface.js/issues/332) | 8 |
| huggingface/huggingface.js | [Integration with the /api/collections endpoint? ](https://github.com/huggingface/huggingface.js/issues/271) | 9 |
| huggingface/chat-ui | [Current Date Issue](https://github.com/huggingface/chat-ui/issues/284) | 11 |

### None

| Repo | Title | Comments |
| --- | --- | --- |

| huggingface/awesome-huggingface | [[hacktoberfest] Hugging Face Collections Hacktoberfest challenge](https://github.com/huggingface/awesome-huggingface/issues/28) | 0 |
| tensorflow/mlir | [Implement support for qualified symbols](https://github.com/tensorflow/mlir/issues/186) | 0 |
| tensorflow/mlir | [Consider trip count in loop invariant code motion](https://github.com/tensorflow/mlir/issues/194) | 4 |
| tensorflow/mlir | [[LLVM] Implement missing LLVM IR instructions](https://github.com/tensorflow/mlir/issues/276) | 11 |

### reStructuredText

| Repo | Title | Comments |
| --- | --- | --- |

| godotengine/godot-docs | [Add C# examples for custom BBCode](https://github.com/godotengine/godot-docs/issues/9334) | 0 |
| godotengine/godot-docs | [Document that C# `string`s are UTF16 while Godot `String`s are UTF32](https://github.com/godotengine/godot-docs/issues/7682) | 0 |
| godotengine/godot-docs | [Curve2D.get_closest_point() incorrectly documented](https://github.com/godotengine/godot-docs/issues/5894) | 0 |
| godotengine/godot-docs | [Physics2DDirectSpaceState does not specify local or global coordinates](https://github.com/godotengine/godot-docs/issues/3299) | 0 |
| godotengine/godot-docs | [Incorrect note on Reflection probes page](https://github.com/godotengine/godot-docs/issues/10493) | 1 |
| godotengine/godot-docs | [Animated gif has visual artifacts](https://github.com/godotengine/godot-docs/issues/10425) | 1 |
| godotengine/godot-docs | [Viewport "use_hdr_2d" documentation point unclear](https://github.com/godotengine/godot-docs/issues/10044) | 1 |
| godotengine/godot-docs | [MultiMesh resource buffer description](https://github.com/godotengine/godot-docs/issues/9891) | 1 |
| godotengine/godot-docs | [Parallax2D property descriptions do not specify units](https://github.com/godotengine/godot-docs/issues/9715) | 1 |
| godotengine/godot-docs | [Improve ArrayMesh examples by adding a rectangle example](https://github.com/godotengine/godot-docs/issues/9620) | 1 |
| godotengine/godot-docs | [Specify the coordinate system for the 'force' parameter in Rigidbody apply_force methods](https://github.com/godotengine/godot-docs/issues/9066) | 1 |
| godotengine/godot-docs | [make_canvas_position_local](https://github.com/godotengine/godot-docs/issues/8313) | 1 |
| godotengine/godot-docs | [Inconsistent code example between PhysicsShapeQueryParameters3D and PhysicsServer3D](https://github.com/godotengine/godot-docs/issues/8305) | 1 |
| godotengine/godot-docs | [Rewording/amendment for Camera2D.align () function.](https://github.com/godotengine/godot-docs/issues/7307) | 1 |
| godotengine/godot-docs | [AudioServer Documentation does not specify units of time](https://github.com/godotengine/godot-docs/issues/7009) | 1 |
| godotengine/godot-docs | [Add clarification about what CharacterBody is used for](https://github.com/godotengine/godot-docs/issues/10458) | 2 |
| godotengine/godot-docs | [PhysicsDirectSpaceState2D.get_rest_info claims not to use query motion but it does](https://github.com/godotengine/godot-docs/issues/10609) | 3 |
| godotengine/godot-docs | [WorkerThreadPool docs do not specify how Thread count is set](https://github.com/godotengine/godot-docs/issues/8937) | 3 |
| godotengine/godot-docs | [Mention that ShapeCast2D and ShapeCast3D stop scanning at the first instance of collision.](https://github.com/godotengine/godot-docs/issues/9624) | 4 |
| godotengine/godot-docs | [Control class page doesn't mention ".release_focus()" in intro](https://github.com/godotengine/godot-docs/issues/9452) | 4 |


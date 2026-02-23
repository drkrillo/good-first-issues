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

## List of Good First Issues to start Collaborating! :surfer: <sub><sub>Last run: 2026-02-23</sub></sub>



### C++

| Repo | Title | Comments |
| --- | --- | --- |

| pytorch/glow | [TensorLayout] Add a way to specify canonical layout propagation to NodeGen | 0 |

| pytorch/glow | [Runtime] Expand Yaml DeviceConfig loading to include HostConfig | 0 |

| pytorch/glow | [runtime] add device memory size configuration to the DeviceConfig::parameters map on all backends | 0 |

| pytorch/glow | resnet-* example code should reuse Tensor memory for images | 0 |

| pytorch/glow | Example binaries should handle HostManager active request limit | 0 |

| pytorch/glow | [ONNXIFI] Add additional precondition checks to model loaders | 0 |

| pytorch/glow | [ONNXIFI][GraphAPI] Add "orErr" methods for graph creation api | 0 |

| pytorch/glow | ConvBench should use the layers of ResNet | 0 |

| pytorch/glow | ConvBench should use libjit_convolution_D8KKC8 | 0 |

| pytorch/xla | [torch_xla] scan_layers fails if the layer have no weights | 0 |

| pytorch/xla | Op info test for `bmm .. ceil` | 0 |

| pytorch/xla | Op info test for `rsub .. searchsorted` | 0 |

| pytorch/xla | Op info test for `norm .. pca_lowrank` | 0 |

| pytorch/xla | Op info test for `nn.functional.softmin .. nonzero_static` | 0 |

| pytorch/xla | Op info test for `nn.functional.group_norm .. nn.functional.layer_norm` | 0 |

| pytorch/xla | Op info test for `nn.functional.conv_transpose3d .. nn.functional.ctc_loss` | 0 |

| pytorch/xla | Op info test for `linalg.ldl_factor_ex` | 0 |

| pytorch/xla | Op info test for `linalg.householder_product` | 0 |

| pytorch/xla | Op info test for `linalg.cholesky_ex` | 0 |

| pytorch/xla | Op info test for `linalg.cholesky` | 0 |

| pytorch/glow | [CPU] Remove the need for Rescale for the CPUMaxSplat | 1 |

| pytorch/xla | xs.make_mesh | 1 |

| pytorch/xla | torch_xla scan forces inputs to be differentiable | 1 |

| pytorch/xla | [hard] Op info test for `special.airy_ai` | 1 |

| pytorch/xla | Op info test for `triangular_solve .. unfold` | 1 |

| pytorch/xla | Op info test for `nn.functional.pixel_shuffle .. nn.functional.scaled_dot_product_attention` | 1 |

| pytorch/xla | Op info test for `linalg.matrix_norm` | 1 |

| pytorch/xla | Op info test for `linalg.lu_factor_ex` | 1 |

| pytorch/xla | Op info test for `linalg.lu_factor` | 1 |

| pytorch/xla | Op info test for `index_reduce` | 1 |

| pytorch/xla | [hard] Op info test for `histogramdd` | 1 |

| pytorch/glow | New files added under glow/test/models/ don't get copied to build folder until clean build is performed. | 2 |

| pytorch/glow | Make all useful data structures in Glow easy to dump in a textual form | 2 |

| pytorch/glow | [Importers] Move "run and compare" tests from importer tests to operator tests | 2 |

| pytorch/glow | Need to canonicalize or optimize high-dim concat to concat+transpose | 2 |

| pytorch/xla | Op info test for `special.scaled_modified_bessel_k0 .. squeeze` | 2 |

| pytorch/xla | Op info test for `nn.functional.feature_alpha_dropout .. nn.functional.grid_sample` | 2 |

| pytorch/xla | Op info test for `linalg.matrix_power` | 2 |

| pytorch/xla | Op info test for `linalg.ldl_solve` | 2 |

| tensorflow/minigo | Support more GTP commands | 3 |

| pytorch/glow | Move layout information from nodes constructor' to their Glow types | 3 |

| pytorch/glow | [habana] Implement backend specific verifications | 3 |

| pytorch/xla | Op info test for `nn.functional.leaky_relu .. nn.functional.max_pool1d` | 3 |

| pytorch/xla | Op info test for `kthvalue` | 3 |

| pytorch/glow | [GraphOptz] Sink Quantize below Reshape | 4 |

| pytorch/xla | Op info test for `pinverse .. put` | 4 |

| pytorch/xla | Op info test for `nn.functional.avg_pool1d .. nn.functional.bilinear` | 4 |

| pytorch/xla | Op info test for `linalg.lu_solve` | 4 |

| pytorch/glow | Fuse RescaleQuantized in the ChannelwiseQuantizedConv | 5 |

| pytorch/glow | Bring back the sinking RELU below Pool optimization | 5 |

| pytorch/glow | Use gtest-parallel | 5 |

| pytorch/glow | Glow should provide its own implementation of a random number generator to ensure deterministic testing and avoid platform-dependent differences | 6 |

| pytorch/glow | Make the execution of the Glow compiler more deterministic between multiple runs | 9 |

| opencv/opencv_contrib | reg: broken python sample | 13 |

| pytorch/glow | [ONNXModelLoader] Support for LogSoftmax operator is missing | 16 |

| opencv/opencv_contrib | selectROI pointer almost invisible on certain colours | 16 |

| pytorch/glow | Use explicit std::string conversions instead of implicit llvm::StringRef->std::string conversions to prepare Glow for builds using LLVM >=11 | 18 |

| godotengine/godot | [Godot v4.4] Gizmos exponentially increasing Draw Calls and Objects when turned on | 22 |

| godotengine/godot | You're breathtaking! | 32 |

| godotengine/godot | PointLight2D doesn't respect Nearest texture filter for normal-maps or shadows | 34 |

| godotengine/godot | [TRACKER] Unit tests to add or improve | 237 |




### Cython

| Repo | Title | Comments |
| --- | --- | --- |

| ansible/pylibssh | [TODO] Ensure release builds don't include debug symbols | 0 |




### Emacs Lisp

| Repo | Title | Comments |
| --- | --- | --- |

| godotengine/emacs-gdscript-mode | Rewrite gdscript-imenu to provide GDScript-specific tables | 0 |

| godotengine/emacs-gdscript-mode | Buffer does not revert or update instantly after formatting buffer | 3 |




### GDScript

| Repo | Title | Comments |
| --- | --- | --- |

| godotengine/godot-demo-projects | Update plugins demo to use custom Resources | 0 |

| godotengine/godot-benchmarks | [Call to Action] Benchmarks for the benchmark server | 5 |

| godotengine/godot-benchmarks | [TRACKER] Benchmarks to create | 11 |




### Go

| Repo | Title | Comments |
| --- | --- | --- |

| ansible/receptor | append conntype string representation in status output | 0 |

| ansible/receptor | add work status command to receptorctl | 1 |

| ansible/receptor | quality of life -- order work list output based on most recent work units | 2 |




### HTML

| Repo | Title | Comments |
| --- | --- | --- |

| django/birthday20 | Add social media links on event pages | 2 |

| django/birthday20 | Vendor third-party assets (leaflet) | 10 |




### Java

| Repo | Title | Comments |
| --- | --- | --- |

| pytorch/serve | The captum for bert notebook needs update | 0 |

| pytorch/serve | Enable naked DIR test case for windows environment | 0 |

| pytorch/serve | [Educational] Typing `.py` files iteratively with mypy | 1 |

| pytorch/serve | Built-in handler for regression | 1 |

| pytorch/serve | permission error while trying to remove previous artifact files in `/tmp/` | 3 |

| pytorch/serve | Torchserve M1 support detailed plan | 4 |

| pytorch/serve | add support for SeTFiT models | 4 |

| pytorch/serve | [BUG] Dockerfile with nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04 gives ascii codec error | 4 |

| pytorch/serve | how does `default_response_timeout` work? | 6 |

| pytorch/serve | [Suggestion] Loading torch-model-archiver arguments from YAML | 6 |

| pytorch/serve | Handle invalid input intelligently ！ | 7 |




### JavaScript

| Repo | Title | Comments |
| --- | --- | --- |

| huggingface/transformers.js | Is 'aggregation_strategy' parameter available for token classification pipeline? | 2 |

| huggingface/transformers.js | [Feature request] Return offset mapping using tokenizer | 2 |

| pytorch/ci-hud | Restore "Show service jobs" checkbox to GitHubStatusDisplay.js  | 2 |

| huggingface/transformers.js | [Doc request] Add an example guide of how to use it in Svelte (and deploy to HF Spaces) | 7 |




### Jinja

| Repo | Title | Comments |
| --- | --- | --- |

| ansible/galaxy_collection | Replace order of roles | 0 |

| ansible/galaxy_collection | infra.ah_configuration.publish leaves clone dirs behind | 0 |

| ansible/awx-operator | Add multi-arch build target | 1 |

| ansible/product-demos | Add teardown template/workflow for "Deploy Cloud Stack in AWS" workflow | 1 |

| ansible/awx-operator | annotations not applied to postgres statefulset | 2 |

| ansible/awx-operator | Inflated Total Host Count on Dashboard when Using Constructed Inventory with Existing Inventories | 2 |

| ansible/awx-operator | Extend README with external logging examples | 2 |

| ansible/receptor-collection | Support for Debian 12 | 2 |

| ansible/awx-operator | Inability to overwrite namespace when using awx-operator chart | 3 |

| ansible/awx-operator | Password set via UI gets overwritten by initialize_django playbook | 5 |




### Jupyter Notebook

| Repo | Title | Comments |
| --- | --- | --- |

| tensorflow/probability | providing sample weights to glm.fit() and glm.fit.sparse() | 0 |

| tensorflow/probability | Sigmoid belief network example/tutorial | 0 |

| tensorflow/probability | Logistic factorial analysis example/tutorial | 0 |

| tensorflow/swift-models | Add documentation to the Gym models to specify additional dependencies for DQN | 0 |

| tensorflow/swift-models | [BERT-CoLA]: Use common file extraction functions | 0 |

| tensorflow/swift-models | Verify BERT variants | 0 |

| tensorflow/probability | Feature Request: Add crps method to tfp.distributions | 1 |

| tensorflow/probability | Keyword argument overload (?) in tfb.real_nvp_default_template | 1 |

| tensorflow/probability | Item response theory model example/tutorial | 1 |

| tensorflow/probability | Bayesian neural network tutorial | 1 |

| tensorflow/swift-models | Add logging callbacks for training statistics  | 1 |

| tensorflow/probability | Support for SeparableConv1DFlipout | 2 |

| tensorflow/probability | NotImplementedError: mean is not implemented: Categorical | 2 |

| tensorflow/probability | Always-on dropout layer | 2 |

| tensorflow/probability | DenseFlipOut layer | 2 |

| tensorflow/probability | Categorical autoregressive distribution with LSTM example/tutorial | 2 |

| tensorflow/swift-models | Better error message on unzip failure | 2 |

| tensorflow/swift-models | Find a more descriptive word for `numericalized` | 2 |

| tensorflow/swift-models | Rewrite long nested `Sequential` types using `Sequential{N}` typealiases | 2 |

| tensorflow/swift-models | [BERT-CoLA] Data source resolution | 2 |

| tensorflow/swift-models | Object detection examples | 2 |

| pytorch/functorch | Add vmap support for PyTorch operators | 2 |

| tensorflow/adanet | Allow one to forward features to predictions | 3 |

| tensorflow/probability | Feature Request: Alternative Horseshoe Parameterization as tfp distribution | 3 |

| tensorflow/probability | Please add example on NUTS sampling from posterior for Bayesian Logistic Regression | 3 |

| tensorflow/probability | Feature request: Tweedie distribution | 3 |

| tensorflow/probability | CholeskyWishart distribution | 3 |

| tensorflow/probability | improve text and visuals in Bayesian Gaussian mixture model tutorial | 3 |

| tensorflow/swift | Installation verification tool | 3 |

| tensorflow/probability | A question about target_log_prob_fn | 4 |

| tensorflow/probability | Provide a resimulation Metropolis TransitionKernel | 4 |

| tensorflow/swift-models | Translation example | 4 |

| tensorflow/probability | Laplace approximation | 5 |

| tensorflow/probability | Missing Inverse Wishart - redefine Wishart? | 5 |

| tensorflow/probability | Categorical features in logistic regression | 5 |

| tensorflow/probability | Stochastic block model example/tutorial | 5 |

| tensorflow/probability | BFGS user should be able to pass parameters to the line search | 6 |

| tensorflow/probability | Tutorial on Variational Inference | 6 |

| tensorflow/swift-models | Speech to text example | 7 |

| tensorflow/probability | Any plans to update the examples to TensorFlow 2? | 8 |

| tensorflow/probability | Sample different weights for examples within a  batch | 9 |

| tensorflow/probability | [Feature Request] tensorflow_probability.distributions.GeneralizedGamma | 11 |

| tensorflow/probability | Feature Request: Efficient Poisson Binomial PMF/CDF in tfp | 13 |

| tensorflow/probability | [Feature Request] Zero-Inflated Poisson and Negative Binomial distributions | 13 |

| tensorflow/swift-models | UNet Example | 15 |




### PHP

| Repo | Title | Comments |
| --- | --- | --- |

| zeromicro/goctl-swagger | support for openapi 3.0  | 0 |

| godotengine/godot-asset-library | Categories need a description (tooltip?) when hovered/selected | 1 |

| godotengine/godot-asset-library | keep the content of the submition form when its not validated, or try some ajax realtime pre-validation | 1 |

| godotengine/godot-asset-library | A way to cancel edit requests | 3 |

| godotengine/godot-asset-library | Sanitize inputs for Asset data/fields, like URLs | 5 |




### Python

| Repo | Title | Comments |
| --- | --- | --- |

| huggingface/nanotron | [Feature] Use CUDA event for measuring elasped time | 0 |

| huggingface/nanotron | [Feature] Refactor `ParallelContext.world_rank_matrix` | 0 |

| huggingface/optimum-executorch | Add benchmarking numbers for more models | 0 |

| ansible/ansible-dev-tools | Ensure tests are passing with devspaces container | 0 |

| ansible/ansible-jupyter-kernel | Add support for handlers | 0 |

| ansible/ansible-jupyter-kernel | Add a #library cell type | 0 |

| ansible/awx | [ui_next] Add All/Any workflow viz indication to Workflow Viz Legend/Key | 0 |

| ansible/awx-plugins | Make `azure_keyvault_backend()` handle DNS resolution issues | 0 |

| ansible/dispatcherd | Enforce UUID format, add "origin" information in message data | 0 |

| ansible/django-ansible-base | `ansible_base.lib.utils.models.diff` takes unused `sanitize_encrypted` param and has outdated return docstring | 0 |

| tensorflow/moonlight | Follow the MusicXML schema | 0 |

| tensorflow/moonlight | Export stem directions in MusicXML | 0 |

| tensorflow/moonlight | Chord duration correction | 0 |

| tensorflow/moonlight | Export the key signature to MusicXML | 0 |

| pytorch/ao | Resolve doc build warnings | 0 |

| pytorch/ao | [fp8 blockwise training] try using torch._scaled_mm instead of Triton kernels for fp8 gemms | 0 |

| pytorch/ao | TorchAO ROCM tests are taking a long time | 0 |

| pytorch/examples | imagenet benchmark measure elapsed time function issue | 0 |

| pytorch/examples | Why there is no tanh activation at the end of TransformerNet? | 0 |

| pytorch/examples | Distributed doesn't work with env:// init_method | 0 |

| pytorch/examples | Is the loss of the first word covered during the language model evaluation? | 0 |

| pytorch/examples | The casting problem on the result of the model. | 0 |

| pytorch/examples | Example code (mnist) does not work under torch.utils.bottleneck | 0 |

| pytorch/executorch | Support getting the delegated payload | 0 |

| pytorch/executorch | [CMake] Potentially duplicated srcs in llama_runner build | 0 |

| pytorch/executorch | Add Android model E2E test | 0 |

| pytorch/PiPPy | Support Segformer models in HF tests | 0 |

| pytorch/PiPPy | Support ConvNext models in HF tests | 0 |

| pytorch/PiPPy | Support Wav2Vec2 models in HF tests | 0 |

| pytorch/PiPPy | Support ResNet models in HF tests | 0 |

| pytorch/PiPPy | [spmd] DistributedTensor doesn't implement is_pinned | 0 |

| pytorch/PiPPy | Support Donut SWIN models in HF tests | 0 |

| pytorch/PiPPy | Create mypy.ini | 0 |

| pytorch/PiPPy | Support DistilBert models in HF tests  | 0 |

| pytorch/PiPPy | Support Deberta models in HF tests | 0 |

| pytorch/PiPPy | Support HubertForSequenceClassification models in HF tests | 0 |

| pytorch/PiPPy | Support LxmertForPreTraining models in HF tests | 0 |

| pytorch/PiPPy | Support Speech2Text models in HF tests | 0 |

| pytorch/PiPPy | Support CLIP models in HF tests | 0 |

| pytorch/PiPPy | Support SWIN models in HF tests | 0 |

| pytorch/rl | [DO NOT CLOSE] Call for contributions | 0 |

| pytorch/tensordict | [Feature Request] Deprecate `_run_checks` in favour of `TensorDict._checked` | 0 |

| pytorch/torcharrow | Making BaseColumn::genericUnaryUDF and the family free functions | 0 |

| pytorch/torcharrow | Call type inferring in interop.from_pylist | 0 |

| pytorch/torcharrow | Move `torcharrow/test` to `test` | 0 |

| huggingface/nanotron | Add Debug utility to be able to preview first samples used for training | 1 |

| huggingface/nanotron | We don't save checkpoint after training ends | 1 |

| huggingface/nanotron | FEAT: Support 1.58-bit LLMs training | 1 |

| huggingface/nanotron | [Feature Request] Add simple communications benchmarks to the repo | 1 |

| huggingface/sentence-transformers | Update example scripts relying on `http_get` to download from the Hugging Face Hub instead | 1 |

| ansible/ansible-documentation | Need explanation that modules can only import from `module_utils` within the `ansible` namespace | 1 |

| ansible/ansible-documentation | Prune stub files in docs/docsite | 1 |

| ansible/ansible-navigator | Many params missing change after initial = False | 1 |

| ansible/awx | Scheduled Job prompted extra_vars overwritten by JT extra_vars | 1 |

| ansible/awx | Inaccurate error handling on Input Group Integer fields (i.e. Org Max Hosts field) | 1 |

| ansible/awx | RFE: Send real client remote address in TACACS+ authentication packet | 1 |

| ansible/django-ansible-base | Several unordered querysets | 1 |

| tensorflow/agents | Tutorial 1: Train a Deep Q Network with TF-Agents and the use of a driver | 1 |

| pytorch/ao | Refactor torchao and tests to use model architectures from torchao.testing.model_architectures | 1 |

| pytorch/ao | Add weight tensor-wise scaling for INT8 quantized and mixed-precision training | 1 |

| pytorch/ao | MoE example  | 1 |

| pytorch/ao | Self compressing neural networks | 1 |

| pytorch/examples | Video classification example | 1 |

| pytorch/examples | Resume will override learning rate on command line. | 1 |

| pytorch/examples | A question about weight initialization of embedding layer. | 1 |

| pytorch/examples | Changes needed to run DCGAN 32x32  | 1 |

| pytorch/examples | ImageFolder doc should clarify 1. order that images returned in 2. that all classes are concatenated into a single list | 1 |

| pytorch/examples | Doc comment on `accuracy` method in imagenet example, incorrect? | 1 |

| pytorch/executorch | Support dim order in Java Tensor | 1 |

| pytorch/executorch | Add dynamism tests for xnnpack model tests | 1 |

| pytorch/executorch | Implement load_into for the shared_ptr data loader | 1 |

| pytorch/executorch | Test exported models in Python | 1 |

| pytorch/executorch | Format CMakeLists.txt | 1 |

| pytorch/executorch | [Android] instrumentation test use models from storage, not bundled with apk | 1 |

| pytorch/executorch | [Android] Use generic JNI instead of fbjni | 1 |

| pytorch/PiPPy | Support LayoutLM models in HF tests | 1 |

| pytorch/pytorch | torch.compile does not support Python try/except | 1 |

| pytorch/pytorch | [BE] Deduplicate auto_functionalized and triton_kernel_wrapper_functional | 1 |

| pytorch/text | torchtext main branch doesn't support pytorch2.0 | 1 |

| pytorch/torcharrow | Default aggregation functions delegates to Arrow Compute  | 1 |

| pytorch/torchchat | GeneratorArgs.is_torchtune_model is a misnomer | 1 |

| pytorch/torchtitan | Ability to train based on epoch | 1 |

| huggingface/nanotron | [Feature] Asyncronous Serialization | 2 |

| huggingface/nanotron | [Feature Request] Support Data Streaming for faster training of large models | 2 |

| huggingface/transformers | [Performance] Tracking open Issues and PRs (pytorch transformers) | 2 |

| ansible/ansible-navigator | Switch to the use of `pathlib` where possible | 2 |

| ansible/awx | Empty value in execution_environment should remove selections (ansible.controller.job_template) | 2 |

| ansible/awx | Issue label for incompliance with Ansible | 2 |

| ansible/awx | New credentials type to provide VAULT_ADDR and VAULT_TOKEN env vars | 2 |

| ansible/awx | Expose the value of "Execution Node" as a variable when running a job from Ansible Tower. | 2 |

| ansible/awx | "Playbook not found for project" error when the playbook exist but is invalid  | 2 |

| ansible/awx | Jobs canceled before starting should not show a "finished" time | 2 |

| ansible/awx | Make Info Metrics more easy to query | 2 |

| ansible/awx | weekly dashboard view does not have sufficient granularity | 2 |

| tensorflow/graphics | Tangential camera distortion/undistortion | 2 |

| pytorch/ao | Unittests Migration Progress | 2 |

| pytorch/ao | [MX \| Triton] Create MX matmul op using new `scaled_dot` op in Triton | 2 |

| pytorch/ao | Support for GrokAdamW | 2 |

| pytorch/ao | Tensor subclass boilerplate can be consolidated | 2 |

| pytorch/ao | [RFC] Intx Tensor Subclasses Quantization | 2 |

| pytorch/examples | Update all examples to latest versions of pytorch | 2 |

| pytorch/examples | Warning: an output with one or more elements was resized since it had shape[xxxx],] | 2 |

| pytorch/examples | Add nn.SyncBatchNorm in ImageNet example | 2 |

| pytorch/examples | mnist example contains bad practices leading to wrongful results | 2 |

| pytorch/examples | Input type and weight type should be the same | 2 |

| pytorch/examples | please use longer names for variables than 2-3 letter acronyms | 2 |

| pytorch/examples | VAE reconstruction loss (BCE)  | 2 |

| pytorch/examples | Imagenet training extremely low gpu utilization | 2 |

| pytorch/examples | Ambiguous code in reinforce | 2 |

| pytorch/executorch | [Arm] Size-test: Run the binary on CI | 2 |

| pytorch/executorch | Consolidation of Selective Build APIs for OSS | 2 |

| pytorch/executorch | [Android] Rename JNI cpp file | 2 |

| pytorch/executorch | Add torchao kernels to xcframework | 2 |

| pytorch/executorch | Need a feature to get etdump while running LLAMA model on qnn with qnn_llama_runner | 2 |

| pytorch/executorch | [Request impl] Gracefully error out in ETDump | 2 |

| pytorch/PiPPy | Make RemoteInterpreter use the full implementation of `Interpreter.run` | 2 |

| pytorch/rl | [Feature Request] Make sure that all losses work with tensorclasses and regular tensors | 2 |

| pytorch/rl | [Feature Request] TensorSpec is_in methods should check the dtype of val | 2 |

| pytorch/text | Convert iterator-style raw datasets to map-style raw datasets | 2 |

| pytorch/torchchat | torchtune as an optional dependency: Lazy Import | 2 |

| pytorch/torchchat | Slimming down torchchat: Replace replace_attention_with_custom_sdpa_attention() with ET's implementation | 2 |

| ansible/ansible-documentation | Incorporate 'shared snippets' for the collection docs into the main rst files | 3 |

| ansible/awx | Fix Delinea imports and import test | 3 |

| ansible/awx | Cleanup Job Details. Configure days retention for the particular job entities.  | 3 |

| ansible/awx | Improve user experience of copy pasting FQDNs from jobs | 3 |

| ansible/awx | Non descriptive error when podman is missing | 3 |

| ansible/awx | Add "nodes" to "Relaunch on" when relaunching jobs after failure - users think it relates to failed tasks and not nodes | 3 |

| ansible/awx | Worker failed to run task awx.main.tasks.system.purge_old_stdout_files | 3 |

| ansible/awx | System Auditors can check list items | 3 |

| ansible/awx | Show more host information in host filter lookup list  | 3 |

| ansible/awx | Inconsistent capitalization across ui-next  | 3 |

| ansible/awx | User auth field not documented in OPTIONS | 3 |

| tensorflow/addons | Benchmark test for rrelu fails on windows | 3 |

| tensorflow/graphics | Add skew to projective camera | 3 |

| tensorflow/model-card-toolkit | Prefer single quote strings model-card-toolkit | 3 |

| tensorflow/similarity | Add a ranking example | 3 |

| pytorch/ao | FP8 Blockwise Training Tracker | 3 |

| pytorch/ao | [QAT] Low-bit FSDP all-gather for QAT | 3 |

| pytorch/ao | [sparse] Add GPTQ support for sparse-marlin | 3 |

| pytorch/ao | Tensor Parallelism Support for AffineQuantizedTensor | 3 |

| pytorch/examples | word_language_model with torch.nn.modules.transformer | 3 |

| pytorch/examples | OSError: [Errno 22] Invalid argument: | 3 |

| pytorch/examples | MNIST test_loader not being used as intended (wrong)! | 3 |

| pytorch/examples | Actor critic example not using discount rate properly | 3 |

| pytorch/examples | "omit freeze_support" | 3 |

| pytorch/executorch | torch.split fails in to_edge | 3 |

| pytorch/executorch | Support Standalone Batch Norm | 3 |

| pytorch/executorch | Get rid of fixed number cmake --build -j in sh and docs | 3 |

| pytorch/executorch | Consolidate executor_runners | 3 |

| pytorch/executorch | ExecuTorch Scalar to() supports fewer types than c10::Scalar, breaking source compatibility | 3 |

| pytorch/pytorch | [auto functionalize][partitioner] ones_like is not getting recomputed | 3 |

| pytorch/torchchat | Improve Tokenizer New Type Onboarding | 3 |

| pytorch/torchchat | [UX] We are too quiet about errors - in particular missing HF authentication... | 3 |

| pytorch/torchdistx | Documentation for AnyPrecisionOptimizer | 3 |

| xbmc/addon-check | Correct the mentioned pylint errors to get perfect 10. (missing-docstring) | 3 |

| godotengine/godot-blender-exporter | Blender object with negative scale | 3 |

| huggingface/transformers | GeneratorExp aren't supported by torch.jit.script when I try to export a previously trained model  'google/vit-base-patch16-224-in21k'. | 4 |

| django/djangoproject.com | Github login doesn't work for community pages | 4 |

| django/djangoproject.com | Documentation table of contents is hard to reach on mobile devices | 4 |

| ansible/ansible-documentation | Link to devel in the various roadmaps | 4 |

| ansible/awx |  visualizer info field  | 4 |

| ansible/awx | Remove some of the eslint-disable comments | 4 |

| ansible/awx | Docker install instructions do not mention how to add awx-logos | 4 |

| tensorflow/graphics | Add ScanNet dataset | 4 |

| pytorch/ao | [llama] Use horizontal fusion trick from Attention for FeedForward | 4 |

| pytorch/ao | Quantized Training | 4 |

| pytorch/examples | Please change dcgan to load truncated images. | 4 |

| pytorch/examples | No matching function call  error in custom_dataset example  | 4 |

| pytorch/examples | Add Siamese Network example | 4 |

| pytorch/executorch | Re-inplace slice_copy with slice | 4 |

| pytorch/pytorch | Use typing_extensions.TypeAliasType for better reexport of `__module__` | 4 |

| pytorch/pytorch | [inductor] nan_asserts doesn't work for FP8, "RuntimeError: "isinf" not implemented for 'Float8_e4m3fn'" | 4 |

| pytorch/pytorch | Remove tensor variable default method fallthrough | 4 |

| pytorch/pytorch | [export] Schematize nn_module_stack serialization | 4 |

| huggingface/nanotron | Avoid nested `InheritFromOtherOptimizer` | 5 |

| huggingface/nanotron | [Bug] Missing `_is_using_mup` when resume checkpoint | 5 |

| huggingface/nanotron | [Unit Test] Add unit tests for DistributedTrainer | 5 |

| huggingface/sentence-transformers | Update example scripts relying on `model.fit` to use `SentenceTransformerTrainer` instead | 5 |

| pandas-dev/pandas | BUG: Timedelta resolution is different depending on how the argument is passed | 5 |

| pandas-dev/pandas | .add gives incorrect result with MI Dataframe with mix of object and datetimes on index. | 5 |

| pandas-dev/pandas | DataFrame.update silently does nothing when indices are of differing type | 5 |

| django/djangoproject.com | Redirect from /about to /foundation | 5 |

| django/djangoproject.com | fundraising: 'customer.subscription.deleted' webhook event always gets 404 response | 5 |

| ansible/ansible-lint | 'format' option missing from configuration file schema | 5 |

| ansible/awx | Add option to force the user to reset its password at first login | 5 |

| ansible/awx |  adhoc jobs block other jobs from being processed in the queue | 5 |

| ansible/awx | all cluster nodes in development environment have the same UUID | 5 |

| tensorflow/graphics | Not detecting TF Nightly when installing from whl. | 5 |

| tensorflow/similarity | Implement multi-siam for segmentation | 5 |

| pytorch/ao | [low-bit optim] Add COAT optimizer | 5 |

| pytorch/ao | The next tutorials | 5 |

| pytorch/audio | read mp3 file fail | 5 |

| pytorch/pytorch | [dynamo, BE] get rid of IncorrectUsage exception | 5 |

| pytorch/pytorch | Report WHY a symbol was created dynamically in symbolic_shapes logs | 5 |

| pytorch/pytorch | torch.fx.Tracer.record_stack_traces is broken in torch 2.4.0 | 5 |

| pytorch/rl | [Feature Request] Missing ActionScaling and FlattenAction  | 5 |

| pandas-dev/pandas | BUG: Conversion from datetime64[ns] to datetime does not effect .info() and probably not the DataFrame itself | 6 |

| pandas-dev/pandas | BUG: groupby.var() does not return arrow types with arrow backed series as input.  | 6 |

| pandas-dev/pandas | BUG: Multiindex Categorical type lost after div operation | 6 |

| pandas-dev/pandas | Groupby Agg not working if different partials with same name on the same column | 6 |

| django/djangoproject.com | Add link to 'Stable' doc version in the Warning Alert on top | 6 |

| django/djangoproject.com | Add link to new minutes repo | 6 |

| django/djangoproject.com | Support switching languages on non-docs sites | 6 |

| ansible/ansible-documentation | Misleading statement about "defaults" and "vars" sub-folders of roles | 6 |

| ansible/ansible-navigator | Allow to set ansible-runner artifacts dir ID  | 6 |

| ansible/awx | AWX Collection Credential Delete | 6 |

| tensorflow/similarity | Create a colab for single shot to demonstrate how augmenters works | 6 |

| pytorch/ao | Accelerate activation sparsity with activation compression | 6 |

| pytorch/executorch | Manual kernel registration to include library names in API | 6 |

| pytorch/pytorch | AOTAutograd: functionalization should emit foreach_copy_() instead of copy_() when possible | 6 |

| pandas-dev/pandas | BUG: Strange behavior when accessing datetime.date index with np.datetime64 | 7 |

| pandas-dev/pandas | BUG: enlarging a DataFrame by adding an extra column with a tz-aware datetime results in object dtype | 7 |

| pandas-dev/pandas | Possible bug in df.update | 7 |

| django/djangoproject.com | Improvements to the Corporate Sponsor Experience | 7 |

| django/djangoproject.com | Improve Documentation by having list of topics fixed on the left and table of contents on the right  | 7 |

| django/djangoproject.com | Docs for old supported versions should indicate that a newer version is available | 7 |

| tensorflow/similarity | Implement SwAV for self-supervised learning | 7 |

| pytorch/audio | Use non-persistent buffers | 7 |

| pytorch/examples | Why don't we use MSE as a reconstruction loss for VAE ? | 7 |

| pytorch/executorch | Rename `executorch` cmake target to `prim_ops_lib` | 7 |

| pytorch/executorch | Add timestamps for pte generation in CI | 7 |

| pytorch/executorch | [Request Impl] Apply Segment Serialization in Bundled Program | 7 |

| pytorch/executorch | Fail to allocate temp memory by exporting torch.topk | 7 |

| huggingface/transformers | Syntax error in Transformer section 3 (Transformers, what can they do?) notebook | 8 |

| pandas-dev/pandas | ENH: Change ExtensionOpsMixin behaviour to not add new operator method if one is already defined on the ExtensionArray class | 8 |

| django/djangoproject.com | Use noindex meta tag or header, not robots.txt, to block untranslated docs pages | 8 |

| ansible/ansible-documentation | Link "see also" sections as recommended in the forum | 8 |

| ansible/awx | Display SAML login icon for /api/login page | 8 |

| pytorch/pytorch | [Inductor] Inference failed with the compiled model with aminmax operator | 8 |

| pytorch/pytorch | [BUG][PyTorch 2.0 Export][quant]:get_source_partitions() may return different matches with same input graph | 8 |

| pytorch/pytorch | Improve error message for wrong number of arguments in CachingAutotuner | 8 |

| pytorch/pytorch | [Dynamo] Support tracing through _get_current_dispatch_mode_stack | 8 |

| huggingface/transformers | oom when using adafactor optimizer in deepspeed | 9 |

| pandas-dev/pandas | BUG: DataFrame.rank does not return EA types when original type was an EADtype | 9 |

| pandas-dev/pandas | Information for new contributors | 9 |

| pandas-dev/pandas | Series.combine with fill_value gives unexpected results | 9 |

| pandas-dev/pandas | startingMonth ignored on non-unitary Quarter periods | 9 |

| django/djangoproject.com | Remove non-canonical docs versions from sitemap.xml | 9 |

| tensorflow/similarity | Lifted Structured loss | 9 |

| pytorch/executorch | Refactor binary op partitioner configs under binary op config class | 9 |

| pytorch/pytorch | aten.grid_sampler_3d.default is missing a c-shim implementation, using proxy executor as fallback | 9 |

| pytorch/pytorch | dynamo (re)compilation issues: shape (1,1), nn.Parameter, mark_dynamic | 9 |

| pytorch/pytorch | Using an empty tensor and `torch.int64` or `torch.bool` for `dtype` of `nanmean()` works while a non-empty tensor doesn't work | 9 |

| pandas-dev/pandas | ERR: ``numeric_only`` in reduction operations should disallow passing non-bools | 10 |

| pandas-dev/pandas | ENH: Better error message when interpolating dtype integer with method="linear" | 10 |

| pandas-dev/pandas | DOC: `.str.cat` output in case of `Index` object | 10 |

| pytorch/executorch | Check tensor's dim order ambiguity in IR verifier | 10 |

| pytorch/pytorch | [dynamo] [dynamic] `torch.combinations` throws RuntimeError when `(backend=aot_eager, dynamic=True)` | 10 |

| pytorch/pytorch | Expand Tag Set: views & reductions | 10 |

| huggingface/transformers | [trainer] figuring out why eval with `--fp16_full_eval` is 25% slower | 11 |

| tensorflow/quantum | [Performance] Boost tfq.convert_to_tensor speed | 11 |

| pytorch/ao | Named Symbol not found (torchchat #1298) | 11 |

| pytorch/ao | [MPS] torchao low-bit-precision optim does not expose 'backend' argument to torch.compile | 11 |

| pytorch/ignite | Replace typing hints with new version | 11 |

| pytorch/pytorch | foreach_map enhancements | 11 |

| pytorch/pytorch | Docs are little bit outdated for torch logs | 11 |

| pytorch/pytorch | bmm, topk, cholesky, linalg.norm, max with out variants set causing recompilations in torch.compile | 11 |

| pandas-dev/pandas | BUG: concat with datetime64 columns of differing resolutions results in object dtype | 12 |

| pandas-dev/pandas | BUG: Assigning extension array value to series of dtype object fails if element type is array-like | 12 |

| django/djangoproject.com | Make right sidebar independent from main content | 12 |

| pytorch/ao | Update documents addressing AQT workflow | 12 |

| pytorch/pytorch | torch.compile regression 2.9.1: Triton kernel name '_Runner__kernel_name_0' is not defined | 12 |

| pytorch/pytorch | Logging when executing fx.Interpreter | 12 |

| pandas-dev/pandas | DOC: Reindexing behaviour of dataframe column-assignment missing | 13 |

| django/djangoproject.com | New content: Accessibility statement | 13 |

| pytorch/pytorch | [Feature request] `torch.export` .save/.load could support `safetensors` and/or `weights_only=True` | 13 |

| pandas-dev/pandas | [Feature Request] Add `replace` method to `Index` objects | 14 |

| django/djangoproject.com | Improve 404 page | 14 |

| pytorch/pytorch | Make tlparse able to show a summary of distinct graph breaks | 14 |

| pandas-dev/pandas | BUG: inconsisntent construction results between `pd.array` and `pd.Series` for dtype=str | 15 |

| pandas-dev/pandas-stubs | `pd.concat` with `GeoDataFrame`s | 15 |

| huggingface/transformers | Follow ups to DocumentQuestionAnswering Pipeline | 16 |

| pytorch/pytorch | Device check missing in torch.linalg.solve_triangular leading to hard crash | 16 |

| pandas-dev/pandas | Indexing on series where index is output from pd.cut  | 17 |

| django/djangoproject.com | Localize the fundraising app | 17 |

| pytorch/ao | Replace flash_4 with FlexAttention | 17 |

| pytorch/pytorch | Obscure error: Expected a value of type 'List[int]' for argument 'sizes' but instead found type 'immutable_list' | 17 |

| pytorch/pytorch | Supporting custom attributes with `__torch_function__` tensor subclasses | 17 |

| pytorch/ao | Add codebook (look up table based) quantization flow in torchao | 18 |

| pytorch/audio | Add Stereo to Mono Convertions | 18 |

| pytorch/executorch | [Request impl] Devtool end-to-end tests | 18 |

| pandas-dev/pandas | BUG: Interpolate over time does not work with Int64 or Float64 | 20 |

| pandas-dev/pandas | Updating value of a single row of a column using loc or at fails | 20 |

| django/djangoproject.com | Add Click to copy text for commands present in the official Django website. | 20 |

| pandas-dev/pandas | BUG: read_sql no longer works simply with SqlAlchemy selectables and a quick fix | 22 |

| huggingface/transformers | Export LayoutLMv2 to onnx  | 24 |

| pandas-dev/pandas | DOC: Single Document For Code Guidelines | 24 |

| huggingface/transformers | Add support for BLIP and GIT in image-to-text and VQA pipelines | 25 |

| pandas-dev/pandas | WEB: Multiple "Getting Started" on pandas.io leads to different links | 25 |

| huggingface/transformers | Getting time offsets of beginning and end of each word in Wav2Vec2 | 26 |

| pandas-dev/pandas | CLN: Use dedup_names in all instances where duplicate column names are renamed | 29 |

| huggingface/transformers | Trying to add support for GPT2 as decoder in EncoderDecoder model | 31 |

| pytorch/ignite | 🥇 Everyone is welcome to contribute 💯  | 37 |

| huggingface/peft | Comparison of Different Fine-Tuning Techniques for Conversational AI | 44 |




### Rust

| Repo | Title | Comments |
| --- | --- | --- |

| tensorflow/rust | Add Scope::with_kernel_label and with_xla_cluster | 3 |

| tensorflow/rust | Add OpArgDef::default_value and allowed_values | 7 |




### SCSS

| Repo | Title | Comments |
| --- | --- | --- |

| godotengine/discourse-theme | Change default `green` to our own green for the Solved questions | 0 |

| godotengine/discourse-theme | Make tag and tag count more distinct | 0 |

| godotengine/discourse-theme | Categories are not rounded on mobile | 0 |

| godotengine/discourse-theme | Search bar should not cover full width on mobile | 0 |

| godotengine/discourse-theme | Remove the "Sign Up" button from navbar | 2 |




### Swift

| Repo | Title | Comments |
| --- | --- | --- |

| tensorflow/swift-apis | [summary] Better formatting | 0 |

| tensorflow/swift-apis | Lift Tensor.dimensionGathering() out of swift-models and into swift-apis | 0 |

| tensorflow/swift-apis | Investigate size/performance tradeoffs for `-sil-inline-generics` and `-sil-partial-specialization` | 0 |

| tensorflow/swift-apis | Update doc comments on non-mutating API to use proper wording. | 0 |

| huggingface/sam2-studio | Model download selector | 1 |

| tensorflow/swift-apis | Recursive Neural Networks (structured data/trees) | 3 |

| tensorflow/swift-apis | Implement Recurrent Layers | 5 |

| tensorflow/swift-apis | some mutating tensor operations are not @differentiable | 7 |

| tensorflow/swift-apis | Add derivative tests for layers | 7 |

| tensorflow/swift-apis | Adding Test Cases for Layers in Layer.swift file | 7 |

| tensorflow/swift-apis | Support Advanced Layers | 8 |

| tensorflow/swift-apis | Swifty API discovery via '@available' on raw APIs. | 8 |

| tensorflow/swift-apis | Add preconditions | 10 |

| tensorflow/swift-apis | Add more optimizers and losses | 16 |

| huggingface/sam2-studio | Video support estimated release date? | 26 |




### TypeScript

| Repo | Title | Comments |
| --- | --- | --- |

| ansible/vscode-ansible | Add option to prefix all shell commands the plugin executes | 0 |

| tensorflow/tfjs-tsne | Implement tensorToDataTexture in the GPU | 0 |

| pytorch/test-infra | Better highlight scheme for force merges | 0 |

| pytorch/probot | deprecation of `number` for octokit | 1 |

| ansible/vscode-ansible | Option to completely disable autocomplete | 3 |

| pytorch/test-infra | A better HUD menu for PyTorch repos family | 4 |

| pytorch/test-infra | Mergebot merged a PR even though a review had been re-requested | 5 |




### Unknown

| Repo | Title | Comments |
| --- | --- | --- |

| huggingface/awesome-huggingface | [hacktoberfest] Hugging Face Collections Hacktoberfest challenge | 0 |

| tensorflow/mlir | Implement support for qualified symbols | 0 |

| tensorflow/mlir | Consider trip count in loop invariant code motion | 4 |

| tensorflow/mlir | [LLVM] Implement missing LLVM IR instructions | 11 |




### reStructuredText

| Repo | Title | Comments |
| --- | --- | --- |

| godotengine/godot-docs | Add C# examples for custom BBCode | 0 |

| godotengine/godot-docs | Parallax2D property descriptions do not specify units | 1 |

| godotengine/godot-docs | Specify the coordinate system for the 'force' parameter in Rigidbody apply_force methods | 1 |

| godotengine/godot-docs | make_canvas_position_local | 1 |

| godotengine/godot-docs | Inconsistent code example between PhysicsShapeQueryParameters3D and PhysicsServer3D | 1 |

| godotengine/godot-docs | AudioServer Documentation does not specify units of time | 1 |

| godotengine/godot-docs | Curve2D.get_closest_point() incorrectly documented | 1 |

| godotengine/godot-docs | Add clarification about what CharacterBody is used for | 2 |

| godotengine/godot-docs | Viewport "use_hdr_2d" documentation point unclear | 2 |

| godotengine/godot-docs | Physics2DDirectSpaceState does not specify local or global coordinates | 2 |

| godotengine/godot-docs | PhysicsDirectSpaceState2D.get_rest_info claims not to use query motion but it does | 4 |

| godotengine/godot-docs | Control class page doesn't mention ".release_focus()" in intro | 4 |

| godotengine/godot-docs | WorkerThreadPool docs do not specify how Thread count is set | 4 |



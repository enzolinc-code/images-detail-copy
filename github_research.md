# GitHub 技术调研（V0.1）

## 结论先行

V0.1 不建议一开始部署 ComfyUI + 本地扩散模型。先用 Codex 官方 imagegen Skill / 内置 image_gen 验证真实电商样本闭环，再决定是否引入本地模型栈。

## 候选能力

### 1. openai/skills - imagegen

定位：Codex 官方图片生成/编辑 Skill。

价值：支持生成、编辑、参考图变体；默认优先调用 Codex 内置 image_gen，不需要 OPENAI_API_KEY。非常适合作为本项目 V0.1 的生成层。

采用：**是，作为 V0.1 默认生成路径。**

### 2. huggingface/diffusers - IP-Adapter

定位：用参考图片引导扩散模型，可增强主体/风格参考能力。

价值：适合后续增强“参考图风格保持”；可与 ControlNet 配合。

采用：**V0.2+ 可选增强，不作为 V0.1 必需依赖。**

### 3. huggingface/diffusers - ControlNet

定位：使用边缘、深度、姿态等结构条件约束生成。

价值：适合后续增强构图、深度、轮廓结构控制。

采用：**V0.2+ 可选增强。**

### 4. ComfyUI

定位：节点式生成工作流与本地模型编排。

价值：适合批量、可重复、复杂本地工作流。

风险：模型/节点依赖与显存、磁盘、运维复杂度明显高于 V0.1 所需。

采用：**暂不作为第一阶段必需项。**

### 5. vue-fabric-editor

定位：Vue + Fabric.js 开源图片编辑器，支持字体、模板、图层、裁剪等；MIT License。

价值：非常适合后期“详情页可编辑文字/图层模板”和视觉风格库 UI。

采用：**Phase 2 前端候选。**

## 当前技术组合

V0.1：

Codex Skill orchestration → reference/product visual analysis → Visual DNA JSON → generation brief → built-in image_gen → product fidelity quality gate.

Phase 2：

OCR/layout analysis → clean visual generation → Fabric.js-like editable text layer → section renderer → long-detail-page stitching.

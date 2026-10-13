# 技术架构 V0.1

## 目标

先验证“精品参考图 + 自有商品图 → 双模式淘宝主图”的真实闭环。

## 数据流

```text
reference image ----┐
                    ├─> visual analysis -> visual_dna.json
product image ------┘                         |
                                              v
mode + product facts ----------------> generation_brief.md
                                              |
                                              v
                                   Codex built-in image_gen
                                              |
                                              v
                                      generated image
                                              |
                                              v
                               product fidelity inspection
                                              |
                                              v
                                    quality_report.json
```

## 双模式

### precision_clone

保留参考图“空间与商业表达逻辑”，不机械复制第三方标识、独特插画、Logo、水印。

### style_rebuild

保留视觉 DNA，但主动重新组织构图，让结果具有明显独立性。

## 为什么先不用重型本地模型

当前最关键的不确定性是：真实淘宝精品参考图场景下，商品一致性是否能达到业务可接受水平。

先用 Codex 原生图片能力测试能最快得到答案。若失败原因明确属于构图/结构控制不足，再引入 IP-Adapter/ControlNet/ComfyUI。

## 质量门槛

漂亮 ≠ 合格。商品结构发生关键变化时必须失败或进入人工复核。

## Phase 2

详情页重点不是“让生图模型写中文”，而是把中文做成独立可编辑图层。

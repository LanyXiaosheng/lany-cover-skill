# Lany Cover Skill

为「Lany 小生」制作 X 长文、帖子和公众号的个人 IP 封面。它把**人物媒介**、**封面语言**和**视觉重点**分开选择：同一个小生可以是像素、手绘或丝印，画面可以是深色报告或浅色杂志，而读者第一眼看到的重点仍由这篇内容决定。

默认是当前像素小生、深色编辑构图和一处 `#D8FF00` 强调色。候选风格和测试图不会自动替换默认头像或长期品牌方向。X 主页 Banner 是另一种画幅与遮挡任务，不在本技能范围内。

## 安装与调用

仓库根目录就是 Codex Skill：[`SKILL.md`](SKILL.md)、`references/`、`assets/` 和 `scripts/` 放在一起，无需安装旁边的 `lany-avatar` 仓库。首次安装到 Windows 的 Codex 技能目录：

```powershell
git clone https://github.com/LanyXiaosheng/lany-cover-skill.git "$env:USERPROFILE\.codex\skills\lany-cover"
py -m pip install -r "$env:USERPROFILE\.codex\skills\lany-cover\requirements.txt"
```

若 `lany-cover` 目录已存在，先检查并保留现有文件，再更新；不要直接在已有目录上运行 `git clone`。如果 `$lany-cover` 未立即出现在可调用列表，重启 Codex 后再试。Python 辅助脚本依赖 [Pillow](https://pillow.readthedocs.io/)；生图本身还需要当前运行环境提供图像生成工具。

```text
使用 $lany-cover，给我的 X 长文做一张 5:2 封面。标题：REA邪修，AI不能立马赚钱，但能立马省钱。默认像素小生，视觉重点是“省钱”，不要编造金额。
```

```text
使用 $lany-cover，固定同一标题，分别测试：像素人物×浅色杂志、手绘人物×深色报告、丝印人物×高对比印刷。每组单独出图和验收，不修改我的默认头像。
```

只要提示词时明确说“仅提示词”；未提出多版时默认做一张。用户本轮指定的头像是身份真源，内置样例只用于媒介与品牌延续。

## 选择风格，不混淆身份

| 变量 | 回答的问题 | 可选例子 |
| --- | --- | --- |
| 人物媒介 | 小生怎么画？ | 像素、自然手绘、丝印、赛璐璐、立体潮玩、毛绒 |
| 封面语言 | 页面怎么组织？ | 深色报告、浅色编辑、撕纸拼贴、高对比印刷、极简画册 |
| 视觉重点 | 读者先看到什么？ | 标题、人物、过程、结果、真实产品 |

十种内置人物媒介及参考图见 [头像媒介目录](references/avatar-styles.md)。封面语言可以与人物媒介交叉搭配；同一张封面只出现一个小生、一种人物媒介。默认不使用金额、百分比或拟真截图来冒充结果，实际文章与发布平台确定后再设计封面，而不是复用测试图的构图。

## 六组混搭实测：同一标题，不同表达

测试标题固定为「**REA邪修，AI不能立马赚钱，但能立马省钱**」。每组有独立 [提示词](examples/rea-savings/prompts/) 与最终图；以下是风格探索，不是对 AI 节省金额的实证，也没有将候选头像升级成账号默认头像。版式拆分思路参考了 [xialingguo-ip](https://github.com/peggykangkang02/xialingguo-ip)，没有复用其人物或图片素材。

| 编号 | 人物 × 封面 | 本轮观察 |
| --- | --- | --- |
| 01 | 像素 × 浅色编辑杂志 | 延续当前识别度，适合稳定账号视觉；折页有轻微图表感 |
| 02 | 自然手绘 × 深色报告 | 稳重、适合长文，可继续精修 |
| 03 | 赛璐璐 × 撕纸拼贴 | 抓眼，但元素较多，长期使用可能冲淡识别 |
| 04 | 丝印 × 高对比实测 | “邪修”冲击力强；发布前可收敛颗粒与黄绿面积 |
| 05 | 立体潮玩 × 极简画册 | 干净，但较偏离日常像素身份，适合专题实验 |
| 06 | 毛绒 × 手写结果 | 有亲和力，更适合轻松主题 |

| 01 像素 × 浅色编辑杂志 | 02 手绘 × 深色报告 |
| --- | --- |
| [![01 像素封面](examples/rea-savings/01-pixel-editorial.png)](examples/rea-savings/01-pixel-editorial.png) · [提示词](examples/rea-savings/prompts/01-pixel-editorial.md) | [![02 手绘封面](examples/rea-savings/02-handdrawn-dark.png)](examples/rea-savings/02-handdrawn-dark.png) · [提示词](examples/rea-savings/prompts/02-handdrawn-dark.md) |
| 03 赛璐璐 × 撕纸拼贴 | 04 丝印 × 高对比实测 |
| [![03 赛璐璐封面](examples/rea-savings/03-cel-anime-collage.png)](examples/rea-savings/03-cel-anime-collage.png) · [提示词](examples/rea-savings/prompts/03-cel-anime-collage.md) | [![04 丝印封面](examples/rea-savings/04-screenprint-proof.png)](examples/rea-savings/04-screenprint-proof.png) · [提示词](examples/rea-savings/prompts/04-screenprint-proof.md) |
| 05 立体潮玩 × 极简画册 | 06 毛绒 × 手写结果 |
| [![05 潮玩封面](examples/rea-savings/05-vinyl-result.png)](examples/rea-savings/05-vinyl-result.png) · [提示词](examples/rea-savings/prompts/05-vinyl-result.md) | [![06 毛绒封面](examples/rea-savings/06-plush-handwritten.png)](examples/rea-savings/06-plush-handwritten.png) · [提示词](examples/rea-savings/prompts/06-plush-handwritten.md) |

本轮优先精修 **04 丝印版**和 **02 手绘深色版**；如果更重视账号连续识别，**01 像素浅色版**最稳。六张最终 PNG 均为 `1500×600`，已按选定背景模式做脚本检查，并目视核对标题与人物。脚本只能验证尺寸与简单背景特征，正式发布前仍需对照文章复核标题、视觉隐喻和结果表述。更早的「赛博小晚」[像素](examples/cyber-xiaowan/cover-pixel.png)与[手绘](examples/cyber-xiaowan/cover-soft-handdrawn.png)测试也保留在 `examples/`。

## 文件与验收约定

- X 长文默认 `5:2`、正式尺寸 `1500×600`；公众号默认 `2.35:1`，正文头图默认 `16:9`。用户指定比例或尺寸时以本次要求为准，不裁一张图兼容多个平台。
- 提示词、生成源图和最终图分开保存到 `<项目根>/lany-assets/lany-cover/<主题>/`。同名文件加 `-v2`、`-v3`，不覆盖已有结果。本仓库 `examples/` 只收录最终测试图与提示词，原始源图仍保留在本地创作目录。
- `scripts/prepare_reference.py` 生成轻量人物参考；`scripts/finalize_ratio.py` 仅在标题、脸和主体均落在目标安全区时裁切；`scripts/validate_output.py` 验证尺寸及深/浅背景启发式。`mixed` 模式只验证尺寸，不能替代目视检查。
- 辅助脚本不会替你判断错字、陌生脸、伪造数据或裁切后的视觉质量。任何一个不通过就继续修正，不把失败图作为正式封面交付。

```powershell
py scripts/validate_output.py examples/rea-savings/01-pixel-editorial.png --size 1500x600 --background light
```

修改辅助脚本后运行 `py -m unittest discover -s tests -v`；Codex 的展示名称与默认调用语位于 `agents/openai.yaml`。
